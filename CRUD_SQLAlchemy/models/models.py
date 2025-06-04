'''Arquivo que contem as classes que representam as tabelas do banco de dados.'''
'''
- IENH - 2025/01
- Aluno/autor: Thomas Otsa Bender
'''

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

'''Classe que representa a tabela de usuarios no banco de dados.
   Atributos:
    id: inteiro que representa o id do usuario.
    nome: string que representa o nome do usuario.
    idade: inteiro que representa a idade do usuario.
'''

class Usuario(Base):

    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    idade = Column(Integer)

    def __repr__(self):
        return f"<Usuario(nome='{self.nome}', idade={self.idade})>"