from utfs import db, login_manager
from flask_login import UserMixin
from datetime import datetime



@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key = True)
    nome_usuario = db.Column(db.String, nullable = False, unique = True)
    email = db.Column(db.String, nullable = False, unique = True)
    senha = db.Column(db.String, nullable = False)
    bio = db.Column(db.String(150))
    fotos = db.relationship("Foto", backref="usuario", lazy= True)
    idioma = db.Column(db.String, default="pt-br")
    privacidade = db.Column(db.String, default="publico")
    genero = db.Column(db.String, nullable=True, default="nao informado")


class Foto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    imagem = db.Column(db.String, default="default.png")
    data_criacao = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable = False) 
