from fpdf import FPDF

def generate_pdf_report(scores, feedback):
    """Generate a PDF report with scores and feedback."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add title
    pdf.cell(200, 10, txt="IELTS Speaking Test Report", ln=True, align="C")

    # Add scores
    pdf.cell(200, 10, txt="Scores:", ln=True)
    for category, score in scores.items():
        pdf.cell(200, 10, txt=f"{category}: {score}", ln=True)

    # Add feedback
    pdf.cell(200, 10, txt="Feedback:", ln=True)
    pdf.multi_cell(0, 10, txt=feedback)

    # Save the PDF
    pdf.output("ielts_report.pdf")
    return "ielts_report.pdf"