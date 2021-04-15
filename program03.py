import cv2

img = cv2.imread("mandrill.jpg")

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("image", img2[:,:,2])
cv2.waitKey(0)
cv2.destroyWindow("image")
