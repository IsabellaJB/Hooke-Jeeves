import numpy as np

def booth_function(arreglo):
    x = arreglo[0] 
    y = arreglo[1]
    return ((x + 2*y - 7)**2) + ((2*x + y - 5)**2)

def exploratory_move(x, deltas, objective_function):
    n = len(x)
    best_x = x[:]
    best_value = objective_function(x)
    for i in range(n):
        x_new = x[:]
        x_new[i] += deltas[i]
        new_value = objective_function(x_new)
        if new_value < best_value:
            best_x = x_new[:]
            best_value = new_value
        x_new = x[:]
        x_new[i] -= deltas[i]
        new_value = objective_function(x_new)
        if new_value < best_value:
            best_x = x_new[:]
            best_value = new_value
    return best_x

def pattern_move(xk, xk_1):
    return [xk[i] + (xk[i] - xk_1[i]) for i in range(len(xk))]

def actualizar_delta(delta, alpha):
    return [d / alpha for d in delta]

def distancia_origen(vector):
    return np.linalg.norm(vector)

def verificar_distancia(vector, e):
    return distancia_origen(vector) < e

def hooke_jeeves(x0, deltas, alpha, epsilon, objective_function):
    xk = x0[:]
    xk_1 = x0[:]
    k = 0

    while max(deltas) > epsilon:
        # Paso 2: Movimiento exploratorio
        xk_new = exploratory_move(xk, deltas, objective_function)
        
        if xk_new != xk:
            xk_1 = xk[:]
            xk = xk_new[:]
            k += 1
            
            # Paso 4: Movimiento de patrón
            xk_p = pattern_move(xk, xk_1)
            
            # Paso 5: Otro movimiento exploratorio desde el nuevo punto patrón
            xk_new = exploratory_move(xk_p, deltas, objective_function)
            
            if objective_function(xk_new) < objective_function(xk):
                xk = xk_new[:]
            else:
                # Paso 3: Verificar si los incrementos son menores que epsilon
                if max(deltas) < epsilon:
                    break
                deltas = actualizar_delta(deltas, alpha)
        else:
            # Paso 3: Verificar si los incrementos son menores que epsilon
            if max(deltas) < epsilon:
                break
            deltas = actualizar_delta(deltas, alpha)
    
    return xk

# Prueba con diferentes funciones objetivo

def objective_function(x):
    # Funcion Sphere
    return np.sum(np.square(x))

    # Funcion Himmelblau
    # return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

    # Función Rastrigin
    # n = len(x)
    # return 10 * n + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))  

    # Funcion Rosenbrock
    # return sum(100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2 for i in range(len(x) - 1))

# Ejemplo de uso:
# x0 = np.array([5, 5, 5])  # Para la función Sphere
# deltas = [0.5, 0.5, 0.5]
# alpha = 2  
# epsilon = 1e-6

x0 = [5, 5] 
deltas = [0.5,0.5]  
alpha = 2  
epsilon = 1e-6 

# x0 = [-5, -2.5] 
# deltas = [0.5,0.25]  
# alpha = 2  
# epsilon = 0.001

resultado = hooke_jeeves(x0, deltas, alpha, epsilon, booth_function)
print("Resultado final:", resultado)
print("Valor de la función objetivo en el resultado final:", booth_function(resultado))

# resultado = hooke_jeeves(x0, deltas, alpha, epsilon, objective_function)
# print("Resultado final:", resultado)
# print("Valor de la función objetivo en el resultado final:", objective_function(resultado))
