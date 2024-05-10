# Función objetivo (Booth Function)
def booth_function(x, y):
    return (x + 2*y - 7)**2 + (2*x + y - 5)**2

# Definición de los parámetros iniciales
punto_inicial = (-5, -2.5)
delta = (0.5, 0.25)
alpha = 2

# Punto inicial
x, y = punto_inicial
print("Punto inicial:", (x, y))

# Movimiento exploratorio
x_nueva_suma = x + delta[0]
x_nueva_resta = x - delta[0]
resultado_x_suma = booth_function(x_nueva_suma, y)
resultado_x_resta = booth_function(x_nueva_resta, y)

y_nueva_suma = y + delta[1]
y_nueva_resta = y - delta[1]
resultado_y_suma = booth_function(x, y_nueva_suma)
resultado_y_resta = booth_function(x, y_nueva_resta)

print("Resultados x:", resultado_x_suma, resultado_x_resta)
print("Resultados y:", resultado_y_suma, resultado_y_resta)

# Determinación de la nueva posición
if resultado_x_suma < resultado_x_resta:
    x_nueva = x_nueva_suma
else:
    x_nueva = x_nueva_resta

if resultado_y_suma < resultado_y_resta:
    y_nueva = y_nueva_suma
else:
    y_nueva = y_nueva_resta

print("Nuevo punto:", (x_nueva, y_nueva))
