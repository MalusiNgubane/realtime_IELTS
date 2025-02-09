from fpdf import FPDF

def generate_pdf_report(scores, feedback):
    """
    Generate a PDF report with progress data.
    Args:
        scores (list): List of dictionaries containing scores.
        feedback (str): Overall feedback.
    Returns:
        str: Path to the generated PDF file.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add a title
    pdf.cell(200, 10, txt="IELTS Speaking Test Progress Report", ln=True, align="C")

    # Add scores
    pdf.cell(200, 10, txt="Scores:", ln=True)
    for i, score in enumerate(scores):
        pdf.cell(200, 10, txt=f"Session {i + 1}: Grammar={score['Grammar']}, Vocabulary={score['Vocabulary']}, Fluency={score['Fluency']}", ln=True)

    # Add feedback
    pdf.cell(200, 10, txt="Overall Feedback:", ln=True)
    pdf.multi_cell(0, 10, txt=feedback)

    # Save the PDF
    report_path = "ielts_progress_report.pdf"
    pdf.output(report_path)
    return report_path