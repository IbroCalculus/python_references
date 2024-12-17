from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

def create_certificate(output_path, name, course_name, date):
    # Create a canvas in landscape mode
    c = canvas.Canvas(output_path, pagesize=landscape(A4))

    # Set text color to black
    c.setFillColor(colors.black)

    # Draw a border
    c.setStrokeColor(colors.black)
    c.setLineWidth(4)
    c.rect(1 * cm, 1 * cm, A4[1] - 2 * cm, A4[0] - 2 * cm)  # Swapped width and height for landscape

    # Title: Certificate of Completion
    c.setFont("Helvetica-Bold", 30)
    c.drawCentredString(A4[1] / 2, A4[0] - 4 * cm, "Certificate of Completion")  # Swapped width and height

    # Subtitle: Presented to
    c.setFont("Helvetica", 18)
    c.drawCentredString(A4[1] / 2, A4[0] - 6 * cm, "Presented to")

    # Recipient's name
    c.setFont("Helvetica-Bold", 26)
    c.drawCentredString(A4[1] / 2, A4[0] - 8 * cm, name)

    # Course details
    c.setFont("Helvetica", 18)
    c.drawCentredString(A4[1] / 2, A4[0] - 10 * cm, f"For successfully completing the {course_name}")

    # Date of completion
    c.setFont("Helvetica", 14)
    c.drawCentredString(A4[1] / 2, A4[0] - 12 * cm, f"Date: {date}")

    # Signature
    c.setFont("Helvetica", 12)
    c.drawString(2 * cm, 2 * cm, "Signature:")
    c.line(4 * cm, 2 * cm, 10 * cm, 2 * cm)

    # Issue Authority (optional)
    c.drawString(12 * cm, 2 * cm, "Authorized by:")
    c.line(15 * cm, 2 * cm, 19 * cm, 2 * cm)

    # Save the PDF
    c.save()

# Generate a sample certificate in landscape
create_certificate("certificate_landscape.pdf", "John Doe", "Python Programming Course", "September 12, 2024")
