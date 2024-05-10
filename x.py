import math

def booth_function(x, y):
    operacion = ((x + 2*y - 7)**2) + ((2*x + y - 5)**2)
    return operacion

def hooke_jeeves(x0, x1, delta, alpha, epsilon):
    x = x0
    y = x1
    iterations = 0  # Contador de iteraciones
    while max(delta) > epsilon:
        x_best = (x, y)
        f_best = booth_function(x_best[0], x_best[1])
        for delta_x in [-delta[0], 0, delta[0]]:
            for delta_y in [-delta[1], 0, delta[1]]:
                x_trial = (x_best[0] + delta_x, x_best[1] + delta_y)
                f_trial = booth_function(x_trial[0], x_trial[1])
                if f_trial < f_best:
                    x_best = x_trial
                    f_best = f_trial
        if x_best != (x, y):
            x = x_best[0]
            y = x_best[1]
        else:
            delta = tuple(d / alpha for d in delta)
        iterations += 1 
    return x_best, iterations  

x0 = -5
x1 = -2.5
x = (-5,-2.5)
delta = (0.5, 0.25)
alpha = 2
epsilon = 0.0001

resultado, iteraciones = hooke_jeeves(x0, x1, delta, alpha, epsilon)

print("El mínimo se encuentra en x =", resultado)
print("El valor mínimo de la función es f(x) =", booth_function(resultado[0], resultado[1]))
print("Número de iteraciones:", iteraciones)
