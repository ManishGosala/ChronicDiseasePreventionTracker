from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib

# Sample data
data = pd.read_csv({
    "C:/Users/dhanasri/Downloads/health_metrics_50.csv"
})

X = data[['glucose', 'bp', 'bmi', 'age']]
y = data['risk']

model = RandomForestClassifier()
model.fit(X, y)
joblib.dump(model, 'chronic_model.pkl')
