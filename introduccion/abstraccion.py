class Lavadora():
  def __init__(self):
    pass

  def lavar(self, temp='caliente'):
    self._llenar_tanque(temp)
    self._anadir_jabon()
    self._lavar()
    self._centrifugar()

  def _llenar_tanque(self, temp):
    print(f'Llenando el tanque con agua {temp}')
    
  def _anadir_jabon(self):
    print('Anadiendo jabon')
    
  def _lavar(self):
    print('Lavando..')
    
  def _centrifugar(self):
    print('Centrifugando la ropa..')

if __name__ == '__main__':
  lavadora = Lavadora()
  lavadora.lavar()