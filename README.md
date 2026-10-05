# 🚗 Driver Drowsiness Detection System

### A Real-Time Safety System Using Computer Vision

## 📌 Overview

The **Driver Drowsiness Detection System** is a real-time computer vision prototype designed to detect signs of driver fatigue.

The system continuously monitors the driver's face through a webcam and analyzes **eye closure** and **yawning behavior**. When drowsiness or yawning is detected, the system generates visual, voice, and beep alerts to warn the driver.

The project uses **Dlib's pre-trained 68-point facial landmark model** along with **Eye Aspect Ratio (EAR)** and **Mouth Aspect Ratio (MAR)** for facial behavior analysis.

---

## 🎯 Objectives

- Design a real-time driver monitoring system using computer vision
- Detect driver fatigue through eye closure and yawning patterns
- Implement EAR and MAR for behavioral analysis
- Provide instant voice and beep alerts
- Develop a low-cost safety solution
- Enhance driver and road safety

---

## ⚙️ System Architecture

```text
┌──────────────────────┐
│       Webcam         │
│   Real-time Video    │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│       OpenCV         │
│   Frame Processing   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│        Dlib          │
│   Face Detection     │
│  68 Facial Landmarks │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│  Eye & Mouth Analysis│
│       EAR / MAR      │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Threshold Comparison │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Drowsiness / Yawning │
│      Detection       │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│   Alert Generation   │
│ Voice + Beep + Visual│
└──────────────────────┘

```
---

## 🧠 How It Works

1. **Video Acquisition** – A webcam captures real-time video of the driver.
2. **Frame Processing** – OpenCV processes the video frames.
3. **Face Detection** – Dlib detects the driver's face.
4. **Facial Landmark Detection** – The pre-trained 68-point model identifies important facial points.
5. **EAR Calculation** – Eye Aspect Ratio is used to analyze eye closure.
6. **MAR Calculation** – Mouth Aspect Ratio is used to analyze yawning.
7. **Threshold Comparison** – EAR and MAR are compared with predefined thresholds.
8. **Alert Generation** – Voice, beep, and visual alerts are generated when required.

---

## 👁️ Drowsiness Detection

The system uses **Eye Aspect Ratio (EAR)** to analyze eye closure.

- When the eyes are open, the EAR value remains relatively high.
- When the eyes close, the EAR value decreases.
- If the EAR remains below `0.25` for `20` consecutive frames, drowsiness is detected.
- The system then activates the alert system.

---

## 😮 Yawning Detection

The system uses **Mouth Aspect Ratio (MAR)** to analyze yawning.

- When the mouth is open widely, the MAR value increases.
- If the MAR exceeds `0.75` for `15` consecutive frames, yawning is detected.
- The system then activates the alert system.

---

## 🚨 Alert System

When drowsiness or yawning is detected, the system provides:

- 🔊 Voice alert
- 🔔 Continuous beep
- ⚠️ Visual warning

The alerts continue while the detected condition remains active.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenCV | Real-time video and image processing |
| Dlib | Face and facial landmark detection |
| 68-Point Facial Landmark Model | Detects facial landmarks |
| NumPy | Numerical operations |
| SciPy | Distance calculations |
| Imutils | Image processing utilities |
| Pyttsx3 | Voice alerts |
| Winsound | Beep alerts |

---

## 💻 Requirements

- Python 3.x
- Webcam
- Speaker/audio output
- Windows operating system
- Minimum 4 GB RAM
- Dlib 68-point facial landmark model

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/shivakumarreddy-1819/Driver-Drowsiness-Detection.git
cd Driver-Drowsiness-Detection

Install the required Python packages:

```bash
pip install -r requirements.txt
```
---

## 🧠 Facial Landmark Model

This project uses Dlib's pre-trained **68-point facial landmark predictor**.

Download the `shape_predictor_68_face_landmarks.dat` model file and place it inside the project folder.

> The model file is not included in this repository because of its large file size.

---

## ▶️ Run the Project

After installing the dependencies and placing the facial landmark model in the project folder, run:

```bash
python drowsiness.py
```
---

## 🌍 Applications

- 🚗 Personal Vehicles
- 🚛 Commercial Trucks
- 🚌 Public Transportation
- 🚚 Fleet Management
- 🌙 Night-Time Driving
- 🛡️ Advanced Driver Assistance Systems (ADAS)
- 🏗️ Industrial and Heavy Vehicles

---

## 🚀 Future Scope

The system can be further enhanced with the following features:

- 🧭 **Head Pose Detection** – Detect driver distraction and head movement.
- 📱 **Mobile Phone Usage Detection** – Identify mobile phone usage while driving.
- 🆘 **Automatic Emergency Alert** – Send an emergency notification when the driver becomes unresponsive.
- 🚘 **Vehicle Control Integration** – Integrate the system with vehicle safety and control mechanisms.
- ☁️ **IoT and Cloud Integration** – Store and monitor driver behavior data remotely.
- 🤖 **Deep Learning Enhancement** – Improve detection accuracy using advanced deep learning techniques.

---

## 👥 Project Team

- **N Shiva Kumar Reddy**
- **Nallareddy Charishma**

---

## ⚠️ Disclaimer

This project is an academic prototype developed for educational and demonstration purposes. It should not be considered a certified automotive safety system.

---