import numpy as np

def booth_function(arreglo):
    x = arreglo[0]
    y = arreglo[1]
    return (x + 2*y - 7)**2 + (2*x + y - 5)**2

def exploratory_move(arreglo_variables, delta):
    copia = arreglo_variables.copy()
    nuevo_punto = []   
    for i in range(len(arreglo_variables)):
        normal = arreglo_variables[i]
        suma = normal + delta[i]
        resta = normal - delta[i]
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
        copia[i] = normal
    return nuevo_punto

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




punto_inicial = [-5, -2.5]
deltas = [0.5, 0.25]  
alpha = 2 
epsilon = 0.01



def hooke_jeeves(x0, deltas, alpha, epsilon, objective_function):
    xk = x0[:]
    xk_1 = x0[:]
    k = 0

    distancia = distancia_origen(deltas)
    
    while (distancia > 0):
        # Paso 2: Movimiento exploratorio
        xk_new = exploratory_move(xk, deltas, objective_function)
        
        if xk_new != xk:
            xk = xk_new[:]
            xk_1 = xk[:]
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
                deltas = [delta / alpha for delta in deltas]
        else:
            # Paso 3: Verificar si los incrementos son menores que epsilon
            if max(deltas) < epsilon:
                break
            deltas = [delta / alpha for delta in deltas]
    
    return xk



resultado = hooke_jeeves(punto_inicial, deltas, alpha, epsilon, booth_function)
print("Resultado final:", resultado)
# print("Valor de la función objetivo en el resultado final:", objective_function(resultado))

