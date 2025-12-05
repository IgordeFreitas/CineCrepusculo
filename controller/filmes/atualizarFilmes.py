from config.dbConfig import getConnection
from model.filmes.atualizarFilmes import atualizar
def atualizarFilme(id_filme, nome, genero, sinopse, duracao):
    connection = None
    connection = getConnection()

    try:

        connection.start_tansaction()
        linhas_afetadas=atualizar(connection,
            nome, 
            genero, 
            sinopse, 
            duracao,          
            id_filme
        ) 
        connection.commit()                

    finally:
        if connection:
            connection.close()