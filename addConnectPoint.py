import cv2
import numpy
img = cv2.imread("./images/f16.png")

points = []

def clickPosition(event,x,y,flags,param) :
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,0,255),4)
        points.append((x,y))
        if len(points) >=2 :
            cv2.line(img, points[-2], points[-1], (0,255,0),5)
            print(points[1])
        cv2.imshow("output", img)


cv2.imshow("output",img)
cv2.setMouseCallback("output", clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()
