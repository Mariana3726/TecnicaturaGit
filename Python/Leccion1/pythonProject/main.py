'''
miVariable = 3
print(miVariable)
miVariable = "a"
print(miVariable)
miVariable = 3 + 3
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
#las literales se escriben x728
print(id(y))
print(id(z))

a = 10.99
print(type(a))

a = True
print(type(a))

# Tipos int,float,string,bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas

miGrupoFavorito = "The Letter Black"
caracteristicas = "Nightwish"
print("Mi grupo favorito es: ", miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))

# Tipos booleanos (bool)
miBooleano = 1 > 0
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar entrada del usuario
# funcion input
# resultado = input("Digite un numero: ")  # regresa un dato tipo string
# print(resultado)
# Conversion de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
'''
"""
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
#print("Resultado de la suma:",suma)
print(f"El resultado de la suma es: {suma}")

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")
multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la division es: {division}")
division = operandoA // operandoB
print(f"El resultado de la division (int) es: {division}")
modulo = operandoA % operandoB
print(f"El resultado de la division o residuo (modulo) es: {modulo}")
exponente = operandoA ** operandoB
print(f"El resultado del exponente es: {exponente}")
"""
'''''
alto = int(input('Proporciona el alto del rectangulo: '))
ancho = int(input('Proporciona el ancho del rectangulo: '))
area = alto * ancho
perimetro = (alto + ancho) * 2
print("Area: ", area)
print("Perimetro: ", perimetro)
'''''
'''''
miVariable3 = 10
print(miVariable3)

#Operadores de reasignación
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable3 * 3
miVariable3 *= 3
print(miVariable3)

# miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)

#Operadores de comparación
d = 4
b = 4
resultado = d == b
print(resultado)

#Operador diferente
resultado = d != b
print(resultado)

# Operador mayor que
resultado = d > b
print(resultado)

#Operador menor que
resultado = d < b
print(resultado)

#Operador menor o igual que
resultado = d <= b
print(resultado)

# Operador mayor o igual que
resultado = d >= b
print(resultado)
'''
''''
#Ejercicio

a = int(input("Digite un número: "))
print(f"El residuo de la división es: {a % 2}")
if a % 2 == 0:
    print(f"El valor de a es: {a} es un número PAR")
else:
    print(f"El valor de a es: {a} es un número IMPAR")
'''
''''
edadAdulto = 18
edadPersona = int(input("Digite su edad: "))
if edadPersona >= edadAdulto:
    print(f"Su edad es: {edadPersona} años, usted es mayor de edad")
else:
    print(f"Su edad es: {edadPersona} años, usted es menor de edad")
'''
''''
# Operadores Lógicos

a = False
b = False
resultado = a and b
print(resultado)

#Operador or
resultado = a or b
print(resultado)

#Operador not
resultado = not a
print(resultado)
'''
'''
#Ejercicio: Valor dentro de un rango
valor = int(input("Digite un número dentro del rango 0 a 5: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f'El valor {valor} está dentro del rango')
else:
    print(f'El valor {valor} no está dentro del rango')
'''
''''
#Ejercicio con el operador OR, NOT
vacaciones = False
diaDescanso = True
if not (vacaciones or diaDescanso):
    print('Tiene trabajo que hacer')
else:
    print('Puede asistir al juego')
'''
''''
#Ejercicio: rango entre 20 y 30 años
edad = int(input('Digite su edad: '))
#veinte = edad >= 20 and edad < 30
#print(veinte)
#treinta = edad >= 30 and edad < 40
#print(treinta)

#if veinte or treinta:
if (20 <= edad < 30) or (30 <= edad < 40): # Sintaxis simplificada del operador and
    print("Estas dentro del rango de los (20´0) a (30'0) años")

#    if veinte:
#        print("Estas dentro del rango de los (20'0) años")
#   elif treinta:
#        print("Estas dentro del rango de los (30'0) años")
#    else:
#        print("No estas dentro del rango")
else:
    print("No estas dentro del rango de los (20´0) a (30'0) años")
'''
''''
#Ejercicio: El mayor de dos números
numero1 = int(input('Digite el valor para el número1: '))
numero2 = int(input('Digite el valor para el número2: '))
if numero1 > numero2:
    print('El número 1 es mayor')
else:
    print('El número 2 es mayor')
'''
# Ejercicio: Tienda de libros
print('Digite los siguientes datos del libro')
nombre = input('Digite el nombre del libro: ')
id = int(input('Digite el ID del libro: '))
precio = float(input('Digite el precio del libro: '))
envioGratuito = input('Indicar si el envío es gratuito (True/False): ')
if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'El valor es incorrecto, debe escribir True/False'
print(f'''
        Nombre : {nombre}
        Id: {id}
        Precio: {precio}
        Envio Gratuito?: {envioGratuito}

''')










