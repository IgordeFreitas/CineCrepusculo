def deletar(dbconnection, nome, endereco, email):
    sql = "DELETE FROM cliente(nome, endereco, email) values (%s, %s ,%s)"
    
    cursor = dbconnection. cursor(dictionary = True)
    cursor . execute(sql, (nome, endereco, email))
    cursor . fetchall()

    return cursor.rowcount