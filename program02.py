import cv2

img = cv2.imread("mandrill.jpg")

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

img2 = b * 0.1 + g * 0.6 + r * 0.3

cv2.imshow("image", img2.astype("uint8"))
cv2.waitKey(0)
cv2.destroyWindow("image")
