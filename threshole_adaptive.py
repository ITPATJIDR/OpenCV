import cv2

img = cv2.imread("./images/map.jpg",0)

thres, result = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
result2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,1)
result3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,1)

cv2.imshow("THRESH", result)
cv2.imshow("THRESH Adaptive", result2)
cv2.imshow("THRESH Adaptive Gaussian C ", result3)
cv2.waitKey(0)
cv2.destroyAllWindows()
