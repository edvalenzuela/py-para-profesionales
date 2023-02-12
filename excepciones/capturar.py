
lista = [1, 2, 3]

try:
  print(lista[4])
except IndexError:
  print('Error: Error en el indice')
else:
  print('No hay ningun error')
finally:
  print('Se ejecuto el script correctamente')