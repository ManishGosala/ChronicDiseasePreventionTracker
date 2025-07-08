# 🩺 Chronic Disease Prevention Tracker by Manish Gosala

This project is a personalized early detection system that predicts the risk of chronic conditions like **Diabetes**, **Hypertension**, and **Metabolic Syndrome** based on user lifestyle data.

It is built entirely in **Jupyter Notebook** using **machine learning** with `ipywidgets` for interactivity — no web development frameworks like Flask or Streamlit involved.

---

## 🎯 Problem Statement

**Can we build a notebook-based health tracker that takes simple lifestyle inputs (BMI, smoking habits, activity level, etc.) and predicts early signs of chronic diseases?**  
This tool aims to help users receive early warnings and actionable health tips, promoting prevention through awareness.

---

## 🔍 Dataset Used

- `diabetes_binary_health_indicators_BRFSS2015.csv`  
  (Sourced from [Kaggle](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset))

Features used:
- High Blood Pressure
- High Cholesterol
- BMI
- Age
- Physical Activity
- Smoking
- Fruits and Vegetables intake (used to create `diet_score`)
- Engineered features: `lifestyle_score` and `diet_score`

---

## ✅ Features

- 🧠 Machine Learning model for chronic disease risk detection
- 🧾 Personalized lifestyle recommendations based on input
- 📊 Risk tracking over time (saved in a CSV log)
- 📈 BMI visualization (optional)
- 🧪 Built-in tips to reduce risk and stay healthy

---

## 🗂️ Project Structure

```
ChronicTracker/
├── chronic_tracker.ipynb              # Jupyter notebook with input form & predictions
├── train_model.py                     # Script to train the ML model
├── chronic_model.pkl                  # Trained ML model saved using joblib
├── diabetes_binary_health_indicators_BRFSS2015.csv  # Dataset
└── README.md                          # Project description
```

---

## 💻 How to Run (No Website Involved)

1. Clone or download this repo

2. **Install dependencies and run:**

```bash
pip install notebook ipywidgets pandas numpy scikit-learn joblib

# Train the model
python train_model.py

# Launch Jupyter Notebook
jupyter notebook chronic_tracker.ipynb
```

Then interact with the notebook UI to enter values and see real-time predictions and lifestyle suggestions.

---

## 📊 Dataset Source

- **File**: `diabetes_binary_health_indicators_BRFSS2015.csv`  
- **Source**: [Kaggle Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)

---

## 👨‍💻 Author

**Manish Gosala**  
Built as part of a self-initiated project to explore healthcare ML applications in a clean, offline notebook interface.

---

## 📌 Note

This project **does not use a website or Voila**. It runs completely inside **Jupyter Notebook**, making it beginner-friendly, offline, and focused purely on machine learning logic and interactivity.
