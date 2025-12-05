from config.dbConfig import getConnection
from model.produtos.consultarProdutos import consultarProdutos 
 
def selecionarProdutos():
    connection = None
    connection = getConnection()

    try:
        Produtos = consultarProdutos(connection)
        return Produtos
    except Exception as error:
        print(f"Erro:{error}")
    finally:
        if connection:
            connection.close()
   