from collections import defaultdict, Counter

def entrenar_modelo_caracteres(texto): 
    texto = texto.lower().replace(" ", "") 
    transiciones = defaultdict(Counter) 
     
    for i in range(len(texto) - 1): 
        actual = texto[i]
        siguiente = texto[i + 1] 
        transiciones[actual][siguiente] += 1 
         
    probabilidades = defaultdict(dict)
    for actual, siguientes in transiciones.items(): 
        total = sum(siguientes.values())
        for siguiente, conteo in siguientes.items(): 
            probabilidades[actual][siguiente] = conteo / total 
             
    return probabilidades 

def calcular_probabilidad_texto(texto_nuevo, modelo): 
    texto_nuevo = texto_nuevo.lower().replace(" ", "")
    puntuacion = 1.0 
     
    for i in range(len(texto_nuevo) - 1):
        actual = texto_nuevo[i] 
        siguiente = texto_nuevo[i + 1] 
         
        # Aplicamos suavizado (0.0001) para evitar multiplicar por 0
        prob = modelo.get(actual, {}).get(siguiente, 0.0001)
        puntuacion *= prob 
         
    return puntuacion 
