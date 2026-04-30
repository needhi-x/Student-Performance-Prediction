from fpdf import FPDF

def generate_report(study_hours, attendance, previous_score, sleep_hours, assignments, score, grade):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Student Performance Report", ln=True, align='C')

    pdf.cell(200, 10, txt=f"Study Hours: {study_hours}", ln=True)
    pdf.cell(200, 10, txt=f"Attendance: {attendance}", ln=True)
    pdf.cell(200, 10, txt=f"Previous Score: {previous_score}", ln=True)
    pdf.cell(200, 10, txt=f"Sleep Hours: {sleep_hours}", ln=True)
    pdf.cell(200, 10, txt=f"Assignments: {assignments}", ln=True)

    pdf.cell(200, 10, txt=f"Predicted Score: {score:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Grade: {grade}", ln=True)

    pdf.output("student_report.pdf")