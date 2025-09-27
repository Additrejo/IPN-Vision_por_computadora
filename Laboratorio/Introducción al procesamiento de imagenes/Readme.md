# Laboratorio - Introducción al procesamiento de imagenes. IPN.  

<img width="1128" height="293" alt="image" src="https://github.com/user-attachments/assets/ed0834bc-0702-4766-bef4-d15edf167580" />  

**Descripción:**  
Programas realizados para la matería de visión por computadora en mi estancia en el IPN.

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

## Operaciones Básicas de Imágenes con OpenCV y NumPy

Este repositorio contiene una serie de scripts sencillos en Python que demuestran las operaciones fundamentales de procesamiento de imágenes utilizando  bibliotecas **OpenCV** y **NumPy**. A través de estos ejemplos, exploraremos cómo interactuar con las imágenes a un nivel de píxel para realizar transformaciones básicas como lecturas, visualizaciones, volteos y operaciones aritméticas (suma, resta, multiplicación, división y rotación).

## 🚀 ¿Qué Encontrarás Aquí?

Cada script está diseñado para ser claro y conciso, mostrando una operación específica sobre imágenes. El enfoque principal está en entender cómo los valores de los píxeles se manipulan directamente para lograr diferentes efectos visuales.

### Énfasis en la Manipulación por Píxeles

Las imágenes digitales son, en esencia, matrices de números. Cada "píxel" en una imagen a color (como las que manejamos aquí) se representa comúnmente por tres valores, uno para cada canal de color: Rojo, Verde y Azul (RGB). Estos valores suelen oscilar entre 0 y 255.

Por ejemplo, un píxel puede representarse así:
* `[255, 0, 0]` para **Rojo puro**
* `[0, 255, 0]` para **Verde puro**
* `[0, 0, 255]` para **Azul puro**
* `[0, 0, 0]` para **Negro**
* `[255, 255, 255]` para **Blanco**
  
Aquí una representación visual de cómo se ven los valores numéricos de los píxeles en una pequeña sección de una imagen a color:  

<img width="446" height="449" alt="image" src="https://github.com/user-attachments/assets/34906a86-2fc0-4212-8f4a-a855d4f03bda" />

Cuando realizamos operaciones como suma, resta, multiplicación o división entre dos imágenes, estamos literalmente combinando, alterando o comparando estos valores numéricos píxel a píxel.  

<img width="416" height="448" alt="image" src="https://github.com/user-attachments/assets/041ecfbc-6574-4625-a4ee-f38538ba3bc5" />

---

#  Operaciones Demostradas

* **Lectura y Visualización**: Cómo cargar y mostrar imágenes.
* **Volteo (Flip)**: Invertir una imagen horizontal o verticalmente.
* **Rotación**: Girar una imagen alrededor de un punto central.
* **Operaciones Aritméticas (Píxel a Píxel)**:
    * **Suma**: Combinar las intensidades de dos imágenes.
    * **Resta**: Resaltar las diferencias entre dos imágenes.
    * **Multiplicación**: Modular la intensidad o aplicar efectos de máscara.
    * **División**: Comparar ratios de intensidad (¡con cuidado de la división por cero!).

Cada script ilustra estos conceptos, y en algunos casos, se explican las peculiaridades y desafíos de realizar estas operaciones directamente sobre los valores de píxel (como los problemas de desbordamiento de enteros o división por cero) y cómo las funciones especializadas de OpenCV los abordan.

---

## Programas

