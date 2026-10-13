# KINETIQ: Physics-Informed Sign-to-Speech Communication Platform
### An Accessible AI Communication Initiative by Sanchar Saathi and FIOL

> **"Your Gestures. Your Language. Your Voice."**  
> An assistive communication system combining 21-landmark hand tracking, Newtonian biomechanics, multilingual translation, and real-time speech synthesis.

---

## ⚡ Quick Start (2 Ways)

Run this project immediately in your browser without installing node_modules or configuring build tools.

### Option 1: Terminal Command (Recommended)
1. Navigate to the project directory:
   ```bash
   cd c:\Users\monoj\Downloads\kinetiq-hand-physics
   ```
2. Start the local server:
   ```bash
   python server.py
   ```
3. Your default web browser will automatically open to `http://localhost:8000`.

### Option 2: Live Server Extension
1. Install the **Live Server** extension in VS Code.
2. Right-click on `index.html` in the file explorer and choose **"Open with Live Server"**.

---

## 🌟 Core Product Architecture & Features

### 1. KINETIQ Translate (Main Communication Hub)
- **Live Camera & Hand-Skeleton Viewport**:
  - 21 anatomical landmarks tracked at 60 FPS in-browser.
  - Color-coded joint nodes (wrist, knuckles, phalanges, fingertips).
  - Clear real-time status indicators: **Ready**, **Hand Detected**, **Recognizing...**, and **Translated Result**.
  - Camera management: **Start**, **Pause / Resume**, **Stop**, and **Retry** controls.
  - Interactive Demo Mode with 5 mathematical presets (**Wave**, **Sharp Strike**, **Gentle Tap**, **Precision Pinch**, **Angular Swirl**) when camera is unavailable.
  - 100% on-device WebAssembly/WebGL processing ensuring complete privacy (no video frames sent to servers).
- **Dedicated Multilingual Output Panel**:
  - Large, high-contrast, easily readable translated message display.
  - **User-Controlled Output Language Selector**:
    - 🇬🇧 English
    - 🇧🇩 বাংলা (Bengali)
    - 🇮🇳 हिन्दी (Hindi)
    - 🇪🇸 Español (Spanish)
    - 🇫🇷 Français (French)
  - Switching languages dynamically updates the translated message without interrupting camera tracking.
  - **Text-to-Speech (TTS)**: Reads the translated message aloud in the selected language with an animated soundwave indicator.
  - Quick action controls: **Speak Aloud**, **Copy Text** (with clipboard toast), **Try Again**, and **Clear**.
  - **Interactive Supported Gestures Chips**: One-click cheatsheet to understand and test each supported gesture.
  - **Recent Conversation Log**: Stores conversation history with timestamps, language tags, and quick replay/copy buttons.

### 2. Motion Physics Telemetry HUD
- Real-time measurements derived from continuous 21-landmark Center-of-Mass (CoM) tracking:
  - **Linear Velocity** $v(t) = \frac{\Delta p}{\Delta t}$ ($m/s$)
  - **Linear Acceleration** $a(t) = \frac{\Delta v}{\Delta t}$ ($m/s^2$)
  - **Jerk (Abruptness)** $j(t) = \frac{\Delta a}{\Delta t}$ ($m/s^3$)
  - **Estimated Kinetic Energy** $KE(t) = \frac{1}{2}mv^2 + \frac{1}{2}I\omega^2$ (Joules, Dempster mass $\approx 0.45\text{ kg}$)
  - Angular Velocity $\omega$ ($rad/s$), Movement Smoothness (SPARC index), and Palm Roll/Pitch.
  - Inspectable **98-Dimensional Feature Vector** ready for ML pipeline ingestion.

### 3. Motion Physics Dashboard (Multi-Trace Oscilloscope)
- Synchronized, high-performance 60 FPS HTML5 Canvas charts showing continuous historical trajectories for velocity, acceleration, jerk, and kinetic energy over a 120-frame rolling window.

### 4. Physics Playground ($KE = \frac{1}{2}mv^2$)
- Interactive speed ($0.1$ to $4.0\text{ m/s}$) and hand mass ($0.25$ to $0.75\text{ kg}$) sliders.
- Dynamic parabolic power curve graph.
- **16× Energy Multiplier Evidence**: Demonstrates why quadrupling velocity produces 16 times greater kinetic energy, providing an unmistakable signal for AI gesture disambiguation.

### 5. Model Comparison Lab (Ablation Benchmark)
- Three-way architectural comparison:
  1. **Shape-Only (Model A)**: Static spatial landmark geometry.
  2. **Dynamics-Only (Model B)**: Velocity and acceleration vectors without shape.
  3. **Shape + Dynamics (Model C - Proposed)**: Physics-informed hybrid pipeline.
- Interactive **Confusion Matrix Visualizer** demonstrating how physics eliminates confusion between dynamic twin gestures (e.g. "Wait" vs "Halt!").

### 6. Interactive 7-Stage Pipeline
- Expandable cards detailing:
  1. Video Ingestion & Landmark Extraction
  2. Bone Vectors & Joint Flexion Angles
  3. Low-Pass Trajectory Smoothing
  4. Kinematic Higher-Order Numerical Differentiation
  5. Rigid-Body Dynamics & Kinetic Energy Formulation
  6. Physics-Informed Feature Vector Assembly
  7. Gesture Disambiguation & Classification

