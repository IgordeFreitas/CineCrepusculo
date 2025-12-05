from config.dbConfig import getConnection
from model.filmes.consultarFilmes import consultarFilmes

def selecionarFilmes():
    connection = None
    connection = getConnection()

    try:
        Filmes = consultarFilmes(connection)
        return Filmes
    except Exception as error:
        print(f"Erro:{error}")
    finally:
        if connection:
            connection.close()    