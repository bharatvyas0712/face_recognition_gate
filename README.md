# 🎯 Face Recognition Gate System

A **Face Recognition Gate** project using **Python, OpenCV, and face_recognition**.  
This system captures faces, trains them, and recognizes users in **real-time** to allow or deny access (like a smart gate system).

---

## ✨ Features
✅ Capture images from webcam  
✅ Train model with stored encodings  
✅ Real-time face recognition  
✅ Access control (Known = Allowed, Unknown = Denied)  
✅ Easy to extend and customize  

---

## 🛠 Tech Stack
- **Python 3.x**
- **OpenCV**
- **face_recognition (dlib)**
- **NumPy**
- **pickle**

---

## 📂 Project Structure
```

📦 face\_recognition\_gate
┣ 📂 dataset/          # Captured face images
┣ 📂 encodings/        # Saved encodings (pickle files)
┣ 📜 capture\_images.py # Capture dataset images
┣ 📜 train\_model.py    # Encode faces and train model
┣ 📜 recognize.py      # Real-time recognition
┣ 📜 requirements.txt  # Python dependencies
┗ 📜 README.md         # Documentation

````

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/face_recognition_gate.git
cd face_recognition_gate
````

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv myenv
# Activate it
myenv\Scripts\activate   # Windows
source myenv/bin/activate  # Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Step 1: Capture Images

```bash
python capture_images.py
```

### Step 2: Train Model

```bash
python train_model.py
```

### Step 3: Run Recognition

```bash
python recognize.py
```

---

## 🚀 Future Enhancements

* 🔐 Database integration for storing encodings
* 🌐 Web or GUI interface for user management
* 🔧 Hardware integration (Servo Motor / Smart Lock)
* 📷 Multi-camera support

---

## 👨‍💻 Author

**Bharat Vyas**
📌 GitHub: [bharatvyas0712](https://github.com/bharatvyas0712)

