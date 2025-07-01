# 🧠 Amboozepedia QueryX

**Amboozepedia QueryX** is a powerful desktop application built with Python and Tkinter that allows users to retrieve intelligent, well-structured information using **OpenAI's ChatGPT API**, with **Wikipedia** as a reliable fallback source.

This hybrid approach ensures accurate and context-rich results, blending AI-generated content with factual encyclopedic summaries.

<p align="center">
  <img src="https://github.com/user-attachments/assets/707e1a33-2ed8-44f2-9b51-149cfa18c85a" width="300" alt="Main UI">
</p>



---

## 🚀 Features

- 🔍 **Smart Search** powered by ChatGPT (GPT-3.5 Turbo)
- 📚 **Wikipedia Fallback** for guaranteed results
- 🧠 **Natural Language Understanding**
- 📝 **Interactive GUI** with clean, modern design
- 🔒 **API-secured access to OpenAI**
- 🧹 **Clear & Disable/Edit Modes** for flexible output control
- 📦 Ready for **PyInstaller Packaging**

---

## 🖥️ Screenshots

<!-- You can include screenshots like this if you want -->

<h2 align="center">Graphical User Interface</h2> 
<p align="center">
<img src="https://github.com/user-attachments/assets/68b4fcc0-8f03-40f9-84aa-1390e31c1b02" width="800" alt="Main UI">

</p>
<h2 align="center">Search Result View: </h2>
<p align="center">
<img src="https://github.com/user-attachments/assets/bdeb63fd-7e47-4ee4-897b-59dabd27c087" width="800" alt="ChatGPT Result">
</p>

<h2 align="center">Enable Mode: </h2>
<p align="center">
<img src="https://github.com/user-attachments/assets/a0a48bcb-af0a-4c02-9386-911343838279" width="800" alt="ChatGPT Result">
</p>

<h2 align="center">Disable Mode: </h2>
<p align="center">
<img src="https://github.com/user-attachments/assets/af168d59-aaa2-4d69-90bc-0fea77082012" width="800" alt="ChatGPT Result">
</p>

<h2 align="center">Clear Mode: </h2>
<p align="center">
<img src="https://github.com/user-attachments/assets/da72f9e6-958e-4bda-921a-e9edf4e2ff08" width="800" alt="ChatGPT Result">
</p>

---

## 🧑‍💻 Developed By

**Ambooj Kumar Sharma**  
`Software Developer | Python Enthusiast | AI Integrator`

---

## ⚙️ How It Works

1. Type any topic into the search box.
2. The app first queries **ChatGPT** via OpenAI’s API.
3. If ChatGPT is unavailable or fails, it falls back to **Wikipedia**.
4. The response is shown in the text area. You can enable/disable editing.
5. Use the **Clear** button to reset the UI.

---

## 📦 Installation

### 🐍 Requirements

- Python 3.8 or higher
- Internet connection (for ChatGPT/Wikipedia)
- OpenAI API key

### 🧰 Dependencies

Install the required Python libraries:

```bash
pip install openai wikipedia
```

---

## 🛠️ Run the App

```bash
python amboozepedia.py
```

- 💡 Make sure to replace "sk-..." in the code with your actual OpenAI API key.

---

##🔐 OpenAI API Setup

1. Go to https://platform.openai.com/account/api-keys
2. Generate a new API key.
3. Replace the placeholder key in main.py:

```bash
openai.api_key = "sk-YourRealAPIKeyHere"
```

✅ For production use, store the API key as an environment variable.

---

## 📁 File Structure

```bash
Amboozepedia-QueryX/
│
├── amboozepedia.py                # Main application file
├── amboozepedia_icon.ico  # App icon
├── README.md              # You're reading it
├── requirements.txt       # Optional: List of dependencies
└── screenshots/           # App screenshots (optional)
```

---

## 🔧 Packaging as .exe (Optional)

To convert your app to an executable (Windows):

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --icon=amboozepedia_icon.ico main.py
```
- Output will be in the /dist directory.

---

## 🛡 License

- This project is licensed under the MIT License — see the LICENSE file for details.

## 💬 Feedback & Contribution

- Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.
- If you find a bug or want to request a feature, feel free to open an issue.

## ⚡ “Knowledge is power — make it intelligent.” – Amboozepedia

