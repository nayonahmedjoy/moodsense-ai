# 😊 MoodSense-AI — Real-Time Emotion Detection

**MoodSense-AI** is a real-time emotion detection project that uses a webcam to analyze facial expressions and identify human emotions using **computer vision and deep learning**.

The system detects faces live and predicts emotions such as **happy**, **neutral**, and **surprise** using a pre-trained deep learning model.

---

## 🚀 Project Overview

MoodSense-AI captures live video from a webcam and:
- Detects human faces in real time
- Analyzes facial expressions
- Displays the dominant emotion on screen
- Shows emotion confidence scores

This project demonstrates how **AI can understand human emotions** using vision-based models.

---

## 🧠 How It Works

1. Webcam captures live video frames
2. Frames are passed to **DeepFace**
3. A deep learning model analyzes facial features
4. Emotion probabilities are returned
5. Dominant emotion is displayed on the video feed

The system runs fully **locally**, without cloud APIs.

---

## 🛠️ Technologies Used

- **Python**
- **OpenCV (cv2)**
- **DeepFace**
- **Deep Learning (Pre-trained models)**
- **Real-time Computer Vision**
- **Linux environment**

---

## 📁 Project Structure

```
MoodSense-AI/
│
├── main.py          # Real-time emotion detection script
├── README.md        # Project documentation
└── .gitignore
```

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install opencv-python deepface
```

> ⚠️ First run may download model weights automatically.

### 2️⃣ Run the program
```bash
python main.py
```

### 3️⃣ Controls
- Press **Q** to exit
- Or close the window manually

---

## 🎯 Purpose of This Project

- Learn real-time computer vision
- Work with deep learning facial analysis
- Build AI-powered interactive applications
- Strengthen ML & CV portfolio projects

---

## 🔮 Future Improvements

- Add more emotion categories
- Support multiple faces
- Improve UI overlay
- Export emotion logs
- Integrate with audio emotion analysis

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.  
Emotion detection may not always be accurate and should not be used for sensitive decision-making.

---

## 📜 License

Open-source project intended for learning and portfolio use.

---

## 🙌 Author

**Nayon Ahmed**  
Linux user | Python developer | Computer Vision enthusiast  
GitHub: https://github.com/nayonahmedjoy
