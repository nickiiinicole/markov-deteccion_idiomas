from collections import defaultdict, Counter
import os
  
def leer_archivo(ruta_archivo):
    """
    Abre un archivo de texto y devuelve su contenido.
    """
    if not os.path.exists(ruta_archivo):
        return ""
        
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return archivo.read()


def entrenar_modelo_caracteres(texto): 
    texto = texto.lower().replace(" ", "").replace("\n", "")  
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
    texto_nuevo = texto_nuevo.lower().replace(" ", "").replace("\n", "") 
    puntuacion = 1.0 
     
    for i in range(len(texto_nuevo) - 1):
        actual = texto_nuevo[i] 
        siguiente = texto_nuevo[i + 1] 
         
        prob = modelo.get(actual, {}).get(siguiente, 0.0001)
        puntuacion *= prob 
         
    return puntuacion 


if __name__ == "__main__":

    texto_entrenamiento_es = leer_archivo("docs/entrenamiento/corpus_es.txt")
    texto_entrenamiento_en = leer_archivo("docs/entrenamiento/corpus_en.txt")
    texto_prueba = leer_archivo("docs/libro/quijote.txt")
    
    matriz_espanol = entrenar_modelo_caracteres(texto_entrenamiento_es) 
    
    matriz_ingles = entrenar_modelo_caracteres(texto_entrenamiento_en) 
     
    print("--- RESULTADOS DE LA DETECCIÓN ---")
    print(f"Texto a evaluar (primeros 50 caracteres): '{texto_prueba[:50]}...'")
    
    prob_es = calcular_probabilidad_texto(texto_prueba, matriz_espanol)
    prob_en = calcular_probabilidad_texto(texto_prueba, matriz_ingles) 

    if prob_es > prob_en:
        print(">>> CLASIFICACION : ¡ESPAÑOL! <<<")
    else: 
        print(">>> CLASIFICACION : ¡INGLÉS! <<<")



