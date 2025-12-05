from config.dbConfig import getconnection

def deletarProduto(id_produto, nome, preco):
    connection = None
    connection = getconnection()

    try:
        connection.start_transation()
        linhas_afetadas=deletarProduto(connection,
                id_produto,
                nome,
                preco)
        connection.commit()

    except Exception as e:
        print(f"erro:{e}")

    finally:
        if connection:
            connection.close()
