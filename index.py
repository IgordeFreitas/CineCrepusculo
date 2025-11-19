from fastapi import FastAPI, Body
from controller.TestContoller import consultarClientes
app = FastAPI()

@app.get("/")
def inicio():
    return consultarClientes()

@app.get("/clientes")
def get_usuarios():
    return consultarClientes()

@app.post("/clientes")
def cadastrar(
        nome: str = Body(embed = True),
        endereco:str = Body(embed = True),
        email:str = Body(embed = True)
):
    return

@app.get("/clientes/{id_cliente}")
def getcliente(id_cliente):
    return ({"cliente_id": id_cliente})

@app.delete("/clientes")
def deletarcliente(id_cliente:str = Body(embed=True)):
    return({"ação":"deletar cliente", "cliente": id_cliente})
    
   
@app.post("/filmes")
def todososfilmes(
        nome:str = Body(embed=True),
        Genero:str = Body(embed=True),
        sinopse:str = Body(embed=True),
        duracao:str = Body(embed=True)
):
    return

@app.get("/filmes")
def getfilme():
    return ({"filme": "lista de filme"})

@app.delete("/filmes")
def deletarfilme (id_filme:str = Body(embed=True)):
    return({"ação": "deletar produto", "produto": id_filme})
        

