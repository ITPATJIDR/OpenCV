import cv2

img = cv2.imread("./images/f16.png")

img_resize = cv2.resize(img,(700,700))

cv2.circle(img_resize,(200,300),20, (0,10,124),5)

cv2.imshow("output", img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
