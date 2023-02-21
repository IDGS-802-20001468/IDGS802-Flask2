'''
f = open('alumnos.txt', 'r')
#nombres = f.read()
#print(nombres)
nombres2 = f.readlines()
print(nombres2)
f.close()

for items in nombres2:
    #items.replace('/n', '')
    print(items,end='')
'''
alumno = {'Matricula': 12345, 
          'Nombre': 'Mario',
          'Apellidos': 'Lopez',
          'Correo': 'marioL@gmail.com'
          }
f = open('alumnos.txt', 'a')
for item in alumno:
    f.write(item.)

#f.write('\n'+'Mario')
#f.write('\n'+'Pedro')
f.close()