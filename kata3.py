# Ejercicio 1

# Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
# Escribe una expresión de prueba para calcular si necesita una advertencia.
# Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.

velocidad=49
if velocidad>25:
    print("El asteroide se acerca muy rápido D:") 
else:
    print("No hay necesidad de preocuparse B)")
    
    
# Ejercicio 2
# Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
# Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
# Agrega las instrucciones que se ejecutarán si las expresiones de prueba son True o False

velocidad = 19
if velocidad>20:
    print("¡Debes buscar un asteroide en el cielo!")
elif velocidad==10:
    print("¡Debes buscar un asteroide en el cielo!")
else:
    print("No se podrá ver el asteroide desde la tierra")
    
    
# Ejercicio 3
# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.

tamano=30
velocidad=30

if tamano<25:
    print("Probablemente se quemará cuando entre a la atmósfera")	
elif tamano>=25 and tamano<1000:
    print("Podría causar mucho daño a la Tierra D:")
elif velocidad>20 or velocidad ==20:
    print("¡Debes buscar un asteroide en el cielo!")
    if velocidad>25:
        print("Advertencia! El asteroide se acerca muy rápido")
else:
    print("No hay nada que ver")