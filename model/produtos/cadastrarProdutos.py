def cadastrar(DBConnection, nome, preco):
    sql = "INSERT INTO produto (nome, preco) VALUES (%s, %s)"

    cursor = DBConnection.cursor(dictionary = True)
    cursor.execute(sql, (nome, preco))
    cursor.fetchall()

    return cursor.rowCount