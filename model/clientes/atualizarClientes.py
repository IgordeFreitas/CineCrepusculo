def atualizar(dbconnection, nome, endereco, email, id):
    sql = "UPDATE cliente set nome = %s, endereco = %s, email = %s, where id_cliente = %s"
    
    cursor = dbconnection.cursor(dicitionary = True)
    cursor.execute(sql, (nome, endereco, email, id))
    cursor.fetchall()

    return cursor.rowcount