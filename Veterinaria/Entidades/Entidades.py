class PracticaMedica:
    def __init__(self,Id,Descripcion):
        self._Id = Id      
        self._Descripcion = Descripcion



    def Id(self):
            return self._Id

 
    def Id(self, value):
            self._Id = value

 
    def Descripcion(self):
            return self._Descripcion

    def Descripcion(self, value):
            self._Descripcion = value

