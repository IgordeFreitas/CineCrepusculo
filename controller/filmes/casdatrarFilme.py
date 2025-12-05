from config.dbConfig import getConnection
from model.filmes.cadastarFilmes import cadastrar

def cadastrarfilme(nome, genero, sinopse, duracao):
    conection = None
    conection = getConnection()

    try:
        linhas_afetadas = cadastrar(conection, nome, genero, sinopse, duracao)
        conection.commit()

        return linhas_afetadas
    
    except:
        print('erro')
        conection.rollback
    finally:
        conection.close()    



