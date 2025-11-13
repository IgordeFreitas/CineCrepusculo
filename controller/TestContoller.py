from config.dbConfig import getConnection

def consultarClientes():
	connection = None
	try:
		connection = getConnection()
		cursor = connection.cursor(dictionary=True)
		cursor.execute("SELECT id_cliente, nome FROM cliente")
		cliente = cursor.fetchall()
		cursor.close()
		return cliente
	finally:
		if connection:
			connection.close()