import math

def funcion(x):
    return x**2 + 2*x + 1  

def hooke_jeeves(x0, delta, epsilon):
    x = x0
    while delta > epsilon:
        x_best = x
        f_best = funcion(x_best)
        
        for delta_x in [-delta, 0, delta]:
            x_trial = x_best + delta_x
            f_trial = funcion(x_trial)
            if f_trial < f_best:
                x_best = x_trial
                f_best = f_trial
        if x_best != x:
            x = x_best
        else:
            delta /= 2
    return x


x0 = 0.0
delta = 0.1
epsilon = 0.0001


resultado = hooke_jeeves(x0, delta, epsilon)

print("El mínimo se encuentra en x =", resultado)
print("El valor mínimo de la función es f(x) =", funcion(resultado))
