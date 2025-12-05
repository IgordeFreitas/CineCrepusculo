def deletar (dbconnection, nome, genero, sinopse, duracao):
    sql = "DELETE FROM filmes(nome, genero, sinopse, duracao) values (%s, %s, %s,%s)"

    cursor = dbconnection . cursor(dictionary = True)
    cursor . execute(sql, (nome, genero, sinopse, duracao))
    cursor . fetchall()

    return cursor . rowcount