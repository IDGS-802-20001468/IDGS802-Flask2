def mostrarColores(banda1,banda2,banda3,rbt):
    color ={}
    cB1 = llenarValores(banda1, 1)
    cB2 = llenarValores(banda2, 1)
    cB3 = llenarValores(banda3, 1)
    cB4 = llenarValores(rbt, 1)

    color ={'b1': cB1,
          'b2': cB2,
          'b3':cB3,
          'b4': cB4
          }
    return color

def calcularValor(banda1,banda2,banda3,rbt, ope):
    num = int(llenarValores(banda1, 2) + llenarValores(banda2, 2))
    b3 = llenarValores(banda3, 3)
    b4 = llenarValores(rbt, 4)
    print(num)
    valor = num * b3
    mini = valor - (valor * b4)
    maxi = valor + (valor * b4)

    if ope == 1:
        return valor
    elif ope == 2: 
        return mini
    elif ope == 3:
        return maxi

def llenarValores(banda, ope):
    color= ''
    num = ''
    multi = 0
    tol = 0
        
    banda = str(banda)
    if banda == 'Negro':
        color = 'black'
        num = '0'
        multi = 1
    elif banda == 'Cafe':
        color = 'brown'
        num = '1'
        multi = 10
    elif banda == 'Rojo':
        color = 'red'
        num = '2'
        multi = 100
    elif banda == 'Naranja':
        color = 'orange'
        num = '3'
        multi = 1000
    elif banda == 'Amarillo':
        color = 'yellow'
        num = '4'
        multi = 10000
    elif banda == 'Verde':
        color = 'green'
        num = '5'
        multi = 100000
    elif banda == 'Azul':
        color = 'blue'
        num = '6'
        multi = 1000000
    elif banda == 'Violeta':
        color = 'purple'
        num = '7'
        multi = 10000000
    elif banda == 'Gris':
        color = 'grey'
        num = '8'
        multi = 100000000
    elif banda == 'Blanco':
        color = 'white'
        num = '9'
        multi = 1000000000
    elif banda == 'Oro':
        color = 'gold'
        tol = 0.05
    elif banda == 'Plata':
        color = 'silver'
        tol = 0.1

    if ope == 1:
         return color
    elif ope == 2:
        return num
    elif ope == 3:
        return multi
    elif ope == 4:
        return tol
        