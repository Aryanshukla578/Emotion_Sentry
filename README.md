# 🧠 Emotion Sentry – Real-Time Emotion Detection + Action Engine

**Emotion Sentry** is an AI-powered desktop/web app that continuously scans a user's facial expressions to detect emotions like stress, anger, sadness, or happiness — and triggers appropriate actions (like locking the screen, alerting a supervisor, or launching calm-mode).

> 🛡️ Originally built for personal security, productivity boosters, and mental health awareness.

---

## 🚀 Features

- 🎥 Real-time webcam feed analysis (OpenCV)
- 😐 Emotion classification using CNN / DeepFace / FER
- 🛑 Action triggers:
  - Lock screen on "stress/anger"
  - Play music on "sad"
  - Notify admin (optional)
- 📊 Emotion logging for analytics
- 🧠 Streamlit / Tkinter GUI support

---

## 🧰 Tech Stack

| Module | Tech Used |
|--------|-----------|
| Face Detection | OpenCV / Mediapipe |
| Emotion Classification | `fer` / `DeepFace` / custom CNN |
| GUI | Streamlit / Tkinter |
| Alert Actions | Python subprocess, OS triggers |
| Logs | JSON / CSV / SQLite |

---

## 🖥️ How to Run

1. **Clone the Repo**

```bash
git clone https://github.com/Aryanshukla578/Emotion_Sentry.git
cd Emotion_Sentry
pip install -r requirements.txt
streamlit run app.py

2.📁 Folder Structure
Emotion_Sentry/
├── app.py                  # Streamlit GUI
├── gui_app.py              # Tkinter GUI (if present)
├── models/                 # Trained model weights (if custom)
├── core/
│   ├── emotion_detect.py   # Emotion classifier
│   ├── action_engine.py    # What to do based on emotion
├── logs/
│   └── emotion_log.csv     # Logged emotion data
├── assets/
│   └── calm_music.mp3      # Auto-play on sad/stress
└── requirements.txt
🔒 Use Cases
👩‍💻 Lock screen if user is angry (for sensitive tasks)

📉 Alert if mental stress detected during study/work

👨‍🏫 Classroom attention tracking

🚨 Alert if someone uses computer under stress/duress
📜 License
MIT License. Free to use, improve, or fork for your own AI sentry!

🧠 Made with ❤️ by Aryan Shukla
Building next-gen AI + Cybersecurity systems for Bharat 🚀
