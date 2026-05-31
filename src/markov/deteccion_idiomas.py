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
         
        prob = modelo.get(actual, {}).get(siguiente, 0.0001)
        puntuacion *= prob 
         
    return puntuacion 

if __name__ == "__main__":
    corpus_es = "el veloz murcielago hindu comia feliz cardillo y kiwi la ciguena tocaba el saxofon" 
    corpus_en = "the quick brown fox jumps over the lazy dog and the cat sleeps all day long" 
     
    matriz_espanol = entrenar_modelo_caracteres(corpus_es) 
    matriz_ingles = entrenar_modelo_caracteres(corpus_en) 
     
    textos_prueba = [
        "el murcielago duerme", 
        "the fox is fast" 
    ] 
     
    print("--- RESULTADOS DE DETECCIÓN ---") 
    for texto in textos_prueba:
        prob_es = calcular_probabilidad_texto(texto, matriz_espanol)
        prob_en = calcular_probabilidad_texto(texto, matriz_ingles) 
         
        if prob_es > prob_en:
            idioma = "ESPAÑOL"
        else: 
            idioma = "INGLÉS" 
             
        print(f"Texto: '{texto}' -> {idioma}")

