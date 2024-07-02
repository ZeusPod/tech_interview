from app.controllers.employe_controller import generate_pdf_controller
from app.models.employes_model import Employes
from flask import Blueprint, make_response, request
from app.utils.create_pdf import genearte_pdf


bp_employes = Blueprint('employes', __name__)

@bp_employes.route('/generate_pdf/<int:id>', methods=['GET'])
def generate_pdf(id):
    if request.method == 'GET':
       return generate_pdf_controller(id) 