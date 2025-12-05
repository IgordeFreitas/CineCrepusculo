def cadastrar(DBconnection,nome, genero, sinopse, duracao):
    sql = "INSERT INTO produto (nome, genero, sinopse, duracao) VALUES (%s , %s, %s, %s)"

    cursor = DBconnection.cursor(dicionary = True)
    cursor.execute(sql, (nome, genero, sinopse, duracao))
    cursor.fetchall()

    return cursor.rowcount