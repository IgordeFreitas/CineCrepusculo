class clientes:
    def __init__(self,nome,idade,email):
      self.nome = nome
      self.idade = idade
      self.email = email 
    
    def getNome(self):
      return self.nome

    def SetNome(self,nome):
      self.nome = nome  

    def getIdade(self):
      return self.idade
    
    def setIdade(self,idade):
        self.idade = idade
    
    def getEmail(self):
      return self.email
    
    def setEmail(self,email):
       self.email = email