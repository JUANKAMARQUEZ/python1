#3. Escribe los números pares del 2 hasta un número que se pida por teclado
#previamente.

numero=int(input("Introduce un número\n"))#hay que realizar un casting

#bucle que imprime tantas veces el nombre como letras contiene el nombre y en lineas distintas
for x in range(2, numero+2, 2):
  print(x) 
