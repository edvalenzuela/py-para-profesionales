class Personal():
  def __init__(self, antiguedad, especialidad):
    self.especialidad = especialidad
    self.antiguedad = antiguedad
  
  def Sueldo(self):
    if self.especialidad == 'BF':
      return 10 * self.antiguedad
    return 15 * self.antiguedad
  
class Supervisor(Personal):
  def __init__(self, cargo):
    super().__init__(5, cargo)
  
class Operador(Personal):
  def __init__(self, cargo):
    super().__init__(2, cargo)

if __name__ == '__main__':
  personal1 = Personal(10, 'Jefe de Desarrollo')
  print(f'Sueldo del personal: {personal1.Sueldo()}')
  
  supervisor1 = Supervisor('BF')
  print(f'El sueldo del supervisor {supervisor1.Sueldo()}')
  
  operador1 = Operador('Programador')
  print(f'Sueldo del Operador: {operador1.Sueldo()}')
    