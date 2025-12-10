from config.dbConfig import getConnection
from model.clientes import consultarClientes
def deletarFilme(id_filme, nome, genero, sinopse, duracao):
    connection = None
    connection = getConnection()

    try:
        connection.start_transation()
        linhas_afetadas=deletarFilme(connection,
                id_filme, 
                nome,
                genero,
                sinopse,
                duracao)
        connection.commit()

    except Exception as e:
        print(f"erro:{e}")

    finally:
        if connection:
            connection.close()