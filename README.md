# 🏋️ AI Real-time Gym Coach

An AI-powered real-time fitness coaching application built using Streamlit, MediaPipe, Groq LLMs, WebRTC, and Text-to-Speech.

This application analyzes user body posture in real-time through webcam input, tracks workout performance, counts repetitions, monitors exercise form, and provides intelligent AI-based voice feedback like a virtual gym trainer.

---

# 🚀 Features

## ✅ Real-time Pose Detection

* Uses MediaPipe Pose Landmarker for real-time body landmark tracking.
* Detects exercise posture through webcam feed.
* Calculates body joint angles for exercise analysis.

## ✅ AI Workout Coaching

* Integrates Groq LLM's for dynamic coaching feedback.
* Generates contextual fitness guidance.
* Motivational AI responses during workouts.

## ✅ Voice Feedback System

* Real-time AI voice coaching.
* Audio playback after workout events.
* Personalized exercise feedback.

## ✅ Supported Exercises

* Squats
* Push-ups
* Biceps Curls
* Shoulder Press
* Lunges

## ✅ Exercise Metrics Tracking

Tracks metrics like:

* Knee angle
* Elbow angle
* Torso angle
* Body alignment
* Hip stability
* Shoulder stability
* Exercise depth

## ✅ Workout Progress Monitoring

* Real-time repetition counting
* Set tracking
* Workout completion monitoring
* Total workout statistics

## ✅ Workout History

* Stores completed workouts in database
* Aggregated exercise analytics
* Date-wise tracking

## ✅ Authentication System

* User login support
* Session-based authentication

## ✅ Streamlit WebRTC Integration

* Browser webcam streaming
* Real-time frame processing
* Low-latency video analysis

---

# 🧠 Tech Stack

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| Python           | Backend Logic             |
| Streamlit        | Web Application           |
| MediaPipe        | Pose Detection            |
| Streamlit WebRTC | Real-time Video Streaming |
| Groq API         | LLM Coaching              |
| SQLite           | Workout Storage           |
| Pandas           | Data Analysis             |
| OpenCV           | Frame Processing          |
| Text-to-Speech   | Voice Coaching            |

---

# 📂 Project Structure

```bash
AI_Gym_Coach/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── pose_landmarker_full.task
│
├── static/
│   ├── style.css
│   └── AdobeClean.otf
│
├── services/
│   ├── auth/
│   ├── coaching/
│   ├── config/
│   ├── persistence/
│   ├── state/
│   ├── tracking/
│   ├── ui/
│   └── vision/
│
├── ml_models/
│   └── pose_landmarker_full.task
│
└── .streamlit/
    └── secrets.toml
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Utkarsh263/AI_Gym_Coach.git
```

---

## 2️⃣ Move Into Project Directory

```bash
cd AI_Gym_Coach
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate environment:

```bash
.venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure API Keys

Create:

```bash
.streamlit/secrets.toml
```

Add:

```toml
GROQ_API_KEY = "gsk_"
```

---

# 📥 Download MediaPipe Model

Download:

[https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_full/float16/latest/pose_landmarker_full.task](https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_full/float16/latest/pose_landmarker_full.task)

Place file inside:

```bash
ml_models/
```

Final path:

```bash
ml_models/pose_landmarker_full.task
```

---

# ▶️ Run Application

```bash
streamlit run main.py
```

Application will start at:

```bash
http://localhost:8501
```

---

# 🎮 How It Works

## Step 1

Login into the application.

## Step 2

Select:

* Exercise type
* Number of sets
* Repetitions

## Step 3

Click:

```bash
Start Workout
```

## Step 4

Allow:

* Camera permissions
* Audio permissions

## Step 5

Perform exercise in front of webcam.

## Step 6

AI system:

* Tracks pose landmarks
* Detects exercise movement
* Counts repetitions
* Evaluates form
* Provides voice coaching

---

# 🧠 AI Coaching Workflow

```bash
Webcam Feed
      ↓
WebRTC Stream
      ↓
MediaPipe Pose Detection
      ↓
Exercise Form Analysis
      ↓
Workout Metrics Engine
      ↓
Groq LLM Coach
      ↓
Text-to-Speech
      ↓
Voice Feedback
```

---

# 📊 Metrics Monitored

## Squats

* Knee Angle
* Back Angle
* Squat Depth

## Push-ups

* Elbow Angle
* Hip Alignment
* Body Posture

## Biceps Curls

* Elbow Angle
* Shoulder Stability
* Swing Detection

## Shoulder Press

* Arm Extension
* Elbow Angle
* Back Arch

## Lunges

* Front Knee Angle
* Torso Angle
* Balance Stability

---

# 🗄️ Database Features

The application stores:

* Exercise history
* Workout duration
* Repetition counts
* Set counts
* Workout dates

---

# 🎤 Voice Coaching Features

The AI coach can:

* Motivate user
* Congratulate completed sets
* Give posture corrections
* Announce workout completion
* Provide contextual fitness guidance

---

# 🌐 Streamlit Deployment

## Deploy on Streamlit Cloud

1. Push project to GitHub
2. Open Streamlit Cloud
3. Connect GitHub repository
4. Select `main.py`
5. Add secrets:

```toml
GROQ_API_KEY="your_api_key"
```

6. Deploy application

---

# 🔒 Security Notes

Do NOT upload:

* `.env`
* `.venv`
* `.streamlit/secrets.toml`

Use `.gitignore` properly.

---

# 🛠️ Future Improvements

* Real-time form correction overlay
* Calorie estimation
* Advanced exercise recognition
  
---

# 📈 Project Highlights

✅ Real-time AI fitness coaching

✅ Computer vision based exercise tracking

✅ LLM-powered motivational feedback

✅ Voice interaction system

✅ Streamlit WebRTC integration

✅ Modular architecture

✅ Event-driven workout pipeline

---

# 🧪 Known Limitations

* Browser autoplay restrictions may affect voice playback.
* Webcam quality impacts pose accuracy.
* High CPU usage during continuous video processing.
* Streamlit rerun loops may affect latency.

---

# 👨‍💻 Author

Utkarsh Kohli

AI + Computer Vision 

---

