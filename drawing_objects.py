import cv2
import numpy as np

# Create a black image
image = np.zeros((400, 400, 3), dtype=np.uint8)

# Draw a line
cv2.line(image, (50, 50), (350, 50), (0, 0, 255), 3)

# Draw a rectangle
cv2.rectangle(image, (50, 100), (350, 200), (0, 255, 0), 2)

# Draw a circle
cv2.circle(image, (200, 300), 50, (255, 0, 0), -1)

# Draw an ellipse
cv2.ellipse(image, (200, 200), (100, 50), 30, 0, 270, (255, 255, 0), 2)

# Put text on the image
cv2.putText(image, 'OpenCV', (120, 380), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Display the image
cv2.imshow('Image', image)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

