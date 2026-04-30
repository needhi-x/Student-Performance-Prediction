import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

df = pd.read_csv("data/student_data.csv")

X = df.drop("performance_score", axis=1)
print(X.columns)
y = df["performance_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------
# MODEL 1: Linear Regression
# -------------------------
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

# -------------------------
# MODEL 2: Random Forest
# -------------------------
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

# -------------------------
# EVALUATION
# -------------------------
print("\n📊 MODEL COMPARISON\n")

print("Linear Regression:")
print("MAE:", mean_absolute_error(y_test, lr_pred))
print("R2:", r2_score(y_test, lr_pred))

print("\nRandom Forest:")
print("MAE:", mean_absolute_error(y_test, rf_pred))
print("R2:", r2_score(y_test, rf_pred))

# Save best model
joblib.dump(rf, "models/model.pkl")

print("\n✅ Best model saved (Random Forest)")