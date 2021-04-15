import cv2
import numpy as np

img = cv2.imread("ball.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 
blue_low = np.array([100,50,50])
blue_high = np.array([150,255,255])

mask = cv2.inRange(hsv, blue_low, blue_high)

output = cv2.bitwise_and(img, img, mask= mask)


cv2.imshow("image", img)
cv2.imshow("mask", mask)
cv2.imshow("output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
