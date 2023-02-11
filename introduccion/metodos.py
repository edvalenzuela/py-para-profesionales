
#Metodos de instancia
class Persona():
  edad = 20
  def __init__(self, nombre, nacionalidad):
    self.nombre = nombre
    self.nacionalidad = nacionalidad
    
  def correr(self):
    print('Estoy corriendo ...')

#Metodos de clase
class Persona2():
  def __init__(self):
    pass
  
  def despedir(self):
    print('Te despido...')
  
  @classmethod
  def saludar(cls, nombre):
    print('Te saludo desde mi metodo de clase, mi nombre es', nombre)

#Metodos estaticos
class Persona3():
  def __init__(self):
    pass
  
  def saltar(self):
    print('Estoy saltando..')
  
  @classmethod
  def correr(cls):
    print('Estoy corriendo..')
  
  @staticmethod
  def nadar():
    print('Estoy nadando..')

pedro = Persona3()
pedro.nadar()


  