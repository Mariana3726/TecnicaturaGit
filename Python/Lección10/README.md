## _Constantes en Python_
### En Python, no hay una forma nativa de definir constantes (valores que no cambian). Sin embargo, por convención, se utilizan nombres en mayúsculas para indicar que una variable debe tratarse como una constante.

#### Ejemplo:

PI = 3.14159
MAX_INTENTOS = 5

#### Aunque estas variables pueden ser modificadas, el uso de mayúsculas indica a otros desarrolladores que no deberían hacerlo.

### Contexto Estático en Python
#### El contexto estático se refiere a elementos del código que no cambian durante la ejecución del programa. En Python, esto se puede lograr mediante el uso de variables y métodos estáticos dentro de una clase.

### Variables Estáticas: Son variables que pertenecen a la clase en lugar de a las instancias de la clase.

class MiClase:
    variable_estatica = 0

    def __init__(self):
        MiClase.variable_estatica += 1

obj1 = MiClase()
obj2 = MiClase()
print(MiClase.variable_estatica)  # Salida: 2

### Métodos Estáticos: Son métodos que no dependen de una instancia de la clase y no pueden modificar el estado de la clase o de la instancia.

class MiClase:
    @staticmethod
    def metodo_estatico():
        return "Este es un método estático"

print(MiClase.metodo_estatico())  # Salida: Este es un método estático
