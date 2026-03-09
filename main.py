#Importa a função responsavel por criar a conecxão com o banco
from sqlalchemy import create_engine

# Importar tipo de dados e estrutura das colunas
from sqlalchemy import Column, Integer, String, Float, Boolean

# Importar a classe Base usada para criar os modelos ORM
from sqlalchemy.orm import declarative_base

#Importa ferramenta para criar sessões de banco
from sqlalchemy.orm import sessionmaker

# Criar classe base do ORM
Base = declarative_base()

# classe = Tabela
# objeto = Linha tabela
# atributos = Coluna

#Classe Produto representando uma tabela no banco de dados
class Produto(Base):
    #Nome da tabela no banco
    __tablename__ = "produtos"

    #Coluna id
    # Integer > numero inteiro
    # Primary_key = True
    id = Column(Integer, primary_key=True)

    #Nome do Produto
    # String > Texto
    nome = Column(String(100))

    #Preço do Produto
    # float : Numero decimal
    preco = Column(Float)

    #Quantiidade em estoque
    estoque = Column(Integer)

    #Produto ativo ou não
    ativo = Column(Boolean)

    #Metodo construtor
    def __init__(self, nome, preco, estoque, ativo):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.ativo = ativo
    
    #Representação do objeto para imprimir
    def __repr__(self):
        return f"Produto(id = {self.id}, nome = {self.nome}, preco = {self.preco}, estoque = {self.estoque}, ativo = {self.ativo})"

#Criar a conexão com sqlite
# echo=True log do sql
engine = create_engine("sqlite:///estoque.db", echo=True)

#Criar as tabelas no banco se ainda não existirem
Base.metadata.create_all(engine)
