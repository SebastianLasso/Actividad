#Actividad 1

# Definimos una lista de números enteros
numeros = [1, 2, 3, 4, 5]
# Usamos una comprensión de listas para elevar cada número al cuadrado
cuadrados = [numero ** 2 for numero in numeros]
# Mostramos el resultado
print("Lista de números elevados al cuadrado:", cuadrados)


#Actividad 2

# Definimos variables de diferentes tipos
nombre = "Francisco"
edad = 20

# Usamos un formato de cadena f-string para insertar variables en una cadena de texto
mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años."

# Mostramos el mensaje formateado
print(mensaje)

#Actividad 3

# Definimos una variable para la edad
edad = 30

# Usamos un condicional para verificar la mayoría de edad
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

#Actividad 4

# Definimos una variable de tipo flotante
saldo = 15000.0

# Simulamos un ciclo de retiros de saldo hasta que el saldo sea menor que 10
while saldo > 10:
    retiro = 800.0
    saldo -= retiro
    print(f"Se ha retirado {retiro}, saldo actual: {saldo}")

#Actividad 5

# Definimos un diccionario con información personal
persona = {"nombre": "Maria","edad": 33,"ciudad": "Nueva York"}

# Iteramos sobre las claves y valores del diccionario
for clave, valor in persona.items():
    print(f"{clave.capitalize()}: {valor}")

