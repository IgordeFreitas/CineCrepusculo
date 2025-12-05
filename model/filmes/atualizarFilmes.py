def atualizar(dbconnection,nome, genero, sinopse, duracao, id):
    sql = "UPDATE filme set nome = %s,genero = %s, sinopse = %s, duracao = %s, WHERE id_filme = %s"

    cursor = dbconnection . cursor(dicitionary = True)
    cursor.execute(sql, (nome, genero, sinopse, duracao, id))
    cursor.fetchall()

    return cursor.rowcount

