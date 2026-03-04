# Tema: Input y Casting (Conversión de tipos)

# Ejercicio 1: Pide al usuario que ingrese su nombre usando input() y luego imprime un saludo 
# personalizado que incluya su nombre.
# Escribe tu código debajo de esta línea:
nombre_usuario = input("Por favor, ingresa tu nombre: ")
print(f"¡Hola, {nombre_usuario}! Bienvenido.")


# Ejercicio 2: Pide al usuario que ingrese su edad como texto (input siempre devuelve texto).
# Convierte esa edad a un número entero (casting) y luego calcula y muestra cuántos años tendrá 
# en el año 2050 (puedes asumir que el año actual es 2024 para el cálculo, o restarle su año de nacimiento).
# Simplificado: asume que sumarle 26 años le da su edad en 2050.
# Escribe tu código debajo de esta línea:
edad_usuario = input("Ingrese su edad:")
edad_usuario = int(edad_usuario)
edad_en_2050 = edad_usuario + 26
print(f"En el año 2050, tendrás {edad_en_2050} años.")


# Ejercicio 3: Pide al usuario que ingrese el precio de un producto. Convierte el valor ingresado 
# a un número decimal (float). Luego, calcula y muestra el precio con un 20% de descuento.
# Escribe tu código debajo de esta línea:
precio_usuario = input("Ingrese el precio del producto:")
precio_usuario = float(precio_usuario)
precio_final = precio_usuario * 0.8
print(f"El precio final seria: {precio_final}")