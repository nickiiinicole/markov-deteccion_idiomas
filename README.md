# Detección de Idiomas con Cadenas de Markov

Implementación de un detector de idiomas basado en **modelos de Markov de caracteres**. A partir de un corpus de entrenamiento, el modelo aprende las probabilidades de transición entre caracteres de cada idioma y las usa para clasificar textos nuevos.

---

## ¿Cómo funciona?

El sistema se basa en cadenas de Markov de primer orden sobre secuencias de caracteres:

1. **Entrenamiento**: dado un texto en un idioma, se calcula la probabilidad de que cada carácter vaya seguido de otro (`P(b | a)`).
2. **Puntuación**: dado un texto nuevo, se multiplican las probabilidades de cada par de caracteres consecutivos según cada modelo entrenado.
3. **Clasificación**: el idioma cuyo modelo asigna mayor probabilidad al texto gana.

### Ejemplo

Texto: "el murcielago duerme"

→ P(español) = 3.2e-12

→ P(inglés)  = 1.1e-18

→ Resultado: ESPAÑOL ✓

---

## Estructura del proyecto

→ markov-deteccion_idiomas/src/markov/deteccion_idiomas.py

---

## Uso

### Ejecutar el ejemplo incluido

```bash
python src/markov/deteccion_idiomas.py
```

Salida esperada:

--- RESULTADOS DE DETECCIÓN ---
Texto: 'el murcielago duerme' -> ESPAÑOL
Texto: 'the fox is fast'      -> INGLÉS

### Usar las funciones en tu propio código

```python
from src.markov.deteccion_idiomas import entrenar_modelo_caracteres, calcular_probabilidad_texto

# 1. Entrenar modelos con corpus de cada idioma
modelo_es = entrenar_modelo_caracteres("el veloz murcielago hindu comia feliz cardillo y kiwi...")
modelo_en = entrenar_modelo_caracteres("the quick brown fox jumps over the lazy dog...")

# 2. Puntuar un texto nuevo
texto = "hola mundo"
prob_es = calcular_probabilidad_texto(texto, modelo_es)
prob_en = calcular_probabilidad_texto(texto, modelo_en)

# 3. Clasificar
idioma = "ESPAÑOL" if prob_es > prob_en else "INGLÉS"
print(f"Idioma detectado: {idioma}")
```

---

## API

### `entrenar_modelo_caracteres(texto: str) -> dict`

Entrena un modelo de Markov de caracteres a partir de un corpus.

| Parámetro | Tipo  | Descripción                         |
|-----------|-------|-------------------------------------|
| `texto`   | `str` | Texto de entrenamiento en un idioma |

**Retorna**: diccionario de probabilidades de transición `{char_actual: {char_siguiente: probabilidad}}`.

El texto se normaliza a minúsculas y se eliminan los espacios antes de procesar.

---

### `calcular_probabilidad_texto(texto_nuevo: str, modelo: dict) -> float`

Calcula la probabilidad de que un texto pertenezca al idioma representado por `modelo`.

| Parámetro     | Tipo   | Descripción                                      |
|---------------|--------|--------------------------------------------------|
| `texto_nuevo` | `str`  | Texto a clasificar                               |
| `modelo`      | `dict` | Modelo entrenado con `entrenar_modelo_caracteres` |

**Retorna**: `float` — producto de las probabilidades de transición. Usa `0.0001` como suavizado para pares de caracteres no vistos en entrenamiento.

---

## Limitaciones

- El corpus de entrenamiento incluido es muy pequeño (una frase por idioma). Para mayor precisión, conviene usar textos más largos y variados.
- La multiplicación de probabilidades puede producir subdesbordamiento numérico (*underflow*) en textos largos; en una versión robusta se usaría la suma de logaritmos.
- Solo distingue entre los idiomas cuyos modelos se hayan entrenado explícitamente.

---

## Requisitos

- Python 3.7+
- Librería estándar únicamente (`collections`)
