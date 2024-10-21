#4. Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice
#  de masa corporal y lo almacene en una variable, y muestre por pantalla la frase 
#Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
#Para calcular IMC se divide el peso, en kilos, por la altura, en metros al cuadrado.

#creamos las variables peso y estatura, siendo su valor el que facilita el usuario.
peso=float(input("Introduce tu peso en kg\n"))#hay que realizar un casting
estatura=float(input("Introduce tu estatura en metros\n"))

#creamos la variable imc y le damos su valor según la fórmula de imc.
imc = peso / (estatura**2)

#con print mostramos el indice de masa corporal (imc) redondeando con round a 2 decimales.
print(f"Tu índice de masa corporal es {round(imc,2)}")
