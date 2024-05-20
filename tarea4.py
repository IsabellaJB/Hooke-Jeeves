import numpy as np

def booth_function(arreglo):
    x = arreglo[0] 
    y = arreglo[1]
    return ((x + 2*y - 7)**2) + ((2*x + y - 5)**2)

def exploratory_move(arreglo_variables, delta):
    copia = arreglo_variables.copy()
    if len(arreglo_variables) == len(delta):
        nuevo_punto = []
        for i in range(0, len(arreglo_variables)):
            normal = arreglo_variables[i]
            suma = arreglo_variables[i] + delta[i]
            resta = arreglo_variables[i] - delta[i]
            copia[i] = normal
            evalua_normal = booth_function(copia)
            copia[i] = suma
            evalua_suma = booth_function(copia)
            copia[i] = resta
            evalua_resta = booth_function(copia)
            minimo = min(evalua_normal, evalua_suma, evalua_resta)
            if minimo == evalua_normal:
                nuevo_punto.append(normal)
            elif minimo == evalua_suma:
                nuevo_punto.append(suma)
            else:
                nuevo_punto.append(resta)
        return nuevo_punto
    else:
        print("No son de la misma dimension")

def pattern_move(k, k_minus_1):
    resul = []
    x = k[0] + (k[0] - k_minus_1[0])
    y = k[1] + (k[1] - k_minus_1[1])
    resul.append(x)
    resul.append(y)
    return resul

def actualizar_delta(delta,alpha):
    lista_deltas = []
    for i in delta:
        nueva_delta = i / 2
        lista_deltas.append(nueva_delta)
    return lista_deltas

def distancia_origen(vector):
    return np.linalg.norm(vector)

def verificar_distancia(vector, e):
    distancia = distancia_origen(vector)
    return distancia < e


def hooke_jeeves(punto_inicial, delta, alpha, epsilon): 
    k = 0
    punto_actual = punto_inicial
    punto_actual_evaluado = booth_function(punto_actual)
    distancia = distancia_origen(delta)

    while distancia > epsilon:
        movimiento_exploratorio = exploratory_move(punto_actual, delta)
        movimiento_exploratorio_evaluado = booth_function(movimiento_exploratorio)

        if movimiento_exploratorio_evaluado < punto_actual_evaluado:
            punto_anterior = punto_actual
            punto_actual = pattern_move(movimiento_exploratorio, punto_anterior)
            punto_actual_evaluado = booth_function(punto_actual)
        else:
            delta = actualizar_delta(delta, alpha)
            distancia = distancia_origen(delta)

    return punto_actual

punto_inicial = [-5, -2.5]
delta = [0.5, 0.25]  
alpha = 2 
epsilon = 0.1
print(hooke_jeeves(punto_inicial, delta, alpha, epsilon))






