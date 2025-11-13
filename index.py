from fastapi import FastAPI, Body
from controller.TestContoller import consultarClientes
app = FastAPI()

@app.get("/")
def inicio():
    return consultarClientes()