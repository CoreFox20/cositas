import itertools
import math

def distanciaeuclidiana(p1, p2):
    return math.sqrt((p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2)

def calcular_matriz(puntos):
    n = len(puntos)
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                matriz[i][j] = distanciaeuclidiana(puntos[i], puntos[j])
            else:
                matriz[i][j] = float('inf')
    return matriz

def calcular_costo(ruta, matriz):
    costo = 0
    for i in range(len(ruta) - 1):
        costo += matriz[ruta[i]][ruta[i + 1]]
    costo += matriz[ruta[-1]][ruta[0]]  # Volver al inicio
    return costo

def encontrar_ruta_mas_corta(puntos):
    n = len(puntos)
    matriz = calcular_matriz(puntos)
    rutas = list(itertools.permutations(range(n)))
    ruta_mas_corta = None
    costo_mas_bajo = float('inf')
    for ruta in rutas:
        costo = calcular_costo(ruta, matriz)
        if costo < costo_mas_bajo:
            costo_mas_bajo = costo
            ruta_mas_corta = ruta
    return ruta_mas_corta, costo_mas_bajo

# Datos de Ruta 1
puntos_ruta1 = [
    ('A', 0, 0), ('B', 0.02, 0.01), ('C', 0.66, 0.25), ('D', 1.30, 0.30),
    ('E', 0.12, 0.11), ('F', 1.06, 0.37), ('G', 1.40, 0.34), ('H', 1.49, 0.42),
    ('I', 1.03, 0.28), ('J', 0.94, 0.27), ('K', 1.52, 0.19), ('L', 1.42, 0.17),
    ('M', 1.00, 0.40), ('N', 1.29, 0.19), ('O', 1.53, 0.38)
]

# Datos de Ruta 2
puntos_ruta2 = [
    ('A', 2.71, 0.42), ('B', 4.02, 1.85), ('C', 0.86, 1.43), ('D', 1.47, 1.25),
    ('E', 2.07, 2.16), ('F', 2.65, 1.9), ('G', 3.97, 2.00), ('H', 2.73, 3.18),
    ('I', 5.20, 0.64), ('J', 3.09, 1.82), ('K', 1.93, 2.62), ('L', 3.43, 2.41),
    ('M', 2.70, 2.29), ('N', 3.34, 2.63)
]

# Datos de Ruta 3
puntos_ruta3 = [
    ('A', 0.60, 0.68), ('B', 0.46, 0.63), ('C', 0.53, 1.06), ('D', 0.00, 0.00),
    ('E', 1.90, 0.25), ('F', 1.48, 0.51), ('G', 1.42, 1.06), ('H', 0.37, 0.68),
    ('I', 1.01, 0.72), ('J', 1.81, 0.35)
]

# Calcular rutas más cortas y sus costos
ruta1_mas_corta, costo1 = encontrar_ruta_mas_corta(puntos_ruta1)
ruta2_mas_corta, costo2 = encontrar_ruta_mas_corta(puntos_ruta2)
ruta3_mas_corta, costo3 = encontrar_ruta_mas_corta(puntos_ruta3)

# Convertir índices de rutas a letras
ruta1_letras = [puntos_ruta1[i][0] for i in ruta1_mas_corta]
ruta2_letras = [puntos_ruta2[i][0] for i in ruta2_mas_corta]
ruta3_letras = [puntos_ruta3[i][0] for i in ruta3_mas_corta]

# Mostrar resultados
print(f"Ruta mas corta para Ruta1: {' -> '.join(ruta1_letras)}, Costo: {costo1}")
print(f"Ruta mas corta para Ruta2: {' -> '.join(ruta2_letras)}, Costo: {costo2}")
print(f"Ruta mas corta para Ruta3: {' -> '.join(ruta3_letras)}, Costo: {costo3}")
