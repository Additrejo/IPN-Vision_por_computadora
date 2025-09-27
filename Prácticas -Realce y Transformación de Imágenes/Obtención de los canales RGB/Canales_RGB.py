import cv2 


img = cv2.imread('C:\Users\addi_\OneDrive\Documentos\IPN\9no_Semestre\Visión_por_computadora\2do_bloque\Prácticas\Obtención_de_los_canales_RGB')
img = np.float_(img)
x, y, ch = img.shape
blue = np.zeros((x, y, ch), dtype=float)
green = np.zeros((x, y, ch), dtype=float)
red = np.zeros((x, y, ch), dtype=float)

for j in range(x):
    for k in range(y):
        blue [j, k, 0] = img [j, k, 0] 
    
for j in range(x):
    for k in range(y):
        green [j, k, 1] = img [j, k, 1] 
        
for j in range(x):
    for k in range(y):
        red [j, k, 2] = img [j, k, 2] 
            
            
result = np.uint8(img)
cv2.imshow("Original", result)

resultB = np.uint8(blue)
cv2.imshow("Blue",resultB)

resultG = np.uint8(green)
cv2.imshow("Green",resultG)

resultR = np.uint8(red)
cv2.imshow("Red",resultR)

cv2.waitKey(0)
cv2.destroyAllWindows()