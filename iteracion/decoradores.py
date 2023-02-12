
def decorador(funcionComun):
  def funcionDecorada(*args, **kwargs):
    print('Mi primer decorador')
  return funcionDecorada

@decorador
def funcionComun():
  print('Mi funcion comun')

funcionComun()