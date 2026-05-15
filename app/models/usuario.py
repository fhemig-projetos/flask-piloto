from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(255), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nome}>'