from flask import Flask
from .db import init_db
import os
from dotenv import load_dotenv
from app.routes import employes_routes

def create_app():

    load_dotenv()

    app = Flask(__name__)
    app.secret_key = "jekxlkalko_'009pñ,__.."

    # Obtener variables de entorno
    username = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    db_host = os.getenv("DB_HOST")
    print(username, db_password)
    # Asegurarse de que las variables de entorno existen
    if not all([username, db_password, db_name, db_host]):
        raise ValueError("Faltan una o más variables de entorno para la configuración de la base de datos")

    # Configurar la URI de SQLAlchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql://{username}:{db_password}@{db_host}/{db_name}"
    )

    # Inicializar la base de datos
    init_db(app)

    app.register_blueprint(employes_routes.bp_employes)

    return app
