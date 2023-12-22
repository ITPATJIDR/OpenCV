import cv2
import numpy
img = cv2.imread("./images/f16.png")

def clickPosition(event,x,y,flags,param) :
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        img_color = numpy.zeros([300,300,3], numpy.uint8)
        img_color[:] = [blue, green, red]
        cv2.imshow("result",img_color)


cv2.imshow("output",img)
cv2.setMouseCallback("output", clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()

