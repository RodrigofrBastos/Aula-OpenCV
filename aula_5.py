import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_green = np.array([45, 50, 50])
    upper_green = np.array([75, 255, 255])
    
    lower_red = np.array([0, 100, 100]) 
    upper_red = np.array([10, 255, 255]) 

    lower_orange = np.array([11, 100, 100]) 
    upper_orange = np.array([25, 255, 255]) 

    lower_blue = np.array([90, 100, 100]) 
    upper_blue = np.array([130, 255, 255]) 

    lower_white = np.array([0, 0, 200]) 
    upper_white = np.array([180, 30, 255]) 

    lower_yellow = np.array([20, 100, 100]) 
    upper_yellow = np.array([35, 255, 255]) 

    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    orange_mask = cv2.inRange(hsv, lower_orange, upper_orange)
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    white_mask = cv2.inRange(hsv, lower_white, upper_white)
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    
    #horizontal_concat = np.hstack((red_mask, orange_mask, blue_mask, white_mask, yellow_mask))


    red_pixels = cv2.bitwise_and(frame, frame, mask=red_mask)
    orange_pixels = cv2.bitwise_and(frame, frame, mask=orange_mask)
    blue_pixels = cv2.bitwise_and(frame, frame, mask=blue_mask)
    white_pixels = cv2.bitwise_and(frame, frame, mask=white_mask)
    yellow_pixels = cv2.bitwise_and(frame, frame, mask=yellow_mask)
    green_pixels = cv2.bitwise_and(frame, frame, mask=green_mask)
    
    horizontal_concat = np.hstack((red_pixels,orange_pixels,blue_pixels))
    horizontal_concat_2 = np.hstack((white_pixels,yellow_pixels,green_pixels))
    
    cv2.imshow('result', horizontal_concat)
    cv2.imshow('result2', horizontal_concat_2)
    #cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()