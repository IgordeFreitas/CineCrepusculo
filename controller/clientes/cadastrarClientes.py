from model.clientes import consultarClientes
from config.dbConfig import getConnection

def getclientes(id_clientes, nome, endereco, email):
    connection = None
    connection = getConnection()
    try:
        connection.start_transation()
        clientes=consultarClientes(connection,
                 id_clientes,
                 nome,
                 endereco,
                 email)
        connection.commit()

        return clientes
    except Exception as e:
        print(f"erro:{e}")
        
    finally:
        if connection:
            connection.close()
