from config.dbConfig import getConnection
from model.clientes.atualizarClientes import atualizar

def atualizarCliente(id_cliente, nome, endereco, email):
    Connection = None
    Connection = getConnection()

    try:

        Connection.start_transation()
        linhas_afetadas=atualizar(Connection,
                id_cliente, 
                nome, 
                endereco, 
                email)
        Connection.commit()

    except Exception as e:
        print(f"erro: {e}")
 
        Connection.rollback()

    finally:
        if Connection:
            Connection.close()