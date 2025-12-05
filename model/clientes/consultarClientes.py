def consultarClientes(dbconnection):
    cursor = dbconnection.cursor(dictionary=True)
    cursor.execute("SELECT id_cliente, nome FROM cliente")
    clientes = cursor.fetchall()
    cursor.close()
    return clientes