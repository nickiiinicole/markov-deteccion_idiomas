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
