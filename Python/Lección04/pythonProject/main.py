# LISTAS: las listas son un conjunto de elementos a los cuales se les asigna un índice. Las listas son
# modificables o mutables.
# Dentro de una misma lista, puede haber diferentes tipo de datos.Por ejemplo:
# lista = Ariel(0), Natalia(1), Liliana(2), Osvaldo(3) (en este caso,tipo string)
# Con las listas podemos usar tres funciones: append, insert y remove. También pop,clear y delete.
# Las listas se conocen en otros lenguajes como arreglos o vectores


nombres = ['Natalia', 'Osvaldo', 'Liliana', 'Ariel']
print(nombres)
print(nombres[2])
print(nombres[0])

#Si la lista es muy larga y queremos ver el último elemento
print(nombres[-1])
#Para mostrar el penúltimo
print(nombres[-2])

#Para recorrer las posiciones
print(nombres[0:2]) #recorre desde la posición indicada hasta anterior de la que pusimos

#Para ir del inicio de la lista al índice (sin incluirlo)
print(nombres[ :3])

#Desde el índice indicado hasta el final
print(nombres[1: ])

#Modificamos un valor
nombres[2] = 'Lily'
nombres[0] = 'Nati'
print(nombres)

#Iterar (repetir una acción varias veces) una lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# Ahora preguntamos cuántos elementos tiene una lista, con la función len
print(len(nombres)) #le pasamos como parámetro la lista

#Ahora agregamos un elemento
nombres.append('Marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)

#Ahora insertamos un elemento en un índice específico
nombres.insert(1, 'Alberto')
print(nombres)

nombres.insert(0, 'Mariana')
print(nombres)

#Ahora eliminamos un elemento de la lista

nombres.remove('Lily')
print(nombres)

#Eliminamos el último elemento de la lista, no el último ingresado
nombres.pop()
print(nombres)

#Ahora si eliminamos un índice específico
del nombres[2] #del significa delete (eliminar)
print((nombres))

#Eliminar, borrar o limpiar todos los elementos de la lista
nombres.clear()
print(nombres)

#Eliminar la lista
# del nombres
# print(nombres) #nos va a mostrar error porque ya la eliminamos

#Ejercicio 1: iterar un rango de 0 a 10 e imprimir números divisibles entre 3
#Ejemplo de ejecución 0,3,6,9

print('Rango de 0 a 10 con números divisibles entre 3')
for i in range(11):
    if i % 3 == 0:
        print(i)

#Ejercicio 2: crear un rango de números de 2 a 6
#Ejemplo de ejecución: 2,3,4,5,6

print('Rango con valores de inicio = 2 y fin = 6')
rango = range(2, 7)
for i in rango:
    print(i)

#Ejercicio 3: crear un rango de 3 a 10 pero con incremento de 2 en 2,
#en lugar de 1 en 1
#Ejemplo de ejecución: 3,5,7,9

print('Rango con valores de inicio = 3, fin = 10, incremento = 2')
for i in range(3, 11, 2):
    print(i)

# TUPLAS: a diferencia de las listas, no se pueden modificar.

cocina = ('cuchara', 'cuchillo', 'tenedor')
print(cocina)
print(len(cocina))#para contar los elementos de la tupla

# Acceder a un elemento, para eso utilizamos corchetes no paréntesis
print(cocina[0])

# Mostrar la manera inversa
print(cocina[-1])

# Como acceder a un rango
print(cocina[0:2]) #llega a 0 y 1, no llega al elemento 2
#Ejemplo
verduras = ('papa') #si no ponemos la coma,pasa a ser un tipo string,cadena.Hay que poner al menos un elemento con coma.

#Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar, end=' ') #Print usa \n para saltos de línea. Usamos end=' 'para eliminar los saltos de línea

#Hacemos una modificación en la tupla(hacemos conversión de tupla a lista y luego de lista a tupla)

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n' ,cocina)

#En las tuplas NO se pueden usar las funciones insert, append y remove

#Eliminamos tupla
#del cocina
#print(cocina)

#Tipo set
planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas)) #Usamos la función len = lenght significa largo

#Revisar si un elemento existe dentro del set
print('Marte' in planetas)

#Agregar un elemento
planetas.add('Tierra') #función add para agregar
print(planetas)

#Eliminar elementos (puede arrojar un error si el elemento no existe)
planetas.remove('Júpiter') #Esta función marca error si el elemento no está bien escrito
print(planetas)
planetas.discard('Tierra') #En esta función si no está bien escrito, directamente no borra nada
print(planetas)

