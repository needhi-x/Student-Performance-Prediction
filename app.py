import streamlit as st
import numpy as np
import joblib
from src.report import generate_report

model = joblib.load("models/model.pkl")

st.title("🎓 Student Performance Prediction System")

study_hours = st.slider("Study Hours", 0, 12, 5)
attendance = st.slider("Attendance (%)", 40, 100, 75)
previous_score = st.slider("Previous Score", 30, 100, 60)
sleep_hours = st.slider("Sleep Hours", 3, 10, 6)
assignments = st.slider("Assignments Completed", 0, 10, 5)

# -----------------------------
# SESSION STORAGE (IMPORTANT FIX)
# -----------------------------
if "score" not in st.session_state:
    st.session_state.score = None
    st.session_state.grade = None

# -----------------------------
# PREDICT BUTTON
# -----------------------------
if st.button("🎯 Predict Performance"):

    data = np.array([[
        study_hours,
        attendance,
        previous_score,
        sleep_hours,
        assignments
    ]])

    score = model.predict(data)[0]

    if score >= 75:
        grade = "A (Excellent)"
    elif score >= 60:
        grade = "B (Good)"
    elif score >= 40:
        grade = "C (Average)"
    else:
        grade = "D (Poor)"

    st.session_state.score = score
    st.session_state.grade = grade

    st.success(f"🎯 Score: {score:.2f}")
    st.info(f"📊 Grade: {grade}")

# -----------------------------
# PDF BUTTON (SEPARATE & SAFE)
# -----------------------------
if st.session_state.score is not None:

    if st.button("📄 Generate PDF Report"):

        generate_report(
            study_hours,
            attendance,
            previous_score,
            sleep_hours,
            assignments,
            st.session_state.score,
            st.session_state.grade
        )

        st.success("📄 PDF Generated Successfully!")

        with open("student_report.pdf", "rb") as f:
            st.download_button(
                label="⬇ Download Report",
                data=f,
                file_name="student_report.pdf",
                mime="application/pdf"
            )