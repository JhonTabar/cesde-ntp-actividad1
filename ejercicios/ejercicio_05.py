# Tema: Ciclos

# Ejercicio 1: Escribe un programa que utilice un ciclo (for o while) para imprimir todos 
# los números del 1 al 10.
# Escribe tu código debajo de esta línea:
i = 1
while i <= 10:
    print(i)
    i += 1

# Ejercicio 2: Utiliza un ciclo for para imprimir todos los números pares del 2 al 10 inclusive.
# Escribe tu código debajo de esta línea:
for numero in range (2,11,2):
    print("Los numeros pares son:",numero)

# Ejercicio 3: Usa un ciclo while para calcular la suma de los números del 1 al 5. Imprime el 
# resultado final (debe ser 15).
# Escribe tu código debajo de esta línea:
i = 1           
suma = 0
while i < 6:   
    suma += i
    i += 1
print("La suma de los números del 1 al 5 es:", suma)     