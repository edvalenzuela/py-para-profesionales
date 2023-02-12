import gzip

# lectura binaria
with open('doc.txt', 'rb') as file:
  with gzip.open('fichero.txt.gz', 'wb') as fichero:
    fichero.writelines(file)