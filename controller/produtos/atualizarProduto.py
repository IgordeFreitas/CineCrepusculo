from config.dbConfig import getConnection
from model.filmes.cadastarFilmes import cadastrar

def atualizarProduto(id_produto, nome, preco):
    connection = None 
    connection = getConnection()

    try: 
        connection.start_transaction()
        linhas_afetadas=cadastrar(connection,
            id_produto,
            nome,
            preco)
        connection.commit()

    finally:
        if connection:
            connection.close()
    