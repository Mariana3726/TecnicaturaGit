class Persona2:
    def __init__(self, nombre, apellido, edad):  #TodoEncapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  #Decorador
    def nombre(self):  #Método Getter
        print('Estamos usando el método Get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  #Método Setter
        print('Estamos usando el método Set')
        self._nombre = nombre

    @property  #Decorador
    def apellido(self):  #Método Getter
        print('Estamos usando el método Get')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  #Método Setter
        print('Estamos usando el método Set')
        self._apellido = apellido

    @property  # Decorador
    def edad(self):  # Método Getter
        print('Estamos usando el método Get')
        return self._edad

    @edad.setter
    def edad(self, edad):  # Método Setter
        print('Estamos usando el método Set')
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':

    # Llamamos al método getter

    persona1 = Persona2('Mariana', 'Aguilera', 31)
    print(persona1.nombre)

    persona1 = Persona2('Marina', 'Aguilera', 31)
    print(persona1.apellido)

    persona1 = Persona2('Mariana', 'Aguilera', 31)
    print(persona1.edad)

    #Llamamos al método setter

    persona1.nombre = 'Florencia'
    print(persona1.nombre) #Acá de nuevo, método getter

    #Mostrar detalle
    print(persona1.mostrar_detalles())

    #Atributo read-only (solo lectura) sería la edad porque no tiene el método set
    #persona1._edad = 40 #no se puede hacer
    print(persona1.edad)

    #Tarea: crear tres objetos mas, utilizando los métodos getter y setter para modificar, y mostrar los cambios

    #Objeto 1
    persona4 = Persona2('Javier', 'Torrico', 27)
    persona4.nombre = 'Pablo'
    persona4.apellido = 'Túnez'
    print(persona4.edad)
    print(persona4.mostrar_detalles())

    #Objeto 2
    persona5 = Persona2('Liliana', 'Dávila', 64)
    print(persona5.nombre)
    print(persona5.apellido)
    print(persona5.edad)
    persona5.nombre = 'Graciela'
    persona5.apellido = 'Montanaro'
    persona5.edad = '80'
    print(persona5.mostrar_detalles())

    #Objeto 3
    persona6 = Persona2('Omar', 'Aguilera', 66)
    persona6.nombre = 'Marcos'
    persona6.apellido = 'Nagger'
    persona6.edad = 50
    print(persona6.mostrar_detalles())

    print(__name__)















