from app.models.employes_model import Employes
from app.utils.create_pdf import genearte_pdf


def generate_pdf_controller(id):
    data_employe = Employes.query.get(id)
    return genearte_pdf(data_employe)