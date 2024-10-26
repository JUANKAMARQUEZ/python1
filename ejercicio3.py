#3. Escribe los números pares del 2 hasta un número que se pida por teclado
#previamente.

numero=int(input("Introduce un número\n"))#hay que realizar un casting

#Con el bucle for conseguimos imprimir los números de dos en dos, desde el 2 hasta el número elegido por usuario
for x in range(2, numero+2, 2):
  print(x) 