**[Mostrar imagen con python](https://github.com/Additrejo/IPN-Vision_por_computadora/tree/main/Laboratorio/Introducci%C3%B3n%20al%20procesamiento%20de%20imagenes/1.%20Mostrar%20imagen%20con%20python)**   
<img width="456" height="413" alt="image" src="https://github.com/user-attachments/assets/2d8e6dc8-ac8d-41b0-bda1-2ea192bfcb8a" />

**Descripción:**  
El script lee un archivo de imagen desde una ubicación específica en la computadora, lo muestra en una ventana titulada "Imagen Original" y espera a que el usuario presione una tecla para cerrar la ventana y terminar el programa.

---

**[Suma de dos imagenes con OpenCV](https://github.com/Additrejo/IPN-Vision_por_computadora/tree/main/Laboratorio/Introducci%C3%B3n%20al%20procesamiento%20de%20imagenes/2.%20suma%20de%20%202%20imagenes%20con%20python)**  
<img width="459" height="409" alt="image" src="https://github.com/user-attachments/assets/554217d9-abe5-460a-a0ed-e7a163fbdca8" />

**Descripción:**  
Este código utiliza las bibliotecas OpenCV y NumPy para cargar dos imágenes, combinar sus píxeles de dos maneras diferentes (sumándolos directamente y promediándolos) y mostrar uno de los resultados.

Saturación de Color (Overflow): La suma directa en la variable nueva es problemática. Los valores de los píxeles van de 0 a 255. Si sumas dos píxeles (ej. 150 + 150 = 300), el resultado excede el máximo de 255. En lugar de quedarse en 255, NumPy realiza una operación de "módulo" (ej. 300 % 256 = 44), lo que produce colores extraños y mucho más oscuros de lo esperado. La forma correcta de sumar imágenes en OpenCV es usando cv2.add(imagen, imagen1), que maneja la saturación automáticamente (si el resultado es > 255, lo deja en 255).

La imagen resultante de la suma, (nueva), sufre una fuerte distorsión de color debido a un problema conocido como desbordamiento de entero (en inglés, integer overflow o wraparound).

---

**[Resta de dos imagenes con OpenCV](https://github.com/Additrejo/IPN-Vision_por_computadora/tree/main/Laboratorio/Introducci%C3%B3n%20al%20procesamiento%20de%20imagenes/3.%20Resta%20de%202%20imagenes%20con%20python)**  
<img width="455" height="414" alt="image" src="https://github.com/user-attachments/assets/1e3e76d9-cc3a-4567-9d4e-94b305c600f7" />
 

**Descripción:**  
Este código carga dos imágenes y crea una tercera imagen (nueva) restando los valores de los píxeles de la primera imagen de los de la segunda. El resultado principal es una imagen que resalta las diferencias entre las dos originales.  

El Problema: Desbordamiento Negativo (Wraparound)
Los valores de los píxeles están en el rango de 0 a 255. Cuando el resultado de una resta es menor que 0, el sistema no puede representarlo y "da la vuelta" desde el valor máximo.  

Ejemplo: Imagina que en un píxel, la imagen1 tiene un valor de rojo de 50 y la imagen tiene un valor de rojo de 80.  

La resta matemática es: 50 - 80 = -30.  

El problema: El valor no puede ser negativo.   
El sistema realiza la operación módulo 256:
−30(mod256)=226  
El resultado visual: En lugar de obtener un píxel oscuro (que sería 0), el resultado es 226, un valor muy brillante.

---

**[Multplicación de dos imagenes con OpenCV](https://github.com/Additrejo/IPN-Vision_por_computadora/tree/main/Laboratorio/Introducci%C3%B3n%20al%20procesamiento%20de%20imagenes/4.%20Multiplicaci%C3%B3n%20de%202%20imagenes%20con%20python)**  
<img width="485" height="441" alt="image" src="https://github.com/user-attachments/assets/b7c8fc68-7a7e-4662-a3aa-14b1aa99cc6f" />

**Descripción:**  
Al igual que con la suma y la resta, la multiplicación directa de píxeles provoca un desbordamiento de entero (wraparound), pero sus efectos son visualmente distintos. La multiplicación tiende a oscurecer drásticamente la imagen.

El Problema: Oscurecimiento por Desbordamiento
Cuando multiplicas dos números entre 0 y 255 (los valores de los píxeles), el resultado suele ser mucho mayor que 255, lo que causa el efecto de "dar la vuelta" o wraparound.  

Ejemplo: Consideremos dos píxeles con valores de intensidad medios, como 20 y 30.  

La multiplicación matemática es: 20 * 30 = 600.  

El problema: El valor máximo es 255. El sistema calcula el módulo 256:
600(mod256)=88  

El resultado visual: En lugar de un valor muy brillante (que se esperaría de una multiplicación), se obtiene un valor relativamente oscuro (88). A menos que uno de los valores del píxel sea muy pequeño (cercano a 1), la multiplicación casi siempre resultará en un desbordamiento, llevando a colores oscuros e inesperados. Las únicas áreas que permanecerán sin cambios son las negras (donde el valor del píxel es 0).  

La multiplicación de píxeles se usa a menudo para crear máscaras o para modular el brillo, pero debe hacerse normalizando primero los valores de los píxeles (generalmente a un rango de 0.0 a 1.0) para evitar este problema de desbordamiento y obtener un resultado predecible. La función cv2.multiply() también gestiona esta operación de forma más controlada.

---

**[División de dos imagenes con OpenCV](https://github.com/Additrejo/IPN-Vision_por_computadora/tree/main/Laboratorio/Introducci%C3%B3n%20al%20procesamiento%20de%20imagenes/5.%20Divisi%C3%B3n%20de%202%20imagenes%20con%20python)**  
<img width="454" height="407" alt="image" src="https://github.com/user-attachments/assets/6d6c78fc-da73-427e-b177-8464d0936909" />

**Descripción:**  

Este código carga dos imágenes y crea una nueva dividiendo los valores de los píxeles de la segunda imagen entre los de la primera. Sin embargo, este método es problemático y propenso a errores.

La división directa de píxeles produce una imagen con resultados poco intuitivos y es muy susceptible a errores críticos, principalmente por dos razones:

1. Error de División por Cero
Este es el problema más grave. Si cualquier píxel en la imagen (el divisor) tiene un valor de 0 (lo cual es extremadamente común en áreas negras u oscuras), el código intentará realizar una división por cero. Esto detendrá la ejecución del programa con un error (ZeroDivisionError) o generará valores infinitos (inf) que crean artefactos visuales extraños y corruptos en la imagen final.

2. Truncamiento de Decimales
La operación de división produce un resultado con decimales (un número de "punto flotante"). Sin embargo, la imagen nueva está configurada para almacenar solo enteros sin signo de 8 bits (dtype=np.uint8). Al guardar el resultado, el sistema descarta la parte decimal (trunca el número).

Ejemplo: Si un píxel en imagen1 vale 150 y en imagen vale 100.

La división matemática es: 150 / 100 = 1.5.

El valor almacenado: El .5 se descarta y el valor guardado en el píxel de la imagen nueva es simplemente 1.

Como resultado, la imagen final será extremadamente oscura, casi completamente negra, con algunos píxeles blancos o de colores brillantes dispersos. Estos pocos píxeles brillantes solo aparecerán en las áreas donde el valor del píxel en imagen1 era un múltiplo significativamente mayor que el de imagen.

Para realizar esta operación de forma segura, se debe utilizar la función de OpenCV cv2.divide(), que maneja correctamente la división por cero y escala los resultados para obtener una salida visualmente coherente.

---

**[Espejo vertical](https://github.com/Additrejo/IPN-Vision_por_computadora/tree/main/Laboratorio/Introducci%C3%B3n%20al%20procesamiento%20de%20imagenes/6.%20Espejo%20vertical)**  
<img width="454" height="414" alt="image" src="https://github.com/user-attachments/assets/6c5f5327-31d0-494a-a4f9-2a550c425d35" />

**Descripción:** 

Este código carga una imagen y la voltea verticalmente, creando un efecto de espejo a lo largo de un eje horizontal.

Importar y Cargar: Primero, importa la biblioteca OpenCV (cv2) y carga el archivo imagen1.jpg en la variable imagen.

Voltear la Imagen: La línea clave es flip0 = cv2.flip(imagen, 0).

La función cv2.flip() se usa para voltear una imagen.

El segundo argumento, el 0, le indica a la función que debe voltear la imagen verticalmente (alrededor del eje x). Esto significa que la parte de arriba de la imagen pasa a ser la de abajo y viceversa.

Mostrar el Resultado: Finalmente, cv2.imshow('Espejo vertical', flip0) crea una ventana con el título "Espejo vertical" y muestra la imagen ya volteada. El programa espera a que presiones una tecla para cerrar la ventana.

El resultado es una imagen que parece reflejada en un espejo colocado horizontalmente en el centro de la misma. La fila superior de píxeles se convierte en la última, y la última en la primera.

---

**[Espejo horizontal](https://github.com/Additrejo/IPN-Vision_por_computadora/tree/main/Laboratorio/Introducci%C3%B3n%20al%20procesamiento%20de%20imagenes/7.%20Espejo%20Horizontal)**   
<img width="458" height="412" alt="image" src="https://github.com/user-attachments/assets/3c67a290-11de-4e18-abb3-23cff7ddfcc4" />


**Descripción:** 
Este código carga una imagen y la voltea horizontalmente, creando un efecto de espejo.

¿Qué Hace el Código?
Importar y Cargar: El script importa la biblioteca OpenCV (cv2) y carga el archivo imagen1.jpg.

Voltear la Imagen: La operación central es flip_1 = cv.flip(imagen, 1).

La función cv2.flip() se utiliza para voltear una matriz (en este caso, la imagen).

El segundo argumento, el 1, le indica a la función que debe realizar un volteo horizontal (alrededor del eje vertical 'y').

Mostrar el Resultado: Finalmente, el código abre una ventana titulada "Espejo Horizontal, By:Addi Trejo" que muestra la imagen ya volteada (flip_1). La ventana permanecerá abierta hasta que el usuario presione cualquier tecla.

El resultado es una imagen que es un reflejo exacto de la original, como si se mirara en un espejo. La parte izquierda de la imagen original ahora está a la derecha, y la parte derecha está a la izquierda.

---

**[Transpuesta](https://github.com/Additrejo/IPN-Vision_por_computadora/tree/main/Laboratorio/Introducci%C3%B3n%20al%20procesamiento%20de%20imagenes/8.%20Transpuesta)**   
<img width="430" height="417" alt="image" src="https://github.com/user-attachments/assets/33f03676-7386-4d04-8d2b-272dcdd60529" />

**Descripción:** 

Este código carga una imagen y la rota 90 grados en sentido antihorario alrededor de su punto central.

¿Qué Hace el Código?
Cargar y Obtener Dimensiones: El script carga imagen1.jpg y luego obtiene su ancho (ancho) y alto (alto) usando image.shape.

Crear la Matriz de Rotación: La línea M = cv2.getRotationMatrix2D((ancho//2, alto//2), 90, 1) es la más importante.

La función cv2.getRotationMatrix2D crea una matriz de transformación que define la rotación.

(ancho//2, alto//2): Especifica que la rotación debe ocurrir alrededor del centro exacto de la imagen.

90: Es el ángulo de rotación en grados. Un valor positivo en OpenCV significa un giro en sentido antihorario.

1: Es el factor de escala. Un valor de 1 significa que la imagen no cambiará de tamaño.

Aplicar la Rotación: La función cv2.warpAffine(image, M, (ancho, alto)) toma la imagen original, le aplica la matriz de transformación M y genera la imagen rotada.

Mostrar Resultados: Finalmente, el código muestra tanto la imagen original como la imagen rotada en ventanas separadas y espera a que el usuario presione una tecla para cerrarlas.

Se mostrarán dos ventanas. Una con la imagen original y otra, titulada "Imagen Transpuesta", con la misma imagen pero girada 90 grados hacia la izquierda. Lo que antes era el borde derecho de la imagen ahora será el borde superior.

---

## Elaborado por:  
- GitHub: [AddiTrejo](https://github.com/Additrejo)

---
