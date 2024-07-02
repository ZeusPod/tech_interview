from ..db import db


class Employes(db.Model):
    __tablename__ = 'employes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<Employes {self.name}>'
    

