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

# Criar uma fabrica de sessões conectadas ao banco
Session = sessionmaker(bind=engine)

# Sessão ativo - pense nela como um carrinho de compras
session = Session()

#Criar objetos produtos
produto1 = Produto("Notebook", 5500, 6, True)
produto2 = Produto("Teclado", 500, 100, True)

#Adicionar os produtos no carrinho
#session.add(produto1)
#session.add(produto2)

# Confirmar a inserção no banco
#Salvar no banco de dados
#session.commit()


# Listar
#Busca todos os produtos do banco
produtos = session.query(Produto).all()

print(produtos)

for p in produtos:
    print(f"id={p.id}, nome{p.nome}, preco{p.preco}, estoque{p.estoque}, ativo{p.ativo}")


# UPDATE (Atualizar)

#Buscar o produto com id = 1
produto_id = session.query(Produto).filter(Produto.id == 1).first()
print(produto_id)

produto_estoque = session.query(Produto).filter(Produto.estoque >= 10).all()
for produto in produto_estoque:
    print(produto.estoque)



produto_id2 = session.query(Produto).filter_by(id=1).first()
print(produto_id2)

# Podemos usar order by
produtos_organizados = session.query(Produto).order_by(Produto.estoque).all()
produtos_oranizados2 = session.query(Produto).order_by(Produto.estoque.desc()).all()
for produto in produtos_organizados:
    print(f"Nome: {produto.nome}, Qtd_estoque: {produto.estoque}")

#Limitar a quantidade de resultado - Top 5 produtos mais caros
produtos_mais_caros = session.query(Produto).order_by(Produto.preco.desc()).limit(3).all()
for produto in produtos_mais_caros:
    print(f"Nome: {produto.nome}, Valor: {produto.preco}")





# Update - atualizar
#Busquei o produto para atualizar
notebook = session.query(Produto).filter_by(id = 1).first()
notebook.preco = 6000

#Confirmar essa autoreção
session.commit()
print("Preço atualizado com sucesso")

produtos = session.query(Produto).all()


for p in produtos:
    print(f"id={p.id}, nome{p.nome}, preco{p.preco}, estoque{p.estoque}, ativo{p.ativo}")
    