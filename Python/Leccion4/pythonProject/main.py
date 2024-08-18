# LISTAS: las listas son un conjunto de elementos a los cuales se les asigna un índice. Las listas son
# modificables o mutables.
# Dentro de una misma lista, puede haber diferentes tipo de datos.Por ejemplo:
# lista = Ariel(0), Natalia(1), Liliana(2), Osvaldo(3) (en este caso,tipo string)
# Con las listas podemos usar tres funciones: append, insert y remove. También pop,clear y delete.

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














