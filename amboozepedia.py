import os
import sys
from tkinter import *
from tkinter import messagebox
import wikipedia
from openai import OpenAI

#Your OpenAI API key
client = OpenAI(api_key="Enter_your_OpenAI_API_Key")



def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class SearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Amboozepedia QueryX | Developed by Ambooze | Ambooj Kumar Sharma")
        self.root.iconbitmap(resource_path("amboozepedia_icon.ico"))
        self.center_window(1360, 800)
        self.root.config(bg="#262626")

        # ---------------------- GUI Layout ------------------------
        title = Label(self.root, text="Wikipedia + ChatGPT", font=("times new roman", 35, "bold"), bg="#e4cccc", fg="#262626")
        title.place(x=0, y=0, relwidth=1)

        LabelFrame(self.root, text="Type Here:", font=("times new roman", 12, "bold"), bg="#262626", fg="white").place(x=10, y=60, width=1340, height=80)

        self.var_search = StringVar()
        Entry(self.root, textvariable=self.var_search, font=("times new roman", 20), bg="#e4cccc").place(x=20, y=85, width=415, height=40)

        Button(self.root, text="Search", command=self.searchword, font=("times new roman", 20), bg="grey", fg="white", padx=50).place(x=450, y=85, height=41)
        Button(self.root, text="Clear", command=self.clear, font=("times new roman", 20), bg="grey", fg="white", padx=50).place(x=660, y=85, height=41)
        Button(self.root, text="Enable Mode", command=self.enable, font=("times new roman", 20), bg="grey", fg="white", padx=50).place(x=855, y=85, height=41)
        Button(self.root, text="Disable", command=self.disable, font=("times new roman", 20), bg="grey", fg="white", padx=50).place(x=1140, y=85, height=41)

        # ---------------------- Text Display ------------------------
        self.frame1 = LabelFrame(self.root, font=("times new roman", 15))
        self.frame1.place(x=15, y=150, width=1326, height=530)

        scrolly = Scrollbar(self.frame1, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        self.txt_area = Text(self.frame1, font=("times new roman", 15), yscrollcommand=scrolly.set)
        self.txt_area.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_area.yview)

        # ---------------------- Footer ------------------------
        footer = Label(self.root, text="Amboozepedia QueryX | © 2025 Ambooze (Ambooj Kumar Sharma). All rights reserved.",
                       font=("times new roman", 10), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X, pady=8)

    # -------------------- Functionalities --------------------
    def enable(self):
        self.txt_area.config(state=NORMAL)
        self.frame1.config(text="Mode: Enable")

    def disable(self):
        self.txt_area.config(state=DISABLED)
        self.frame1.config(text="Mode: Disable")

    def searchword(self):
        query = self.var_search.get().strip()
        if not query:
            messagebox.showerror("Error", "Search area should not be empty!")
            return

        self.txt_area.delete('1.0', END)
        self.txt_area.insert(END, "Searching ChatGPT...\n\n")

        try:
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Tell me about: {query}"}
                ],
                max_tokens=1000,
                temperature=0.7
            )
            result = response.choices[0].message.content
            self.txt_area.delete('1.0', END)
            self.txt_area.insert('1.0', result)

        except Exception as chat_err:
            try:
                fallback = wikipedia.summary(query)
                self.txt_area.delete('1.0', END)
                self.txt_area.insert('1.0', fallback)
            except Exception as wiki_err:
                messagebox.showerror("Error", f"Both ChatGPT and Wikipedia failed.\n\nChatGPT: {chat_err}\n\nWikipedia: {wiki_err}")

    def clear(self):
        self.var_search.set("")
        self.txt_area.delete('1.0', END)
        self.frame1.config(text="")

    def center_window(self, width=1360, height=800):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
root = Tk()
app = SearchApp(root)
root.mainloop()