
class Libro():
  def __init__(self, nombre, autor, paginas):
    self.nombre = nombre
    self.autor = autor
    self.paginas = paginas
  
  def __str__(self):
    return f'{self.nombre} escrito por {self.autor}'

  def __len__(self):
   return self.paginas
 
  def __del__(self):
   print('Se ha eliminado un libro...')
  
libro1 = Libro('Curso de py', 'brian', 110)
del libro1
