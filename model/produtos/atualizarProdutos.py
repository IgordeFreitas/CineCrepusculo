def atualizar(dbconnection, nome, preco, id):
    sql = "UPDATE filme set nome = %s, preco = %s, where id_produto = %s"

    cursor = dbconnection.cursor(dictionary = True)
    cursor.exexcute(sql, (nome, preco,id))
    cursor.fetchall()

    return cursor.rowcount