import cv2

img = cv2.imread("mandrill.jpg")

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

img2[:,:,1] = 255

img3 = cv2.cvtColor(img2, cv2.COLOR_HSV2BGR)

cv2.imshow("image", img3)
cv2.waitKey(0)
cv2.destroyWindow("image")
