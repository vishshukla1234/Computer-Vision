# 🖐️ Virtual Hand Volume Controller

A Computer Vision project that allows you to **control your system volume using hand gestures** in real time.  
Built using **OpenCV**, **MediaPipe**, and **Pycaw**, this project detects your hand and adjusts the audio volume based on the distance between your thumb and index finger.

---

## 🎥 Features
- Real-time hand tracking using **MediaPipe Hands**
- Volume control through **thumb-index finger distance**
- Dynamic volume bar and percentage display
- Smooth and responsive performance
- Works entirely with your webcam — no external hardware needed

---

## 🧠 Technologies Used
- **Python 3**
- **OpenCV** – for image processing and visualization
- **MediaPipe** – for real-time hand landmark detection
- **NumPy** – for numerical computations
- **Pycaw** – for system audio control on Windows
- **Math** – for calculating distance between landmarks

---

## ⚙️ How It Works
1. The webcam captures live video frames.
2. **MediaPipe** detects your hand landmarks.
3. The distance between your **thumb tip (id 4)** and **index fingertip (id 8)** is measured.
4. This distance is mapped to the system’s volume range using interpolation.
5. The **volume level**, **bar**, and **percentage** are displayed on screen.

| Gesture | Action |
|----------|---------|
| 🤏 Thumb and Index close | Low Volume |
| ✋ Thumb and Index far apart | High Volume |


