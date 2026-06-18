from datetime import date
from typing import Optional
from app.extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class DadoFuncional(db.Model):
    __tablename__ = 'dados_funcionais'

    # CHAVE PRIMÁRIA COMPOSTA (MASP + Nº Admissão)
    masp: Mapped[int] = mapped_column(primary_key=True)
    num_admissao: Mapped[int] = mapped_column(primary_key=True)

    # Identificadores e Referências
    nome_servidor: Mapped[str] = mapped_column(String(150))
    
    # Datas tratadas nativamente (Data Completa = Nascimento)
    data_nascimento: Mapped[Optional[date]] = mapped_column()
    data_inicio_exercicio: Mapped[Optional[date]] = mapped_column()
    
    # Códigos auxiliares
    cod_idade: Mapped[Optional[int]] = mapped_column()
    cod_sexo: Mapped[Optional[str]] = mapped_column(String(10))
    cod_carreira: Mapped[Optional[str]] = mapped_column(String(50))
    
    # Situações cadastrais
    situacao_funcional: Mapped[Optional[str]] = mapped_column(String(100))
    situacao_servidor: Mapped[Optional[str]] = mapped_column(String(100))

    def __repr__(self):
        return f'<DadoFuncional MASP={self.masp}/Adm={self.num_admissao} - {self.nome_servidor}>'