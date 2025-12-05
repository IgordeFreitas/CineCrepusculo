def cadastrar(dbconection,nome,endereco,email):
    sql = "INSERT INTO cliente (nome, endereco, email) VALUES (%s, %s, %s)"

    Cursor = dbconection. cursor(dictionary = True)
    Cursor.execute(sql,(nome, endereco, email))
    Cursor.fetchall()

    return Cursor.rowcount