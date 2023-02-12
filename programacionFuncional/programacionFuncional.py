
def lower(elementos): 
  return elementos.lower()

lista = ['MARIA', 'JUAn', 'Si']
print(list(map(lower, lista)))

print([i.lower() for i in lista])

def saludar(idioma):
  def saludar_es():
    print('Hola')
  def saludar_en():
    print('Hi')
  func_idioma={
    'es': saludar_es,
    'en': saludar_en
  }
  return func_idioma[idioma]

el_saludo = saludar('en')
el_saludo()