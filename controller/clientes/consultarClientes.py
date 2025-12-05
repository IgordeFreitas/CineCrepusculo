from config.dbConfig import getConnection
from model.clientes.consultarClientes import consultarClientes

def selecionarClientes():
    connection = None
    connection = getConnection()

    try:
        clientes = consultarClientes(connection)
        return clientes
    except Exception as error:
        print(f"Erro: {error}")
    finally:
        if connection:
            connection.close()