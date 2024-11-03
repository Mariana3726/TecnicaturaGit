from Persona2 import Persona2

print('Creación de objetos'.center(50, '-'))
if __name__ == '__main__':
    persona7 = Persona2('María', 'Pérez', 32)
    persona7.mostrar_detalles()

    print(__name__)

print('Eliminación de objetos'.center(50, '-'))
del persona7
