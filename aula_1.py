import cv2
import numpy as np

# Load the image
image = cv2.imread('imagens/car.jpeg')
resize = cv2.resize(image, (0,0),fx=0.5, fy=0.5)
rotate = cv2.rotate(resize, cv2.ROTATE_90_CLOCKWISE)

# Display the original image and the processed image
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resize)
cv2.imshow('Rotated Image', rotate)

#cv2.imwrite('imagens/nova_imagem.jpeg', rotate)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
