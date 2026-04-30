import joblib
import numpy as np

model = joblib.load("models/model.pkl")

# sample student data
sample = np.array([[5, 80, 70, 7, 6]])

prediction = model.predict(sample)

print("🎯 Predicted Performance Score:", prediction[0])