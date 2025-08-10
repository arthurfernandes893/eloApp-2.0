# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Gps(Base):
    __tablename__ = 'Gps' 

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_lider_gps = Column(String(50), nullable=False)

    membros = relationship("AcolhedorData", back_populates="gps")

    def __repr__(self):
        return f"<Gps(id={self.id}, name_lider_gps='{self.nome_lider_gps}')>"


class AcolhedorData(Base):
    __tablename__ = 'AcolhedorData'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    apelido = Column(String(50), nullable=True)
    email = Column(String(120), unique=True, nullable=False)
    celular = Column(String(30), unique=True,nullable=False)
    nome_lider_gps = Column(String(50), ForeignKey('Gps.nome_lider_gps'))

    gps = relationship("Gps", back_populates="membros")
    posts = relationship("Post", back_populates="owner")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.nome}', email='{self.email}')>"


class Evento(Base):
    __tablename__ = 'Evento'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)


class Adocao(Base):
    __tablename__ = "Adocao"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    idade = Column(Integer, nullable=False)
    celular = Column(String(30), unique=True,nullable=False)
    situacao = Column(Enum('Visitante', 'Conversao', 'Reconciliacao', name='situacao_enum'), nullable=False)
    data_decisao = Column(DateTime,nullable=False)
    data_carga = Column(DateTime, default=datetime.now)
    status_contato = Column(String(45), default='PENDENTE')
    observacoes = Column(String(256))
    nome_acolhedor =  Column(String(50), ForeignKey('AcolhedorData.nome'))
    HouM = Column(String(1), nullable=False)
    evento = Column(String(50), ForeignKey('Evento.nome'))