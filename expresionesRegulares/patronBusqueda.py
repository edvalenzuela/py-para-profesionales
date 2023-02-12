import re

mi_patron = re.compile('\d\d\d')
print(mi_patron.search('Ta122za').group())

if (re.search('\Aa[0-9].*(end|fin)$', 'a6 es una marca de fin')):
  print('Se encontro el patron...')