import numpy as np

def booth_function(x, y):
    return ((x + 2*y - 7)**2) + ((2*x + y - 5)**2)

def exploratory_move(x, y, delta):
    new_x = x + delta[0] * np.random.uniform(-1, 1)  # Movimiento más dirigido
    new_y = y + delta[1] * np.random.uniform(-1, 1)  # Movimiento más dirigido
    return new_x, new_y

def pattern_move(x_k, y_k, x_k_minus_1, y_k_minus_1):
    new_x = x_k + (x_k - x_k_minus_1)
    new_y = y_k + (y_k - y_k_minus_1)
    return new_x, new_y

def algorithm(starting_point, delta, alpha, epsilon, max_iterations):
    x_k_minus_1, y_k_minus_1 = starting_point
    x_k, y_k = starting_point
    k = 0

    while k < max_iterations:  # Definir el criterio de parada
        x, y = exploratory_move(x_k, y_k, delta)
        if booth_function(x, y) < booth_function(x_k, y_k):
            x_k_plus_1, y_k_plus_1 = x, y
        else:
            delta = (delta[0] / alpha, delta[1] / alpha)
            k += 1
            continue

        pattern_moved = pattern_move(x_k_plus_1, y_k_plus_1, x_k, y_k)
        x, y = exploratory_move(pattern_moved[0], pattern_moved[1], delta)
        if booth_function(x, y) < booth_function(x_k_plus_1, y_k_plus_1):
            x_k, y_k = x, y
        else:
            x_k, y_k = x_k_plus_1, y_k_plus_1

        if np.linalg.norm((x_k - x_k_minus_1, y_k - y_k_minus_1)) < epsilon:
            break

        k += 1

    return x_k, y_k

# Parámetros proporcionados
starting_point = (-5, -2.5)  # Punto inicial
delta = (0.05, 0.05)  # Incrementos de variable más pequeños
alpha = 2  # Factor de reducción de paso
epsilon = 0.0001  # Parámetro de terminación
max_iterations = 1000  # Número máximo de iteraciones

# Ejecutar el algoritmo
result = algorithm(starting_point, delta, alpha, epsilon, max_iterations)
print("Resultado final:", result)
print("Valor de la función objetivo en el resultado final:", booth_function(*result))
