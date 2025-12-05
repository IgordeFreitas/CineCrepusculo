def consultarProdutos(dbconnection):
    cursor = dbconnection.cursor(dictionary=True)
    cursor.execute("SELECT id_cliente, nome FROM cliente")
    Produtos = cursor.fetchall()
    cursor.close()
    return Produtos
    