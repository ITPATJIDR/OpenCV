import cv2

img = cv2.imread("./images/f16.png")
thresh, result = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
thresh, result2 = cv2.threshold(img,128,255,cv2.THRESH_BINARY_INV)
thresh, result3 = cv2.threshold(img,128,255,cv2.THRESH_TRUNC)
thresh, result4 = cv2.threshold(img,128,255,cv2.THRESH_TOZERO)
thresh, result5 = cv2.threshold(img,128,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("Original", img)
cv2.imshow("Result", result)
cv2.imshow("Result2", result2)
cv2.imshow("Result3", result3)
cv2.imshow("Result4", result4)
cv2.imshow("Result5", result5)

cv2.waitKey(0)
cv2.destroyAllWindows()
