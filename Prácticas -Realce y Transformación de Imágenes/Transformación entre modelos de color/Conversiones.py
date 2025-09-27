import cv2
import numpy as np
from matplotlib import pyplot as plt

# ------------------------------------------------------------------------
#                              DE RGB A CMY
# ------------------------------------------------------------------------

ImagenOriginal = cv2.imread('C:\\Users\\addi_\\OneDrive\\Escritorio\\sinus_iridium.jpg')
(B, G, R) = cv2.split(ImagenOriginal)
zeros = np.zeros(ImagenOriginal.shape[:2], dtype="uint8")

M = 1-(G/255)
Y = 1-(B/255)
C = 1-(R/255)

ImagenCMY = cv2.merge([C, M, Y])
#cv2.imshow('Imagen Original', ImagenOriginal)
#cv2.imshow('Canal C-CMY', cv2.merge([B, G, zeros]))
#cv2.imshow('Canal M-CMY', cv2.merge([B, zeros, R]))
#cv2.imshow('Canal Y-CMY', cv2.merge([zeros, G, R]))
#cv2.imshow('Imagen CMY', ImagenCMY)
#                                                                        5 imágenes
cv2.imwrite('Imagen CMY.jpg', ImagenCMY)
cv2.imwrite('Canal C.jpg', cv2.merge([B, G, zeros]))
cv2.imwrite('Canal M.jpg', cv2.merge([B, zeros, R]))
cv2.imwrite('Canal Y.jpg', cv2.merge([zeros, G, R]))

#cv2.waitKey(0)
#cv2.destroyAllWindows()

# ------------------------------------------------------------------------
#                               DE RGB A HSI
# ------------------------------------------------------------------------

zeros = np.zeros(ImagenOriginal.shape[:2], dtype="uint8")
ImagenHSI = cv2.cvtColor(ImagenOriginal, cv2.COLOR_RGB2HSV_FULL)

(H, S, I) = cv2.split(ImagenHSI)
#cv2.imshow('IMAGEN DUDA', cv2.merge([H, S, I]))
#cv2.imshow('Canal H', cv2.merge([H, zeros, zeros]))
#cv2.imshow('Canal S', cv2.merge([zeros, S, zeros]))
#cv2.imshow('Canal I', cv2.merge([zeros, zeros, I]))
#cv2.imshow('Imagen HSI', ImagenHSI)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# ------------------------------------------------------------------------
#                               DE RGB A HSV
# ------------------------------------------------------------------------

#ImagenOriginal = cv2.imread('C:\\Users\\addi_\\OneDrive\\Escritorio\\sinus_iridium.jpg')
#zeros = np.zeros(ImagenOriginal.shape[:2], dtype="uint8")
#ImagenHSV = cv2.cvtColor(ImagenOriginal, cv2.COLOR_BGR2HSV)

#(H, S, V) = cv2.split(ImagenHSV)
#cv2.imshow('IMAGEN DUDA', cv2.merge([H, S, V]))
#cv2.imshow('Canal H', cv2.merge([H, zeros, zeros]))
#cv2.imshow('Canal S', cv2.merge([zeros, S, zeros]))
#cv2.imshow('Canal V', cv2.merge([zeros, zeros, V]))
#cv2.imshow('Imagen HSV', ImagenHSV)
#                                                                        15 imágenes
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# ------------------------------------------------------------------------
#                        DE RGB A ESCALA DE GRISES
# ------------------------------------------------------------------------



#(R, G, B) = ImagenOriginal[:, :,0], ImagenOriginal[:, :, 1], ImagenOriginal[:, :, 2]
#EscGrises = 0.2989 * R + 0.5870 * G + 0.1140 * B
#plt.imshow(EscGrises, cmap='gray')
#                                                                       17 imágenes
#cv2.imwrite('C:\\Users\\addi_\\OneDrive\\Escritorio\\sinus_iridium.jpg', EscGrises)
#plt.show()


# ------------------------------------------------------------------------
#                                  Y Cb Cr
# ------------------------------------------------------------------------


(B, G, R) = cv2.split(ImagenOriginal)
zeros = np.zeros(ImagenOriginal.shape[:5], dtype="uint8")

Y = 16+((65.738/256)*R)+((129.057/256)*G)+((25.064/256)*B)
CB = 128-((37.945/256)*R)-((74.494/256)*G)+((112.439/256)*B)
CR = 286+((112.439/256)*R)-((94.154/256)*G)-((18.285/256)*B)
Y = Y/255
CB = CB/255
CR=CR/255


ImagenYCbCr = cv2.cvtColor(ImagenOriginal, cv2.COLOR_RGB2YCrCb)

cv2.imshow('Imagen YCbCr', ImagenYCbCr)
cv2.imshow('Y', Y)
cv2.imshow('Cb', CB)
cv2.imshow('Cr', CR)
#                                                                        19 imágenes
cv2.imwrite('Imagen YCbCr.jpg', ImagenYCbCr)

cv2.waitKey(0)
cv2.destroyAllWindows()


# ------------------------ C M Y K ------------------------

B, G, R = ImagenOriginal[:, :, 0], ImagenOriginal[:,
                                                  :, 1], ImagenOriginal[:, :, 2]
zeros = np.zeros(ImagenOriginal.shape[:5], dtype="uint8")

B_ = np.copy(B)
G_ = np.copy(G)
R_ = np.copy(R)

K = zeros
C = zeros
M = zeros
Y = zeros

K = min(C, M, Y)
Y = (1-(B/255)-K)/(1-K)
M = (1-(G/255)-K)/(1-K)
C = (1-(R/255)-K)/(1-K)

ImagenCMYK = cv2.merge([K, C, M, Y])

#cv2.imshow('Imagen C-CMYK', cv2.merge([B, G, zeros, zeros]))
#cv2.imshow('Imagen M-CMYK', cv2.merge([B, zeros, R, zeros]))
#cv2.imshow('Imagen Y-CMYK', cv2.merge([zeros, G, R, zeros]))
#cv2.imshow('Imagen K-CMYK', cv2.merge([zeros, G, R, zeros]))
#cv2.imshow('Imagen CMYK', ImagenCMYK)
#                                                                        25 imágenes
cv2.imwrite('Imagen CMYK.jpg', ImagenCMYK)



cv2.waitKey(0)
cv2.destroyAllWindows()
