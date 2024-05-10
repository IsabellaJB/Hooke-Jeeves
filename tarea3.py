import numpy as np

def booth_function(x, y):
    return ((x + 2*y - 7)**2) + ((2*x + y - 5)**2)

def exploratory_move(x, y, delta):
    x_nueva_suma = x + delta[0]
    x_nueva_resta = x - delta[0]
    resultado_x_suma = booth_function(x_nueva_suma, y)
    resultado_x_resta = booth_function(x_nueva_resta, y)
    y_nueva_suma = y + delta[1]
    y_nueva_resta = y - delta[1]
    resultado_y_suma = booth_function(x, y_nueva_suma)
    resultado_y_resta = booth_function(x, y_nueva_resta)
    if resultado_x_suma < resultado_x_resta:
        x_nueva = x_nueva_suma
    else:
        x_nueva = x_nueva_resta
    if resultado_y_suma < resultado_y_resta:
        y_nueva = y_nueva_suma
    else:
        y_nueva = y_nueva_resta
    return x_nueva, y_nueva

def pattern_move(k, k_minus_1):
    x = k[0] + (k[0] - k_minus_1[0])
    y = k[1] + (k[1] - k_minus_1[1])
    return x, y




def hooke_jeeves(punto_inicial, delta, alpha, epsilon): 
    x = punto_inicial[0]
    y = punto_inicial[1]

    movimiento_exploratorio = exploratory_move(x, y, delta)


    return(movimiento_exploratorio)






punto_inicial = (-5, -2.5)
delta = (0.5, 0.25)  
alpha = 2 
epsilon = 0.0001
max_iterations = 1000  
print(hooke_jeeves(punto_inicial,delta, alpha, epsilon))
