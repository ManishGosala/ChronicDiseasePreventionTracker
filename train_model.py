import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# 📥 Load dataset
data = pd.read_csv("diabetes_binary_health_indicators_BRFSS2015.csv")

# 🧠 Feature engineering
data["lifestyle_score"] = data["PhysActivity"] + (1 - data["Smoker"])
data["diet_score"] = data["Fruits"] + data["Veggies"]

# 🎯 Select features and target
X = data[['HighBP', 'HighChol', 'BMI', 'Age', 'lifestyle_score', 'diet_score']]
y = data['Diabetes_binary']

# ✂️ Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🏗️ Train smaller model to reduce size
model = RandomForestClassifier(n_estimators=25, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# ✅ Print accuracy
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# 💾 Save with compression to reduce .pkl size
joblib.dump(model, "chronic_model.pkl", compress=3)
