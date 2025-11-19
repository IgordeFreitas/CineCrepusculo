class sessao:
    def __init__(self,filme,data_hora,sala):
        self.filme = filme
        self.data_hora = data_hora
        self.sala = sala
        
    def get(self):
           return self.filme

    def set(self,filme):
      self.filme = filme
           
    def getDataHora(self):
      return self.data_hora
    
    def setData_Hora(self,data_hora):
        return self.data_hora
    
   