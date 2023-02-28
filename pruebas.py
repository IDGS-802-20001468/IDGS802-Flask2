def crearDiccionario():
    f = open('diccionario.txt', 'r')
    contenido = f.read()
    f.close()
    lista = contenido.split(',')
    dicc = {}
    for item in lista:
        if(item != ''):
            key = item.split(' ')[0]
            value = item.split(' ')[1]
        dicc[(key)] = value
    return (dicc)

def escribirPalabra(pEsp, pIng):
    validacion = validarPalabras(crearDiccionario(), pEsp, pIng)
    if (validacion == 'validada'):
        f = open('diccionario.txt', 'a')
        f.write(pEsp+' '+pIng+',')
        f.close()
        return 'Palabra Guardada'
    else:
        return validacion

def buscarIng(diccionario, palabra):
    palabraL = palabra.lower()
    print(palabraL)
    for clave in diccionario.keys():
        print(clave)
        print(palabraL)
        if palabraL == clave.lower():
            valor = diccionario[clave]
            mensaje =  'La traduccion de '+ palabra + ' en Ingles es: '+ valor
            break
        else:
            mensaje = 'La palabra no se encuentra en el diccionario'
    return mensaje
        
        
def buscarEsp(diccionario, palabra):
    palabraL = palabra.lower()
    claveF = ''
    for clave, valor in diccionario.items():
        if palabraL == valor.lower():
            print(valor.lower())
            print(valor.lower())
            claveF = clave
            break
    if claveF != '':          
            return'La traduccion de '+ palabra+ ' en Español es: '+ clave
    else:
        return'La palabra no se encuentra en el diccionario'
    
def validarPalabras(diccionario, pEsp, pIng):

    if pEsp.lower() in  map(str.lower, diccionario.keys()):
        return 'La palabra '+ pEsp + ' ya está en las palabras en Español del diccionario.'
    if pIng.lower() in  map(str.lower, diccionario.values()):
        return 'La palabra '+ pIng+ ' ya está en las palabras en Ingles del diccionario.'
    return 'validada'

