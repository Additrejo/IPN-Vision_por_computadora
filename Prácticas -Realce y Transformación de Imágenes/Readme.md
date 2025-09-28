# Laboratorio - Prácticas de realce y transformación de imagenes. IPN.  

<img width="896" height="368" alt="image" src="https://github.com/user-attachments/assets/7dcfda99-8b27-49d0-bfb5-7dff8aff30fd" />

**Descripción:**  
Aquí se archivan las prácticas y proyectos desarrollados en el curso, enfocados principalmente en las técnicas de pre-procesamiento que forman la base para cualquier sistema de análisis de imágenes.

El objetivo es explorar cómo las imágenes, que no son más que matrices de valores de píxeles, pueden ser manipuladas matemáticamente para mejorar su calidad o extraer información relevante.

---

## Índice

[Software utilizado](#software-utilizado)  
    [Librerías](#librerías)
[Introducción](#introducción)  
[Programas](#programas)  
[Operaciones Demostradas](#operaciones-demostradas)

---

## Software utilizado
[Anaconda Navigator](https://anaconda.org/anaconda/anaconda-navigator) - GUI.  
[spyder](https://www.spyder-ide.org/) - IDE.

### Librerías

Python 3.x  
[Pandas](https://pandas.pydata.org/)
```
pip install pandas 
```
[OpenCV](https://opencv.org/)  
```
pip install opencv-python  
```
[NumPy](https://numpy.org/)  
```
pip install numpy
```


---

# Introducción

La Visión por Computadora es una disciplina científica, en la intersección de la inteligencia artificial y el procesamiento de señales, cuyo objetivo es desarrollar los formalismos teóricos y los métodos algorítmicos que permitan a las máquinas adquirir, procesar, analizar e interpretar datos visuales del mundo real. El fin último es emular la capacidad de la visión humana para extraer información significativa y tomar decisiones a partir de ella.

El pilar de esta disciplina reside en el procesamiento digital de imágenes. En su forma más fundamental, una imagen digital es una representación discreta del mundo visual, codificada como una matriz numérica donde cada elemento, conocido como píxel, cuantifica una propiedad física como la intensidad lumínica o el cromatismo.  Toda operación de visión artificial, por compleja que sea, se reduce en su nivel más elemental a una secuencia de manipulaciones matemáticas sobre estas matrices.

La Visión por Computadora es una disciplina científica, en la intersección de la inteligencia artificial y el procesamiento de señales, cuyo objetivo es desarrollar los formalismos teóricos y los métodos algorítmicos que permitan a las máquinas adquirir, procesar, analizar e interpretar datos visuales del mundo real. El fin último es emular la capacidad de la visión humana para extraer información significativa y tomar decisiones a partir de ella.

El pilar de esta disciplina reside en el procesamiento digital de imágenes. En su forma más fundamental, una imagen digital es una representación discreta del mundo visual, codificada como una matriz numérica donde cada elemento, conocido como píxel, cuantifica una propiedad física como la intensidad lumínica o el cromatismo.  Toda operación de visión artificial, por compleja que sea, se reduce en su nivel más elemental a una secuencia de manipulaciones matemáticas sobre estas matrices.

Dentro de este paradigma, las operaciones de pre-procesamiento son un paso ineludible y se pueden clasificar en dos grandes categorías:

Realce de Imágenes: Conjunto de técnicas enfocadas en mejorar la calidad perceptual o la interpretabilidad de una imagen para un observador humano o para una etapa algorítmica posterior. Estas operaciones, como el ajuste de contraste o la reducción de ruido, no añaden información nueva, sino que acentúan características existentes o atenúan información irrelevante.

Transformación de Imágenes: Implica la alteración de la representación de la imagen para revelar información que no es explícita en su dominio original. Esto incluye transformaciones geométricas, que modifican las coordenadas espaciales de los píxeles (e.g., rotación, escalado), y transformaciones de dominio, que cambian la base de representación de la imagen, como la conversión entre espacios de color (RGB, HSV) o la transición al dominio de la frecuencia mediante la Transformada de Fourier.

El dominio de estas técnicas de bajo nivel es, por tanto, el prerrequisito esencial sobre el cual se construyen las soluciones a problemas de alto nivel como la detección de objetos, la segmentación semántica y el reconocimiento de patrones.


---

## Programas

## **[Correción gamma](https://github.com/Additrejo/IPN-Vision_por_computadora/blob/main/Pr%C3%A1cticas%20-Realce%20y%20Transformaci%C3%B3n%20de%20Im%C3%A1genes/Correcci%C3%B3n%20gamma/Correccion_Gamma.py)**   
<img width="934" height="449" alt="image" src="https://github.com/user-attachments/assets/26adb90b-cd2a-4e41-8ab1-57076e14fb84" />

Este script implementa cinco transformaciones no lineales para el realce de contraste en imágenes. Cada función mapea los valores de intensidad de los píxeles de entrada, $r \in [0, 255]$, a nuevos valores de salida, $s \in [0, 255]$.

## 1. Transformación Logarítmica (`funLog`)

-   **Propósito:** Expande el rango dinámico de las regiones oscuras y comprime las claras. Ideal para mejorar la visibilidad en imágenes con baja iluminación o mucho detalle en las sombras.
-   **Fórmula:**
    $$s = \frac{255}{\log(1 + 255a)} \cdot \log(1 + a \cdot r)$$
    Donde $a$ es un parámetro de ajuste (fijado a $1$ en el código).

---

## 2. Transformación Senoidal (`funSen`)

-   **Propósito:** Aplica una curva senoidal que tiende a expandir el contraste en los rangos de intensidad medios, mientras comprime los valores muy oscuros y muy claros.
-   **Fórmula:**
    $$s = 255 \cdot \sin\left(\frac{\pi \cdot r}{2 \cdot 255}\right)$$

---

## 3. Transformación Exponencial (`funExp`)

-   **Propósito:** Realiza una transformación de tipo exponencial (similar a una corrección gamma inversa). Con el parámetro negativo (`a=-10`), esta función tiende a realzar las regiones claras de la imagen y comprimir las oscuras.
-   **Fórmula:**
    $$s = \frac{255}{1 - e^{a}} \cdot \left(1 - e^{\frac{a \cdot r}{255}}\right)$$
    Donde $a$ es un parámetro de ajuste (fijado a $-10$ en el código).

---

## 4. Transformación Cosenoidal (`funCos`)

-   **Propósito:** Aplica una curva cosenoidal que, dependiendo de la fase, puede comprimir los rangos de intensidad medios y expandir los extremos. Su uso es menos común en realce estándar.
-   **Fórmula:**
    $$s = 255 \cdot \left(1 - \cos\left(\frac{\pi \cdot r}{2 \cdot 255}\right)\right)$$
    **Nota:** La implementación en el código utiliza bucles `for` explícitos, lo cual es menos eficiente que las operaciones vectorizadas de NumPy. Además, asume una imagen en escala de grises o puede tener un comportamiento inesperado si se aplica directamente a los píxeles RGB como un todo.

---

## 5. Transformación Exponencial Creciente (`funExpCres`)

-   **Propósito:** Implementa otra forma de transformación exponencial que expande significativamente el contraste de las regiones oscuras, llevando rápidamente los valores bajos hacia tonos más claros, mientras comprime las regiones brillantes.
-   **Fórmula:**
    $$s = \frac{255}{e^{a} - 1} \cdot \left(e^{\frac{a \cdot r}{255}} - 1\right)$$
    Donde $a$ es un parámetro de ajuste (fijado a $2$ en el código).
    **Nota:** Similar a `funCos`, esta implementación también utiliza bucles `for` ineficientes y comparte la misma consideración sobre su aplicación a imágenes a color.

Para leer el paper completo visite:  
####  [PAPER: Corrección Gamma aplicado a la astrofotografía para la detección de nuevos cráteres en la luna (PDF) ](https://github.com/Additrejo/IPN-Vision_por_computadora/blob/main/Pr%C3%A1cticas%20-Realce%20y%20Transformaci%C3%B3n%20de%20Im%C3%A1genes/Correcci%C3%B3n%20gamma/Correcci%C3%B3n%20Gamma%20Perez%20Trejo%20Addi%20Alberto.pdf)
<img width="931" height="275" alt="image" src="https://github.com/user-attachments/assets/867c8580-3d99-4065-896d-ad35339a5e33" />

---

## Elaborado por:  
- GitHub: [AddiTrejo](https://github.com/Additrejo)

---
