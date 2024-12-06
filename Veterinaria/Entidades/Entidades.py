class PracticaMedica:
    def __init__(self,Id=None, Descripcion=None):
        self._Id = Id      
        self._Descripcion = Descripcion



    def getId(self):
            return self._Id

 
    def setId(self, value):
            self._Id = value

 
    def getDescripcion(self):
            return self._Descripcion

    def setDescripcion(self, value):
            self._Descripcion = value

