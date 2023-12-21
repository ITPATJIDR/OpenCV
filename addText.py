import cv2

img = cv2.imread("./images/f16.png")

img_resize = cv2.resize(img,(700,700))

cv2.putText(img_resize,"HI", (150,200),cv2.FONT_ITALIC,2.5,(0,32,44),5)

cv2.imshow("output", img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