---

## 📐 Mathematical Formulation

### 1. Center-of-Mass (CoM) Estimation
Using Dempster (1955) anthropometric hand segment mass distributions:
$$\mathbf{P}_{CoM}(t) = \sum_{i=0}^{20} w_i \mathbf{P}_i(t)$$
where $w_0 = 0.20$ (wrist), $w_{\text{metacarpals}} \approx 0.32$, and $w_{\text{phalanges}} \approx 0.48$.

### 2. Numerical Kinematics
$$\mathbf{v}(t) = \frac{\mathbf{P}_{CoM}(t) - \mathbf{P}_{CoM}(t-\Delta t)}{\Delta t}$$
$$\mathbf{a}(t) = \frac{\mathbf{v}(t) - \mathbf{v}(t-\Delta t)}{\Delta t}, \quad \mathbf{j}(t) = \frac{\mathbf{a}(t) - \mathbf{a}(t-\Delta t)}{\Delta t}$$

### 3. Rigid-Body Kinetic Energy
$$KE = \frac{1}{2} m \|\mathbf{v}_{CoM}\|^2 + \frac{1}{2} \boldsymbol{\omega}^T \mathbf{I} \boldsymbol{\omega}$$
where $m \approx 0.45\text{ kg}$ and $\mathbf{I} \approx \frac{1}{12} m (w^2 + h^2)$.

---

## 🎤 2-Minute Demonstration Script for Evaluators

1. **The Human Challenge (First 15s)**:
   > *"Millions of deaf and hard-of-hearing individuals face daily communication barriers with people who do not understand sign language. We created KINETIQ as an accessible AI initiative by Sanchar Saathi and FIOL to turn hand gestures directly into readable and spoken words in multiple languages."*

2. **The Translation Walkthrough (Next 45s)**:
   > *"Here in KINETIQ Translate, a person makes a gesture in front of their webcam. Notice the side-by-side layout: while the camera tracks hand landmarks in real-time on-device, the translated message appears prominently in the output panel. Watch how easily we can toggle the language between English, Bengali, Hindi, Spanish, or French—and tap 'Speak Aloud' to voice the message instantly."*

3. **The Physics Disambiguation Advantage (Next 30s)**:
   > *"Traditional computer vision only inspects static 2D hand shapes. In human sign communication, a gentle tap and an urgent stop command share similar hand shapes—they differ in velocity, jerk, and kinetic energy. In our Physics Playground, we demonstrate that quadrupling speed produces 16 times more kinetic energy, giving our AI a physical understanding of motion."*

4. **Scientific Honesty & Vision (Final 30s)**:
   > *"Everything runs 100% privately in the browser with zero cloud dependencies. Our current vocabulary covers core conversational phrases with kinematic disambiguation, and continuous sign language expansion is actively underway."*

---

## 📁 File Structure

```
kinetiq-hand-physics/
│
├── index.html                 # Complete Single-Page Application
├── server.py                  # Zero-dependency local dev server
├── README.md                  # Documentation and presentation guide
│
├── css/
│   └── styles.css             # Cyber grid, glassmorphism, soundwaves, scanline
│
├── js/
│   ├── physics-engine.js      # Biomechanical kinematics & Dempster CoM
│   ├── synthetic-demo.js      # 5 synthetic trajectory generators (60 FPS)
│   ├── mediapipe-tracker.js   # MediaPipe Hands, Pause/Resume, Canvas overlays
│   ├── charts-dashboard.js    # High-performance Canvas oscilloscopes
│   ├── gesture-classifier.js  # Multilingual translator, debounce, speech engine
│   ├── playground.js          # Interactive KE = 0.5*m*v^2 explorer
│   ├── model-comparison.js    # Ablation study & confusion matrix
│   ├── hero-visualizer.js     # 3D interactive hero canvas
│   └── app.js                 # Master coordinator & UI event handlers
│
└── backend/
    └── api.py                 # Optional FastAPI + NumPy/SciPy backend
```

---

## 🏆 Sanchar Saathi & FIOL Deployment Checklist

- [x] Dedicated KINETIQ Translate communication interface with 2-column layout.
- [x] Multilingual translation engine (English, Bengali, Hindi, Spanish, French).
- [x] Web Speech API Text-to-Speech synthesis with animated soundwave indicator.
- [x] Debounced classification logic preventing duplicate message spam.
- [x] Real-time 21-landmark hand tracking with color-coded joint overlays.
- [x] Start, Pause, Resume, Stop, and Retry camera controls.
- [x] Complete privacy: 100% on-device client-side inference.
- [x] Full fallback synthetic demo mode with 5 distinct gesture presets.
- [x] Live velocity, acceleration, jerk, and kinetic energy graphs with SI units.
- [x] Interactive kinetic energy playground with the 16× energy explanation.
- [x] Model comparison lab with interactive confusion matrices.
- [x] Established Sanchar Saathi & FIOL branding across all interfaces.
- [x] Zero-dependency launch via `python server.py`.
