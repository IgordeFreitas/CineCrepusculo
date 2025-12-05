def consultarclientes(dbconnection):
    cursor = dbconnection.cursor(dictionary=True)
    cursor.execute("SELECT id_filme, nome FROM cliente")
    filmes =  cursor.fetchall()
    cursor.close()
    return filmes