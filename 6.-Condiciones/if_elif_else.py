# La estructura `if-elif-else` se utiliza cuando hay múltiples condiciones posibles
# y quieres ejecutar un bloque de código diferente para cada una.
# Python evalúa las condiciones en orden, y ejecuta el bloque de la primera condición que sea verdadera.

# Ejemplo 1: Sistema de calificación de notas
nota = 85

if nota >= 90:
    print("Excelente: Calificación A")
elif nota >= 80: # Si la nota no es >= 90, pero sí >= 80
    print("Muy Bien: Calificación B")
elif nota >= 70: # Si la nota no es >= 80, pero sí >= 70
    print("Bien: Calificación C")
elif nota >= 60: # Si la nota no es >= 70, pero sí >= 60
    print("Suficiente: Calificación D")
else: # Si ninguna de las condiciones anteriores es verdadera
    print("Insuficiente: Calificación F")

# Ejemplo 2: Clasificar un día de la semana
dia = "Sábado"

if dia == "Lunes":
    print("Inicio de semana laboral.")
elif dia == "Viernes":
    print("¡Por fin es viernes! Casi fin de semana.")
elif dia == "Sábado" or dia == "Domingo": # Se pueden combinar condiciones
    print("Es fin de semana. ¡A disfrutar!")
else:
    print("Es un día entre semana.")

# Ejemplo 3: Determinar el estado del clima
temperatura = 15
clima = "soleado"

if temperatura > 30 and clima == "soleado":
    print("¡Día de playa! Hace mucho calor.")
elif temperatura >= 20 and clima == "soleado":
    print("Día agradable y soleado.")
elif temperatura < 10 and clima == "lluvioso":
    print("Hace frío y está lloviendo, lleva paraguas.")
elif clima == "nublado":
    print("El día está nublado, ideal para quedarse en casa.")
else:
    print("Clima inesperado o normal.")