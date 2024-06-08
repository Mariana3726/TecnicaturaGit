 #DEfinimos las estaciones del año

#estaciones = {
#   "Verano": [1, 2, 3],
 #   "Otoño": [4, 5, 6],
  #  "Invierno": [7, 8, 9],
   # "Primavera": [10, 11, 12]
#}
# Le pedimos al usuario que ingrese un mes del año
#mes = int(input("Por favor, ingresa un mes del año (1-12): "))

# Inicializamos la variable estación con None
#estacion = None

# Recorremos las estaciones para encontrar a cuál corresponde el mes ingresado
#for e in estaciones:
 #   if mes in estaciones[e]:
  #      estacion = e
   #     break

# Si encontramos una estación, la imprimimos
#if estacion is not None:
 #   print(f"El mes {mes} corresponde a la estación {estacion}.")
#else:
 #   print("El número ingresado no corresponde a un mes válido.")

#Ejercicio 4

#calificacion = float(input("Ingrese su calificación (1-10): "))

#
#if 9 <= calificacion <= 10:
#    letra_calificacion = 'A'
#elif 8 <= calificacion < 9:
#    letra_calificacion = 'B'
#elif 7 <= calificacion < 8:
#    letra_calificacion = 'C'
#elif 6 <= calificacion < 7:
#    letra_calificacion = 'D'
#elif 0 <= calificacion < 6:
 #   letra_calificacion = 'F'
#else:
#    print("Valor ingresado incorrecto.")

#if letra_calificacion is not None:
#    print(f"Su calificación es: {letra_calificacion}")

#Ejercicio 5
''''

edad = int(input("Ingrese su edad: "))
mensaje = None

if 0 <= edad <= 10:
    mensaje = "La infancia es increíble y bella."
elif 11 <= edad <= 19:
    mensaje = "Tienes muchos cambios, mucho que estudiar."
elif 20 <= edad <= 29:
    mensaje = "Amor y comienza el trabajo."
elif 30 <= edad <= 39:
    mensaje = "Tiempo de consolidar tu vida."
elif 40 <= edad <= 49:
    mensaje = "Madurez y responsabilidades plenas."
elif 50 <= edad <= 59:
    mensaje = "La sabiduría se refleja en cada decisión."
elif 60 <= edad <= 69:
    mensaje = "Una nueva aventura comienza con la jubilación."
elif 70 <= edad <= 79:
    mensaje = "Tiempo de disfrutar los frutos del trabajo."
elif 80 <= edad <= 89:
    mensaje = "Cada día es un regalo lleno de recuerdos."
elif 90 <= edad <= 99:
    mensaje = "Las historias y experiencias son tesoros para compartir."
elif 100 <= edad <= 110:
    mensaje = "Más de un siglo de vida, un siglo de sabiduría."
else:
    mensaje = "Edad fuera de rango. Por favor, ingrese una edad entre 0 y 110."

if mensaje is not None:
    print(mensaje)
'''

# En esta clase veremos la sentencia IF/ELSE
'''condicion = 10
if condicion == True:
    print('Condición Verdadera')
elif condicion == False:
    print('Condición Falsa')
else:
    print('Condición sin especificar')
'''
# num = int(input('Digite un número en el rango del 1 al 3: '))
# numTexto = ''
# if num == 1:
#     numTexto = 'Número uno'
# elif num == 2:
#     numTexto = 'Número dos'
# elif num == 3:
#     numTexto = 'Número tres'
# else:
#     numTexto = 'Has ingresado un número fuera de rango'
# print(f'El número ingresado es: {num} - {numTexto}')

condicion = False
# if condicion:
#     print('Condición verdadera')
# else:
#     print('Condición falsa')

print('Condición Verdadera') if condicion else print('Condición Falsa')













