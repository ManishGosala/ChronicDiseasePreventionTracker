# 🩺 Chronic Disease Prevention Tracker

This project is an early warning system that monitors user health metrics (like glucose, blood pressure, BMI, and age) to predict the risk of chronic diseases such as:

- **Pre-diabetes**
- **Hypertension**
- **Metabolic Syndrome**

It uses a trained machine learning model to detect risk and suggest lifestyle-based intervention strategies.

---

## ✨ Features

- 🧠 AI-powered risk prediction
- 📈 User input for health metrics (Glucose, BP, BMI, Age)
- 🎯 Interactive UI using Jupyter Widgets
- 🎨 Styled web interface via Voila + CSS
- 📁 Modular: Easily extend to include more factors or conditions

---

## 📦 Requirements

Make sure you have:

- Python 3.8 or later
- Jupyter Notebook
- Voila
- ipywidgets
- pandas, numpy, scikit-learn, joblib

Install :
pip install notebook voila ipywidgets pandas numpy scikit-learn joblib

🪜 Project Structure
ChronicTracker/
├── chronic_tracker.ipynb      # Main notebook UI
├── train_model.py             # Generates the ML model (one-time run)
├── chronic_model.pkl          # Trained model used for predictions
├── styles.css                 # Custom CSS for beautiful UI
└── README.md                  # Project documentation

🧪 Setup Instructions
1️⃣ Clone or download this repo
2️⃣ Create and activate virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate  
3️⃣ Install dependencies
pip install notebook voila ipywidgets pandas numpy scikit-learn joblib
4️⃣ Generate model (if not already present)
python train_model.py
🚀 Run the Web App
Launch with:
voila chronic_tracker.ipynb

Screenshot:
![image](https://github.com/user-attachments/assets/5901e7f7-ff69-42c6-ad4a-41a142cc401c)




