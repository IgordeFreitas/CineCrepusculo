def deletar (dbconnection, nome,preco):
    sql = "DELETE FROM cliente (nome, preco) values (%s, %s)"

    cursor = dbconnection . cursor(dictionary = True)
    cursor . execute(sql, (nome, preco))
    cursor . fetchall()

    return cursor . rowcount