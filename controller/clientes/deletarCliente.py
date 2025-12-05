from config.dbConfig import getConnection
from model.clientes import deletarClientes

def deletarCliente(id_cliente, nome, endereco, email):
    conecton = None
    connection = getConnection()

    try:
        connection.start_transation()
        linhas_afetadas=deletarClientes(connection,
                id_cliente,
                nome,
                endereco,
                email)
        connection.commit()

    except Exception as e:
        print(f"erro:{e}")

    finally:
        if connection:
            connection.close()