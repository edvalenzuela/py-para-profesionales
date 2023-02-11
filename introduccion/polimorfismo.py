class Perro():
  def avanzar(self):
    print('Tengo 4 patas')
    
class Perico():
  def avanzar(self):
    print('Volar')
    
def mover(animal):
  animal.avanzar()
  

perro = Perro()
perro.avanzar()

perico = Perico()
perico.avanzar()

print('------')

mover(perro)
mover(perico)