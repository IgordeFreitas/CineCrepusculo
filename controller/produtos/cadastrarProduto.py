from config.dbConfig import getConnection
from model.produtos.cadastrarProdutos import cadastrar

def cadastrarProduto(nome, preco):
    connection = None
    connection = getConnection()
    try:
        linhas_afetadas = cadastrar(connection, nome, preco)
        connection.commit()

        return linhas_afetadas
    except:
        print('erro')
        connection.rollback()
    finally:
        connection.close()