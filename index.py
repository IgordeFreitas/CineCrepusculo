from fastapi import FastAPI, Body
from controller.clientes.consultarClientes import selecionarClientes
from controller.produtos.consultarProduto import selecionarProdutos
from controller.produtos.cadastrarProduto import cadastrarProduto

app = FastAPI()

@app.get("/")
def inicio():
    return()

@app.get("/clientes")
def get_usuarios():
    return selecionarClientes()

@app.post("/clientes")
def cadastrar(
        nome: str = Body(embed = True),
        endereco:str = Body(embed = True),
        email:str = Body(embed = True)
):
    return

############################################################################################

@app.get("/clientes/{id_cliente}")
def getcliente(id_cliente):
    return ({"cliente_id": id_cliente})

@app.patch("clientes-/{id_cliente}")
def atualizar_cliente(
    id_cliente:int,
    nome: str=Body(embed=True),
    idade:int=Body(embed=True)
    ):
    return
@app.delete("/clientes")
def deletarcliente(id_cliente:str = Body(embed=True)):
    return({"ação":"deletar cliente", "cliente": id_cliente})
    
   
@app.post("/filmes")
def selecionarfilmes(
        nome:str = Body(embed=True),
        Genero:str = Body(embed=True),
        sinopse:str = Body(embed=True),
        duracao:str = Body(embed=True)
):
    return({"ação": "selecionar filmes", "nome": nome, "genero": Genero, "sinopse": sinopse })

##########################################################################################

@app.get("/filmes")
def getfilme():
    return ({"filme": "lista de filme"})

@app.delete("/filmes")
def deletarfilme (id_filme:str = Body(embed=True)):
    return({"ação": "deletar filme", "filme": id_filme})

@app.patch("/filmes/{id_filme}")
def atualizar_filme(
    id_filme: int,
    titulo:str= Body(embed=True),
    genero:str= Body(embed=True)
):
    
 ########################################################################################

@app.get("/produtos")
def getProdutos():
    return selecionarProdutos()

@app.get("/produtos/{id_produto}")
def getcliente(produto):
    return ({"produto": produto})

@app.post("/produtos")
def listadeprodutos(
        nome:str = Body(embed=True),
        preco:float = Body(embed=True)
):
    return cadastrarProduto(nome, preco)

@app.patch("/produtos/{id_produto}")
def atualizar_Produto(
    id_produto:int,
    nome:str=Body(embed=True),
    preco:float=Body(embed=True)
):
    return atualizar_Produto

@app.delete("/produtos")
def deletarfilme (id_produto:str = Body(embed=True)):
    return({"ação": "deletar produto", "produto": id_produto})
  
  
#@app.post ("/clientes")
@app.delete("/clientes")
def deletarcliente(id_cliente:str = Body(embed=True)):
    return({"ação":"deletar cliente", "cliente": id_cliente})
    
   
@app.post("/filmes")
def selecionarfilmes(
        nome:str = Body(embed=True)
    ):
    return

#@app.get ("/clientes")
#@app.patch("/clientes")
#@app.delete("/clientes")

#@app.post ("/filmes")
#@app.get ("/filmes")
#@app.patch ("/filmes")
#@app.delete("/filmes")

#@app.post("/produtos")
#@app.get("/produtos")
#@app.patch("/produtos")
#@app.delete("/produtos")

#@app.post("/salas")
#@app.get("/salas")
#@app.patch("/salas")
#@app.delete("/salas")

#@app.post("/sessoes")
#@app.get("/sessoes")
#@app.patch("/sessoes")
#@app.delete("/sessoes")

#@app.post("/pedidos")
#@app.get("/pedidos")
#@app.patch("/pedidos")
#@app.delete("/pedidos")