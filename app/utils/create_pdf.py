from flask import make_response
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
import io
import os    

def genearte_pdf(data_employe):
    buffer = io.BytesIO()

    # Configurar el estilo del documento
    styles = getSampleStyleSheet()
    style_heading = styles['Heading1']
    style_body = ParagraphStyle(
        'body',
        parent=styles['Normal'],
        spaceBefore=0.5*inch,
        spaceAfter=0.5*inch,
        fontSize=12,
        textColor='black',
    )

    # Crear un objeto canvas
    pdf = SimpleDocTemplate(buffer, pagesize=letter)
    content = []

    logo_path = os.path.join(os.getcwd(), 'app', 'static', 'img', 'bohiques.png')
    logo = Image(logo_path, width=2*inch, height=1*inch, hAlign='RIGHT')
    content.append(logo)

    # Añadir detalles del empleado al PDF
    content.append(Paragraph('Detalle de empleado', style_heading))
    content.append(Paragraph(f'________________________________________________', style_body))
    content.append(Paragraph(f'<b>Nombre:</b> {data_employe.name}', style_body))
    content.append(Paragraph(f'<b>Departamento</b> {data_employe.department}', style_body))
    content.append(Paragraph(f'<b>Email:</b> {data_employe.email}', style_body))
    content.append(Paragraph(f'________________________________________________', style_body))

    # Construir el PDF
    pdf.build(content)

    # Mover el buffer al inicio
    buffer.seek(0)

    # Crear respuesta con el PDF
    response = make_response(buffer.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename=employee_{id}.pdf'

    return response
