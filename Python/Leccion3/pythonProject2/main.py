# Ciclo While (Mientras o durante)
# contador = 0
# while contador < 3:
#     print('Ejecutamos nuestro ciclo While', contador)
#     contador += 1
# else:
#     print('Fin del ciclo While')

# Imprimir números del 0 al 5 con el ciclo While
# maximo = 5
# contador = 0
# while contador <= maximo:
#     print(contador)
#     contador += 1

# minimo = 1
# contador = 5
# while contador >= minimo:
#     print(contador)
#     contador -= 1

#Ciclo for (Para hasta con paso hacer)
# cadena = 'Hello'
# for letra in cadena:
#     print(letra)
# else:
#     print('Fin del ciclo For')

# Palabra reservada Break

# for letra in 'Alemania':
#     if letra == 'A':
#         print(f'Letra encontrada: {letra}')
#         break
# else:
#     print('Fin del ciclo for')

# Palabra reservada Continue
# for i in range(6):
#     if i % 2 == 0:
#         print(f'Valor: {i}')

# for i in range(6):
#     if i % 2 != 0:
#         continue
#     print(f'Valor: {i}')

# def es_bisiesto(año):
#     # Un año es bisiesto si es divisible por 4, excepto aquellos divisibles por 100,
#     # a menos que también sean divisibles por 400.
#     return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
#
# # Este bucle se ejecutará hasta que el usuario decida.
# while True:
#     año = int(input("Ingresa un año para saber si es bisiesto o no: "))
#     if es_bisiesto(año):
#         print(f"El año {año} es bisiesto.")
#     else:
#         print(f"El año {año} no es bisiesto.")
#
#     # Preguntamos al usuario si desea continuar
#     continuar = input("¿Quieres verificar otro año?: ")
#     if continuar.lower() != 'si':
#         break
#
# print("Programa finalizado.")

#Calcular la suma de N primeros numeros
# # Este programa calcula la suma de números enteros ingresados por el usuario
#
# # Pedimos al usuario que ingrese los números enteros separados por espacios
# numeros = input("Ingresa los números enteros separados por espacios: ")
#
# # Convertimos la cadena de entrada en una lista de enteros
# lista_numeros = [int(numero) for numero in numeros.split()]
#
# # Calculamos la suma de los números enteros
# suma_total = sum(lista_numeros)
#
# # Mostramos el resultado
# print(f"La suma de los números enteros es: {suma_total}")

# Ejercicio 3 Leer 10 números e imprimir cuántos son positivos, cuántos negativs y cuántos neutros

# Este programa lee 10 números enteros y cuenta cuántos son positivos, negativos y neutros

# Inicializamos los contadores para cada tipo de número
positivos = 0
negativos = 0
neutros = 0

# Pedimos al usuario que ingrese 10 números enteros
# print("Ingresa 10 números enteros, uno por uno:")
#
# # Utilizamos un bucle para leer los números y clasificarlos
# for i in range(10):
#     numero = int(input(f"Número {i+1}: "))
#     if numero > 0:
#         positivos += 1
#     elif numero < 0:
#         negativos += 1
#     else:
#         neutros += 1
#
# # Imprimimos los resultados
# print(f"Números positivos: {positivos}")
# print(f"Números negativos: {negativos}")
# print(f"Números neutros: {neutros}")

# Ejercicio 4: Suponga que se tiene un conjunto de calificaciones de un grupo de 10 alumnos. Realizar un algoritmo
# para calcular la calificación promedio y la calificación mas baja de todo el grupo.

# Inicializamos una lista para almacenar las calificaciones
#calificaciones = []

# Pedimos al usuario que ingrese las calificaciones de los 10 alumnos
# print("Ingresa las calificaciones de los 10 alumnos:")
#
# for i in range(10):
#     calificacion = float(input(f"Calificación del alumno {i+1}: "))
#     calificaciones.append(calificacion)
#
# # Calculamos la calificación promedio
# promedio = sum(calificaciones) / len(calificaciones)
#
# # Encontramos la calificación más baja
# calificacion_baja = min(calificaciones)
#
# # Imprimimos los resultados
# print(f"La calificación promedio es: {promedio}")
# print(f"La calificación más baja es: {calificacion_baja}")

# Ejercicio 5: calcular el factorial de un número entero mayor o igual a 0

# def factorial(n):
#     if n < 0:
#         return "El factorial no está definido para números negativos."
#     elif n == 0:
#         return 1
#     else:
#         resultado = 1
#         for i in range(1, n + 1):
#             resultado *= i
#         return resultado
#
# # Solicitamos al usuario que ingrese un número
# numero = int(input("Ingresa un número entero no negativo para calcular su factorial: "))
#
# # Calcular y mostrar el resultado
# print(f"El factorial de {numero} es {factorial(numero)}")

# Ejercicio 6: Ingresar N enteros, visualizar la suma de los números pares de la lista, cuántos números pares existen
# y cuál es el promedio de números impares

# def procesar_numeros(numeros):
#     suma_pares = 0
#     cantidad_pares = 0
#     suma_impares = 0
#     cantidad_impares = 0
#
#     # Procesar cada número en la lista
#     for num in numeros:
#         if num % 2 == 0:
#             suma_pares += num
#             cantidad_pares += 1
#         else:
#             suma_impares += num
#             cantidad_impares += 1
#
#     # Calcular el promedio de números impares
#     promedio_impares = suma_impares / cantidad_impares if cantidad_impares > 0 else 0
#
#     return suma_pares, cantidad_pares, suma_impares, cantidad_impares, promedio_impares
#
#
# # Solicitar al usuario la cantidad de números a ingresar
# n = int(input("¿Cuántos números deseas ingresar? "))
#
# # Solicitar al usuario que ingrese los números
# numeros = []
# for i in range(n):
#     numero = int(input(f"Ingrese el número {i + 1}: "))
#     numeros.append(numero)
#
# # Obtener los resultados
# suma_pares, cantidad_pares, suma_impares, cantidad_impares, promedio_impares = procesar_numeros(numeros)
#
# # Mostrar los resultados
# if cantidad_pares > 0:
#     print(f"Suma de los números pares: {suma_pares}")
#     print(f"Cantidad de números pares: {cantidad_pares}")
# else:
#     print("No se ingresaron números pares.")
#
# if cantidad_impares > 0:
#     print(f"Suma de los números impares: {suma_impares}")
#     print(f"Cantidad de números impares: {cantidad_impares}")
#     print(f"Promedio de los números impares: {promedio_impares}")
# else:
#     print("No se ingresaron números impares.")

# Ejercicio 7: Dadas las horas trabajadas de 5 personas y la tarifa de pago, calcular el salario y la sumatoria
# de todos los salarios

def calcular_salario(horas, tarifa):
    return horas * tarifa

def main():
    total_salarios = 0
    salarios = []

    for i in range(5):
        horas = float(input(f"Ingrese las horas trabajadas de la persona {i+1}: "))
        tarifa = float(input(f"Ingrese la tarifa de pago por hora: "))
        salario = calcular_salario(horas, tarifa)
        salarios.append(salario)
        total_salarios += salario
        print(f"El salario de la persona {i+1} es: {salario}")

    print(f"La sumatoria de todos los salarios es: {total_salarios}")

if __name__ == "__main__":
    main()















































