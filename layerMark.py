import cv2
import numpy


while True :

    img_color = cv2.imread("./images/color2.jpg")
    img_resize = cv2.resize(img_color,(400,400))

    lower = numpy.array([46,154,49])
    upper = numpy.array([114,227,127])

    mask = cv2.inRange(img_resize,lower, upper)
    result = cv2.bitwise_and(img_resize,img_resize,mask=mask)
    if cv2.waitKey(0) & 0xFF == ord("e"): 
        break

    cv2.imshow("Original", img_resize)
    cv2.imshow("Mask", mask)
    cv2.imshow("result", result)

cv2.destroyAllWindows()

