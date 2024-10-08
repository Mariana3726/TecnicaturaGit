class Persona:  #Creamos una clase
    def __init__(self, nombre, apellido, edad):  #se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Ariel', 'Betancud', 40)  #necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

#Tarea
print(f'El objeto1 de la clase Persona es: {persona1.nombre} {persona1.apellido} y su edad es: {persona1.edad}')

persona2 = Persona('Osvaldo', 'Giordanini', 45)
print(f'El objeto2 de la clase Persona es: {persona2.nombre} {persona2.apellido} y su edad es:  {persona2.edad}')

#Tarea
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)

#Los objetos no comparten los valores, solo comparten los atributos. Y asi asignamos diferentes valores a cada atributo.

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto1 MODIFICADO de la clase Persona es: {persona1.nombre} {persona1.apellido} y su edad es: {persona1.edad}')


#Los atributos son las características
#Los métodos son el comportamiento que van a tener los objetos (acciones)

persona1.mostrar_detalle()
persona2.mostrar_detalle()






















