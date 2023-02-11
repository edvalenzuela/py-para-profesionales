
class Intro():
  pepe = 'hola'
  
  def __init__(self, valor):
    self.valor = valor
  
  def segundo(self):
    print('Segundo')
    
  def tercero(self):
    print('Tercero')
  
class Pepe():
  def saludar(self):
    print('Hola soy pepe')

dato = Intro('valor')
#print(dir(dato))

#print(isinstance(dato, Pepe))
print(hasattr(dato, 'pepe'))