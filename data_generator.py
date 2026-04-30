import pandas as pd
import numpy as np

np.random.seed(42)

n = 500  # more data = better model

df = pd.DataFrame({
    "study_hours": np.random.randint(0, 12, n),
    "attendance": np.random.randint(40, 100, n),
    "previous_score": np.random.randint(30, 100, n),
    "sleep_hours": np.random.randint(3, 10, n),
    "assignments_completed": np.random.randint(0, 10, n),
    "stress_level": np.random.randint(1, 10, n),
    "internet_access": np.random.randint(0, 2, n),  # 0/1
})

# realistic formula (adds noise like real life)
df["performance_score"] = (
    df["study_hours"] * 4.5 +
    df["attendance"] * 0.4 +
    df["previous_score"] * 0.5 +
    df["assignments_completed"] * 2 -
    df["stress_level"] * 1.5 +
    df["internet_access"] * 3 +
    np.random.normal(0, 5, n)
)

df.to_csv("data/student_data.csv", index=False)

print("✅ Advanced dataset created")