class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f'{self.nombre}  {other.nombre}'

    def __sub__(self, otro): #Sub significa = substraction (resta)
        return self.edad - otro.edad

persona1 = Persona('Mariana', 31)
persona2 = Persona('Aguilera', 8)

persona1.__add__(persona2)

# persona1.__add__(persona2) sintaxis interna y automática

print(persona1 + persona2)
print(persona1 - persona2)