#importa um 'pool' de conexões mysql, para atender mais de um client conectado ao mesmo tempo e gerenciá-los
import mysql.connector
from mysql.connector import pooling
#importa o .env dentro do arquivo
import os
from dotenv import load_dotenv

load_dotenv()

try:
	connectionPool = mysql.connector.pooling.MySQLConnectionPool(
		pool_name = "pool",
		pool_size = 5,
		pool_reset_session = True,
		host = os.getenv("DB_HOST"),
		user = os.getenv("DB_USER"),
		password = os.getenv("DB_PASSWORD"),
		database = os.getenv("DB_NAME")
	)
	print('Pool MySQL Criado!')

except mysql.connector.Error as err:
	print(f"Erro ao criar o pool de conexões: {err}")
	connectionPool = None


def getConnection():
	if connectionPool is None:
		raise Exception("Erro: o pool de conexões não foi iniciado!")
	return connectionPool.get_connection()