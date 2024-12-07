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


class Mascotas:
       def __init__(self,DNIporietario_ma=None, raza_ma=None, Genero_ma=None, Peso_ma=None,  FechaNacimiento_ma=None, Nombre_ma=None, Especie_ma=None, Observacion_ma=None):
                self._IDNIporietario_ma = DNIporietario_ma      
                self._raza_ma = raza_ma
                self._Genero_ma = Genero_ma      
                self._Peso_ma = Peso_ma
                    
                self._FechaNacimiento_ma = FechaNacimiento_ma
                self._Nombre_ma = Nombre_ma      
                self._Especie_ma = Especie_ma
                self._Observacion_ma = Observacion_ma

       def getDNIporietario_ma(self):
                return self._IDNIporietario_ma

       def setDNIporietario_ma(self, value):
                self._IDNIporietario_ma = value

       def getRaza_ma(self):
                return self._raza_ma

       def setRaza_ma(self, value):
                self._raza_ma = value

       def getGenero_ma(self):
                return self._Genero_ma

       def setGenero_ma(self, value):
                self._Genero_ma = value

       def getPeso_ma(self):
                return self._Peso_ma

       def setPeso_ma(self, value):
                self._Peso_ma = value

      # def getEstado_ma(self):
               # return self._Estado_ma

       #def setEstado_ma(self, value):
                #self._Estado_ma = value

       def getFechaNacimiento_ma(self):
                return self._FechaNacimiento_ma

       def setFechaNacimiento_ma(self, value):
                self._FechaNacimiento_ma = value

       def getNombre_ma(self):
                return self._Nombre_ma

       def setNombre_ma(self, value):
                self._Nombre_ma = value

       def getEspecie_ma(self):
                return self._Especie_ma

       def setEspecie_ma(self, value):
                self._Especie_ma = value

       def getObservacion_ma(self):
                return self._Observacion_ma

       def setObservacion_ma(self, value):
                self._Observacion_ma = value

