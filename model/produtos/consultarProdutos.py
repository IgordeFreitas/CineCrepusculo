def consultarProdutos(dbconnection):
    cursor = dbconnection.cursor(dictionary=True)
    cursor.execute("SELECT id_produto, nome, preco FROM produto")
    Produtos = cursor.fetchall()
    cursor.close()
    return Produtos
    