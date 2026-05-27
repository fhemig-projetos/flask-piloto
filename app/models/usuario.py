from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    senha_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    @property
    def senha(self):
        raise AttributeError("A senha não é um atributo legível")

    @senha.setter
    def senha(self, valor):
        self.senha_hash = generate_password_hash(valor)
        
    def check_senha(self, valor):
        return check_password_hash(self.senha_hash, valor)

    def __repr__(self):
        return f'<Usuario {self.nome}>'