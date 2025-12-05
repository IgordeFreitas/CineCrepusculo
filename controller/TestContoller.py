from config.dbConfig import getConnection

def consultarClientes():
	connection = None
	connection = getConnection()
	try:
		cursor = connection.cursor(dictionary=True)
		cursor.execute("SELECT id_cliente, nome FROM cliente")
		cliente = cursor.fetchall()
		cursor.close()
		return cliente
	finally:
		if connection:
			connection.close()