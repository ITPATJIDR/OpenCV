import cv2

img = cv2.imread("./images/f16.png")

img_resize = cv2.resize(img,(800,600))

cv2.arrowedLine(img_resize, (0,0), (100,100), (255,0,0), 5)

cv2.imshow("output", img_resize)

cv2.waitKey(0)
cv2.destroyAllWindows()
