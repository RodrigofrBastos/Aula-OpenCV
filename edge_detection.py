import cv2
import numpy as np

# Load the image
image = cv2.imread('imagens/i1583076866325242.jpeg')
cv2.imshow('Original Image', image)
# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform edge detection using the Canny edge detection algorithm
edges = cv2.Canny(blur, 50, 150)

# Encontra os contornos na imagem
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

cv2.imshow('Contours', image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()