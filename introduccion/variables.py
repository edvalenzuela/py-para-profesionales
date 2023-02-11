
class Persona():
  edad = 20 #Variable de clase
  def __init__(self, nombre, nacionalidad): #Variables de instancia
    self.nombre = nombre
    self.nacionalidad = nacionalidad
    
persona1 = Persona('Martin', 'Argentina')
print(persona1.nombre)
print(persona1.nacionalidad)