#Limpiar set o conjunto
planetas.clear()
print(planetas)

#Eliminar set o conjunto
del planetas
#print(planetas)

# "Maradona" : 10 Un diccionario esta compuesto por dos elementos
# Una llave y un valor
# dict(key,value)
diccionario = {
    'IDE' : 'Integrated Development Enviroment' ,
    'POO' : 'Programación Orientada a Objetos' ,
    'SABD' : 'Sistema de Administración de Base de Datos'
}
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave (key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento Get = obtener
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# modificamos elementos
diccionario['IDE'] = 'Entorno de desarrollo integrado'
print(diccionario)

# Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7, 8, 9, 1]) #extend para agregar elementos a una lista
print(lista3)

print(lista3.index(3)) # Index: para saber en que indice esta ubicado el elemento
#print(lista3.index(0))

# Cómo saber cuántos valores repetidos hay dentro de una lista
print(lista3.count(1)) # cuenta cuántos valores iguales hay dentro de la lista

# Para poner la lista al reves
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Métodos de ordenamiento
lista3.sort() # ordena ascendentemente los elementos
print(lista3)
lista3.sort(reverse=True) #ordena descendentemente
print(lista3)

# Repaso de tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4,'Hola') #Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) # Acción boolenana, su respuesta es de tipo booleana
# Lo que no podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir lista a tupla y de tupla a lista

# Repaso de set o conjunto
# para definir un conjunto
conjunto2= set()
conjunto1 ={'chau'}
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add('Hola')
print(conjunto1)
print(3 not in conjunto1) #preguntamos si el numero 3 no esta en el conjunto 1, devuelve un valor booleano

# Cómo hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2)#Nos devuelve como repsuesta un valor booleano

#Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 #La línea es la que une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 #qué elemento tienen en común los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 #Asigna el valor que está en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1 #Asigna el valor que está en el conjunto2 y no en el conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 #Son los elementos que no comparten oson diferentes entre ambos
print(conjunto3)

#preguntamos si un conjunto es un subconjunto de otro
conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3))
print(conjunto2.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) #Preguntamos si los elementos del conjunto1 están dentro del 3
print(conjunto3.issuperset(conjunto2)) #Si el verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

#Cómo saber si ambos conjuntos son disconexos, que no comparten un elemento en común
print(conjunto1.isdisjoint(conjunto2))#False, si hay cosas en común

#Convertir un conjunto totalmente en inmutable(no se puede agregar ni modificar,ni eliminar elemntos del conj)
conjunto1 = frozenset

# Repaso diccionarios(los diccionarios aceptan cualquier tipo de dato:cadenas,enteros,reales,listas,tuplas,otros diccionarios)

diccionarioNuevo = {'Azul' : 'Blue', 'Rojo' : 'Red', 'Verde' : 'Green', 'Amarillo' : 'Yellow'}
print(diccionarioNuevo)
#Cómo eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

diccionario2 = {'Ariel' : {'edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)

#Ejercicio con diccionario

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.60, 'Precio': '50 millones', 'Posicion': 'extremo derecho'},
    11: {'Nombre': 'Angel di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 millones', 'Posicion': 'extremo derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 millones', 'Posicion': 'media punta'},
    19: {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 millones', 'Posicion': 'defensa central'},
    18: {'Nombre': 'Franco Armani', 'Edad': 30, 'Altura': 1.89, 'Precio': '3.5 millones', 'Posicion': 'portero'},
    17: {'Nombre': 'Leandro Paredes', 'Edad': 25, 'Altura': 1.89, 'Precio': '5.5 millones', 'Posicion': 'extremo izquierdo'},
    12: {'Nombre': 'Enzo Fernandez', 'Edad': 28, 'Altura': 1.90, 'Precio': '4.5 millones', 'Posicion': 'centro'},
    1: {'Nombre': 'Julian Alvarez', 'Edad': 32, 'Altura': 1.88, 'Precio': '5 millones', 'Posicion': 'centro'}
}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

#para ver la cantidad de elementos del diccionario
print('Tenemos cargados en el diccionario la cantidad de jugadores: ',  end=' ')
print(len(seleccionArgentina)) #son 8

#Método pilas
pila = [1,2,3]

#Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#Ahora sacamos elementos de la fila, por el final
elementoBorrado = pila.pop() #quita el último elemento y lo guarda en la variable
print(f'Sacamos el elemento {elementoBorrado}') #quita el último elemento
print(f'La pila ahora quedó asi: {pila}')

#Colas con listas(estructura de datos de tipo fifo(first input / first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

#Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('José')
print(cola)

#Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)





