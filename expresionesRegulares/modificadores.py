import re 

reg = re.compile(r'ac', re.IGNORECASE)
print(reg.search('pedrocualquierAC'))