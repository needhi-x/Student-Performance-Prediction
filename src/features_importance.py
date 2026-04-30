import pandas as pd
import joblib
import matplotlib.pyplot as plt

model = joblib.load("models/model.pkl")

df = pd.read_csv("data/student_data.csv")

X = df.drop("performance_score", axis=1)

importance = model.feature_importances_

plt.barh(X.columns, importance)
plt.title("Feature Importance")
plt.xlabel("Importance Score")
plt.show()