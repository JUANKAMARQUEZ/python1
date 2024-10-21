#5. Escribe un programa que genere una multiplicación de dos números del 2 al 10 al azar,
# # pregunte por el resultado y diga si se ha dado la respuesta correcta  o no es correcta,
# # y en este caso escribir la correcta.

#se importa random
import random

#se crea los dos números aleatorios con random.Con randint conseguimos que los números sean enteros.
numero1 = random.randint(2,10)
numero2 = random.randint(2,10)
resultado = numero1*numero2
print(f"¿Cuanto es {numero1} x {numero2} ?")

resultadoUsuario=int(input())

if resultadoUsuario==resultado:
    print(f"Es correcto.El resultado es {resultado}")
else:
    print(f"No es correcto. El resultado correcto es {resultado}")

