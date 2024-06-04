# Ejercicio 3: Calcular la estación del año
''''
mes = int(input('Escriba un mes del año (1 - 12): '))
estacion = None
if mes == 1 or mes == 2 or mes == 3:
    estacion = 'Verano'
elif mes == 4 or mes == 5 or mes == 6:
    estacion = 'Otoño'
elif mes == 7 or mes == 8 or mes == 9:
    estacion = 'Invierno'
elif mes == 10 or mes == 11 or mes == 12:
    estacion = 'Primavera'
else:
    estacion = 'Error, no existe ese mes'
print(f'Para el mes {mes} la estación es: {estacion}')
'''''

# Ejercicio 4: Etapas de la vida
'''''
edad = int(input('Digite su edad: '))
mensaje = None
if 0 <= edad < 10:
     mensaje = 'La infancia es increíble y bella'
elif 10 <= edad < 20:
    mensaje = 'Tienes muchos cambios, mucho que estudiar'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo'
elif 30 <= edad < 40:
    mensaje = 'Estás en una edad interesante'
elif 40 <= edad < 50:
    mensaje = 'Vida conforme'
elif 50 <= edad < 60:
    mensaje = 'Estás en una hermosa etapa'
elif 60 <= edad < 70:
    mensaje = 'Hora de viajar!'
elif 70 <= edad < 80:
    mensaje = 'Vivir tranquilo'
elif 80 <= edad < 90:
    mensaje = 'Vivir'
elif 90 <= edad < 100:
    mensaje = 'Vivirn t'
elif 100 <= edad < 110:
    mensaje = 'Ya no se que decir'
else:
    mensaje = 'Error, etapa de vida no reconocida'
print(f'Tu edad es: {edad}, {mensaje} ')
'''
#Ejercicio 5: Sistema de calificaiones
calificacion =  int(input('Digite una calificación entre 0 y 10: '))
if 9 <= calificacion <= 10:
    print('A')
elif 8 <= calificacion <= 9:
    print('B')
elif 7 <= calificacion <= 8:
    print('C')
elif 6 <= calificacion <= 7:
    print('D')
elif 0 <= calificacion <= 6:
    print('F')
else:
    print('Valor incorrecto')