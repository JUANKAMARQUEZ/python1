#2. Escribe un programa que pregunte el nombre y después de que el usuario
#lo introduzca muestre por pantalla el nombre en mayúsculas y el número de
#caracteres que tiene. Después deberá escribir el nombre tantas veces como
#letras contiene el nombre en líneas distintas.

x=input("Introduce su nombre\n")
print(f"¡Hola, {x.upper()}!"); #con .upper contamos el número de letras que contiene el nombre contando los espacios

print(f"La longuitud del nombre es de {len(x)}")#con "len" determinamos la longitud

#bucle que imprime tantas veces el nombre como letras contiene el nombre y en lineas distintas
for y in range(len(x)):
    print(x.upper())