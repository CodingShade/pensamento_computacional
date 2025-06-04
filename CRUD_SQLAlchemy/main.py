from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.models import Usuario

Base = declarative_base()

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

# Criar uma sessão
Session = sessionmaker(bind=engine)
session = Session()

def criar_usuario(nome: str, idade: int) -> Usuario:
    novo_usuario = Usuario(nome=nome, idade=idade)
    session.add(novo_usuario)
    session.commit()
    return novo_usuario

def buscar_todos_usuarios() -> list[Usuario]:
    try:
        usuarios = session.query(Usuario).all()
    except Exception as e:
        print(e)
        usuarios = []
    return usuarios

def buscar_usuarios_por_nome() -> list[Usuario]:
    try:
        usuarios = session.query(Usuario).filter_by(nome=nome).all()
    except Exception as e:
        print(e)
        usuarios = []
    return usuarios


if __name__ == "__main__":
    print("meu primeiro banco de dados com SQLAlchemy")
    novo_usuario = criar_usuario(nome="João", idade=30)
    print(novo_usuario)

    # Buscar todos os usuários e imprimir
    for usuario in buscar_todos_usuarios():
        print(usuario)