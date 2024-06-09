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

def es_bisiesto(año):
    # Un año es bisiesto si es divisible por 4, excepto aquellos divisibles por 100,
    # a menos que también sean divisibles por 400.
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

# Este bucle se ejecutará hasta que el usuario decida.
while True:
    año = int(input("Ingresa un año para saber si es bisiesto o no: "))
    if es_bisiesto(año):
        print(f"El año {año} es bisiesto.")
    else:
        print(f"El año {año} no es bisiesto.")

    # Preguntamos al usuario si desea continuar
    continuar = input("¿Quieres verificar otro año?: ")
    if continuar.lower() != 'si':
        break

print("Programa finalizado.")




















