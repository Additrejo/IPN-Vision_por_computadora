# Laboratorio - Prácticas de realce y transformación de imagenes. IPN.  

<img width="896" height="368" alt="image" src="https://github.com/user-attachments/assets/7dcfda99-8b27-49d0-bfb5-7dff8aff30fd" />

**Descripción:**  
Aquí se archivan las prácticas y proyectos desarrollados en el curso, enfocados principalmente en las técnicas de pre-procesamiento que forman la base para cualquier sistema de análisis de imágenes.

El objetivo es explorar cómo las imágenes, que no son más que matrices de valores de píxeles, pueden ser manipuladas matemáticamente para mejorar su calidad o extraer información relevante.

---

# Índice

- [Software utilizado](#software-utilizado)
  - [Librerías](#librerías)
- [Introducción](#introducción)
- [Programas](#programas)
  - [Corrección gamma](#corrección-gamma)
    - [1. Transformación Logarítmica (`funLog`)](#1-transformación-logarítmica-funlog)
    - [2. Transformación Senoidal (`funSen`)](#2-transformación-senoidal-funsen)
    - [3. Transformación Exponencial (`funExp`)](#3-transformación-exponencial-funexp)
    - [4. Transformación Cosenoidal (`funCos`)](#4-transformación-cosenoidal-funcos)
    - [5. Transformación Exponencial Creciente (`funExpCres`)](#5-transformación-exponencial-creciente-funexpcres)
  - [Introducción a las Imágenes RGB](#introducción-a-las-imágenes-rgb)
    - [¿Cómo funcionan?](#cómo-funcionan)
    - [Representación Digital](#representación-digital)
    - [Aplicaciones](#aplicaciones)
  - [Obtención de los canales RGB](#obtención-de-los-canales-rgb)
  - [Introducción a los Operadores Puntuales en Visión por Computadora](#introducción-a-los-operadores-puntuales-en-visión-por-computadora)
    - [¿Cómo funcionan?](#cómo-funcionan-1)
    - [Características Clave:](#características-clave)
    - [Ejemplos Comunes de Operadores Puntuales:](#ejemplos-comunes-de-operadores-puntuales)
  - [Operadores sobre crater lunar](#operadores-sobre-crater-lunar)
  - [Introducción a la Transformación en Modelos de Color en Visión por Computadora](#introducción-a-la-transformación-en-modelos-de-color-en-visión-por-computadora)
    - [¿Por qué transformar modelos de color?](#por-qué-transformar-modelos-de-color)
    - [Ejemplos Comunes de Transformación:](#ejemplos-comunes-de-transformación)
  - [Transformación entre modelos de color aplicado a la Astrofotografía para la detección de cráteres en la luna](#transformación-entre-modelos-de-color-aplicado-a-la-astrofotografía-para-la-detección-de-cráteres-en-la-luna)

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

## Introducción a las Imágenes RGB

Una imagen digital es, en esencia, una **matriz bidimensional (o tridimensional para color)** de números. Cada número, o **píxel**, representa la intensidad o el color en una ubicación específica. Para imágenes en escala de grises, cada píxel almacena un único valor de intensidad (comúnmente de 0 a 255). Para imágenes a color (como RGB), cada píxel consta de tres valores, uno para cada componente de color (Rojo, Verde, Azul). Esta discretización de la luz en una cuadrícula numérica es el fundamento de todo el procesamiento y análisis de imágenes en el dominio digital.

Las **imágenes RGB** (del inglés **R**ed, **G**reen, **B**lue - Rojo, Verde, Azul) son un modelo de color aditivo fundamental utilizado para representar una vasta gama de colores. Este modelo se basa en la forma en que el ojo humano percibe el color y en cómo la luz se mezcla. En el sistema RGB, el rojo, el verde y el azul son considerados los colores primarios de la luz.


### ¿Cómo funcionan?

Cada color en una imagen RGB se forma mediante la mezcla de diferentes intensidades de estas tres luces primarias. Por ejemplo:  
<img width="1024" height="683" alt="image" src="https://github.com/user-attachments/assets/80cd0963-4f1e-43ea-9e28-04a8c138960f" />

* La combinación de luz roja y verde produce **amarillo**.
* La combinación de luz verde y azul produce **cian**.
* La combinación de luz roja y azul produce **magenta**.
* Cuando las tres luces primarias se combinan con la máxima intensidad, el resultado es el **blanco**.
* La ausencia total de las tres luces (intensidad cero) resulta en el **negro**.



### Representación Digital

En el ámbito digital, la intensidad de cada componente (Rojo, Verde, Azul) se representa comúnmente con un valor numérico. El estándar más extendido utiliza un rango de **0 a 255** para cada color (un sistema de 8 bits por canal). Esto significa que existen **más de 16 millones de colores posibles** (256 x 256 x 256 combinaciones distintas).

### Aplicaciones

El modelo RGB es la base para la visualización de imágenes en prácticamente todas las pantallas electrónicas modernas, incluyendo:
* Monitores de ordenador
* Televisores
* Cámaras digitales
* Teléfonos móviles

Estos dispositivos utilizan pequeños elementos de luz (píxeles) que emiten intensidades variables de luz roja, verde y azul para componer las imágenes que observamos.

## **[Obtención de los canales RGB](https://github.com/Additrejo/IPN-Vision_por_computadora/tree/main/Pr%C3%A1cticas%20-Realce%20y%20Transformaci%C3%B3n%20de%20Im%C3%A1genes/Obtenci%C3%B3n%20de%20los%20canales%20RGB)**   
<img width="930" height="361" alt="image" src="https://github.com/user-attachments/assets/a22e482a-20a3-478a-8132-5bca6d5ceae4" />

Este script de Python utiliza **OpenCV** y **NumPy** para realizar la siguiente tarea:

1.  **Carga una imagen** desde una ruta específica.
2.  **Inicializa tres matrices vacías** (una para cada canal de color: Azul, Verde, Rojo) del mismo tamaño que la imagen original.
3.  **Recorre cada píxel de la imagen original** y:
    * Copia el valor del componente **Azul** de cada píxel a la matriz `blue`.
    * Copia el valor del componente **Verde** de cada píxel a la matriz `green`.
    * Copia el valor del componente **Rojo** de cada píxel a la matriz `red`.
    * Los componentes no copiados en cada matriz de canal se mantienen en cero, lo que efectivamente aísla la información de un solo color.
4.  **Muestra en ventanas separadas**:
    * La **imagen original**.
    * La imagen que contiene solo el **canal Azul** (mostrando las intensidades de azul en sus píxeles correspondientes, el resto en negro).
    * La imagen que contiene solo el **canal Verde**.
    * La imagen que contiene solo el **canal Rojo**.
5.  **Espera una pulsación de tecla** para cerrar todas las ventanas de visualización.

En esencia, el código toma una imagen a color y descompone su información cromática, mostrando cómo cada color primario (Azul, Verde, Rojo) contribuye a la imagen final.

Para leer el paper completo visite:  
####  [PAPER: OBTENCIÓN DE LOS CANALES R, G, B EN ASTROFOTOGRAFÍA. (PDF) ](https://github.com/Additrejo/IPN-Vision_por_computadora/blob/main/Pr%C3%A1cticas%20-Realce%20y%20Transformaci%C3%B3n%20de%20Im%C3%A1genes/Obtenci%C3%B3n%20de%20los%20canales%20RGB/Obtenci%C3%B3n%20de%20canales%20RGB%20Perez%20Trejo%20Addi%20Alberto%209cv11.pdf)  
<img width="937" height="228" alt="image" src="https://github.com/user-attachments/assets/07ab2e4f-f2e5-472d-b0fa-95fc6681c5ad" />

---

## Introducción a los Operadores Puntuales en Visión por Computadora

En el vasto campo de la visión por computadora y el procesamiento digital de imágenes, los **operadores puntuales** (también conocidos como transformaciones puntuales o de píxel) constituyen una de las operaciones más fundamentales y sencillas. Su característica principal es que el nuevo valor de intensidad de un píxel en la imagen de salida **depende únicamente del valor de intensidad del mismo píxel en la imagen de entrada**, sin considerar los píxeles vecinos.

### ¿Cómo funcionan?

Un operador puntual aplica una función matemática `T` a cada píxel individual de una imagen. Si `f(x, y)` es la intensidad del píxel en las coordenadas `(x, y)` en la imagen de entrada, y `g(x, y)` es la intensidad del píxel correspondiente en la imagen de salida, entonces la relación se expresa como:

`g(x, y) = T[f(x, y)]`

Es decir, la transformación se aplica de forma independiente a cada píxel, utilizando solo su propio valor.

### Características Clave:

* **Independencia del Vecindario:** No se tienen en cuenta los píxeles circundantes. Esto los diferencia de los operadores locales o de vecindario (como los filtros de convolución).
* **Eficiencia Computacional:** Son muy rápidos de calcular, ya que la operación se realiza de forma paralela en cada píxel sin interacciones complejas.
* **Modificación de la Intensidad:** Su objetivo principal es alterar la distribución de los niveles de brillo o color de una imagen.

### Ejemplos Comunes de Operadores Puntuales:

1.  **Negativo de la Imagen:** Invierte los niveles de intensidad. Un píxel oscuro se vuelve claro y viceversa.
    * `g(x, y) = L - 1 - f(x, y)` (donde `L` es el número total de niveles de intensidad, ej. 256 para 8 bits).
2.  **Ajuste de Brillo:** Aumenta o disminuye la intensidad general de la imagen.
    * `g(x, y) = f(x, y) + b` (donde `b` es un valor constante de brillo).
3.  **Ajuste de Contraste:** Estira o comprime el rango de intensidades.
    * `g(x, y) = f(x, y) * c` (donde `c` es un factor de contraste).
4.  **Umbralización (Binarización):** Convierte una imagen en escala de grises en una imagen binaria (solo blanco y negro) basándose en un valor de umbral.
    * `g(x, y) = 255` si `f(x, y) > umbral`, de lo contrario `g(x, y) = 0`.
5.  **Transformación Logarítmica o de Potencia (Gamma Correction):** Se utiliza para comprimir o expandir rangos dinámicos, útil para mejorar la visibilidad de detalles en áreas oscuras o claras.

Los operadores puntuales son una base fundamental en el procesamiento de imágenes, a menudo utilizados como un primer paso para preprocesar imágenes antes de aplicar operaciones más complejas, o para mejorar visualmente su apariencia.

## **[Operadores sobre crater lunar](https://github.com/Additrejo/IPN-Vision_por_computadora/tree/main/Pr%C3%A1cticas%20-Realce%20y%20Transformaci%C3%B3n%20de%20Im%C3%A1genes/Operadores%20sobre%20crater)**   
<img width="933" height="304" alt="image" src="https://github.com/user-attachments/assets/b5323ded-272f-43da-bad4-bcd431bee8b0" />  

Este script de Python carga una imagen y aplica y muestra **siete transformaciones puntuales (píxel a píxel)** diferentes. Cada función define una operación que modifica los valores de los píxeles de la imagen de entrada para producir una imagen de salida, mostrando cómo se manipulan los niveles de intensidad sin considerar píxeles vecinos.

Las transformaciones implementadas son:

1.  **`iD()` (Identidad):** Crea una copia exacta de la imagen original.
2.  **`iN()` (Negativo):** Invierte los valores de intensidad (255 - valor original), creando un efecto de negativo fotográfico.
3.  **`iU()` (Umbral):** Binariza la imagen, haciendo blancos los píxeles cuya intensidad del canal verde está fuera de un rango `[p1, p2]` y negros los que están dentro.
4.  **`iUB()` (Umbral Binario):** Similar a `iU()`, binariza la imagen basándose en un rango de umbral para el canal verde.
5.  **`iUBI()` (Umbral Binario Invertido):** Inverte el umbral binario, haciendo negros los píxeles fuera del rango `[p1, p2]` y blancos los que están dentro.
6.  **`iUEG()` (Umbral Escala de Grises):** Mantiene los valores de escala de grises para los píxeles dentro del rango `[P1, P2]` y los hace blancos si están fuera.
7.  **`iUIEGI()` (Umbral Escala de Grises Invertido):** Intenta una binarización e inversión de la escala de grises basada en un rango `[P1, P2]`.

Finalmente, el script muestra todas estas imágenes resultantes en ventanas separadas y espera que el usuario presione una tecla para cerrarlas. Todas las operaciones se realizan sobre el canal verde de la imagen de entrada.

Para leer el paper completo visite:  
####  [PAPER: COPERADORES PUNTUALES APLICADOS A LA ASTROFOTOGRAFÍA PARA LA DETECCIÓN DE NUEVOS CRÁTERES EN LA LUNA. (PDF) ](https://github.com/Additrejo/IPN-Vision_por_computadora/blob/main/Pr%C3%A1cticas%20-Realce%20y%20Transformaci%C3%B3n%20de%20Im%C3%A1genes/operador%20puntual/Operadores%20puntuales.pdf)  

<img width="939" height="347" alt="image" src="https://github.com/user-attachments/assets/00c79bf8-ca78-4b23-b426-9fdb1966b2d7" />

---
## Introducción a la Transformación en Modelos de Color en Visión por Computadora

En visión por computadora y procesamiento de imágenes, el color de un píxel no se representa de una única manera. Existen diversos **modelos de color**, cada uno con sus propias ventajas y aplicaciones, que describen cómo se organizan y cuantifican los colores. La **transformación entre modelos de color** es el proceso de convertir la representación de color de una imagen de un modelo a otro.

### ¿Por qué transformar modelos de color?

La necesidad de transformar modelos de color surge por varias razones:

1.  **Percepción Humana vs. Captura de Dispositivos:**
    * **RGB (Rojo, Verde, Azul):** Es el modelo más común para la captura y visualización en dispositivos (cámaras, monitores). Es aditivo y se alinea con cómo los dispositivos emiten luz.
    * **HSV (Hue, Saturation, Value) / HSL (Hue, Saturation, Lightness):** Estos modelos están más alineados con la forma en que los humanos describen y perciben el color (tono, saturación, brillo/luminosidad). Son ideales para tareas de manipulación de color intuitiva.
    * **CMYK (Cian, Magenta, Amarillo, Negro):** Es un modelo sustractivo utilizado principalmente en impresión.

2.  **Facilitar Tareas de Procesamiento:**
    * **Separación de Color e Intensidad:** Modelos como HSV o YCbCr separan la información de la luminosidad (intensidad) de la información cromática (color). Esto es crucial para algoritmos donde se desea procesar el brillo sin afectar el color, o viceversa (ej., detección de bordes, ajuste de contraste).
    * **Robustez a la Iluminación:** Algunos algoritmos de visión por computadora son más robustos a los cambios de iluminación si se trabajan en modelos que desacoplan la intensidad, haciendo la detección de objetos más consistente.
    * **Segmentación por Color:** En tareas donde se busca segmentar objetos por su color, trabajar en espacios como HSV permite definir rangos de color de manera más directa y eficaz que en RGB.

3.  **Compresión de Imágenes:**
    * Modelos como YCbCr (utilizado en JPEG) son eficientes para la compresión, ya que el ojo humano es más sensible a los cambios en la luminosidad que en el color, permitiendo submuestrear los canales de croma sin una pérdida perceptible de calidad.

### Ejemplos Comunes de Transformación:

* **RGB a Escala de Grises:** Reduce la imagen a un solo canal de intensidad, eliminando la información de color. Es una transformación muy común para muchos algoritmos que no requieren color.
* **RGB a HSV/HSL:** Permite manipular el tono (el color "puro"), la saturación (qué tan "vivo" es el color) y el valor/luminosidad (qué tan oscuro o claro es).
* **RGB a YCbCr:** Separa la luminancia (Y) de los componentes de crominancia (Cb, Cr), útil en video y compresión.
* **RGB a Lab:** Intenta crear un espacio de color perceptual uniforme, donde las diferencias numéricas corresponden a diferencias visuales percibidas, útil para comparación de colores y retoque.

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/d84ca060-1d37-40e1-a94d-636f05f2347d" />

La capacidad de transformar imágenes entre diferentes modelos de color es una herramienta poderosa en visión por computadora, permitiendo adaptar los datos de color a las necesidades específicas de una aplicación o algoritmo, mejorando así la eficiencia y la calidad de los resultados.


## **[Transformación entre modelos de color aplicado a la Astrofotografía para la detección de cráteres en la luna](https://github.com/Additrejo/IPN-Vision_por_computadora/tree/main/Pr%C3%A1cticas%20-Realce%20y%20Transformaci%C3%B3n%20de%20Im%C3%A1genes/Operadores%20sobre%20crater)**  
<img width="935" height="332" alt="image" src="https://github.com/user-attachments/assets/4398f4c2-8742-4bdd-8bb3-16ad9c2983a1" />   
Este script de Python utiliza **OpenCV** y **NumPy** para explorar y transformar una imagen de entrada (cargada en formato RGB/BGR) a diferentes modelos de color comúnmente usados en visión por computadora.

El código está estructurado en secciones, cada una dedicada a una transformación específica:

1.  **De RGB a CMY:**
    * Carga la imagen original.
    * Divide la imagen RGB en sus canales B, G y R.
    * Calcula los componentes C, M e Y del modelo CMY usando la fórmula `1 - (color_RGB / 255)`.
    * Guarda la imagen CMY resultante y las representaciones visuales de sus canales individuales como archivos JPG.

2.  **De RGB a HSI (Hue, Saturation, Intensity):**
    * Utiliza la función `cv2.cvtColor()` de OpenCV para convertir la imagen original de RGB a HSV_FULL (que en este contexto se usa como HSI).
    * Separa los canales H, S e I de la imagen resultante.

3.  **De RGB a HSV (Hue, Saturation, Value):**
    * (Esta sección está comentada en el código, pero si se activara, convertiría la imagen original de BGR a HSV usando `cv2.COLOR_BGR2HSV` y separaría sus canales H, S y V).

4.  **De RGB a Escala de Grises:**
    * (Esta sección está comentada). Si estuviera activa, calcularía la escala de grises mediante una fórmula ponderada de los canales R, G y B, y luego la guardaría y mostraría usando `matplotlib`.

5.  **De RGB a YCbCr:**
    * Intenta calcular los componentes Y, Cb y Cr manualmente usando fórmulas, aunque estos cálculos manuales parecen incompletos o incorrectos (`286` para CR).
    * Luego, utiliza la función `cv2.cvtColor()` de OpenCV para una conversión correcta de RGB a YCbCr (`cv2.COLOR_RGB2YCrCb`).
    * Muestra la imagen YCbCr resultante y los canales Y, Cb y Cr (aunque las variables `Y`, `CB`, `CR` calculadas manualmente no se usarían para mostrar los canales de la imagen `ImagenYCbCr` generada por `cv2.cvtColor`).
    * Guarda la imagen YCbCr resultante.

6.  **CMYK:**
    * Intenta calcular los componentes C, M, Y y K del modelo CMYK.
    * La lógica para calcular K y los demás canales es compleja y no parece seguir directamente las fórmulas estándar para una conversión directa de RGB a CMYK en un contexto práctico de procesamiento de imágenes con OpenCV/NumPy.
    * (Las líneas para mostrar y guardar los canales individuales están comentadas).
    * Finalmente, intenta fusionar los 4 canales en una `ImagenCMYK` y la guarda.

Para leer el paper completo visite:  
####  [PAPER: Transformación entre modelos de color aplicado a la Astrofotografía para la detección de cráteres en la luna. (PDF) ](https://github.com/Additrejo/IPN-Vision_por_computadora/blob/main/Pr%C3%A1cticas%20-Realce%20y%20Transformaci%C3%B3n%20de%20Im%C3%A1genes/operador%20puntual/Operadores%20puntuales.pdf)  
<img width="934" height="309" alt="image" src="https://github.com/user-attachments/assets/f31eb5d1-76ba-4a76-be52-18c48937887a" />

---

## Elaborado por:  
- GitHub: [AddiTrejo](https://github.com/Additrejo)

---
