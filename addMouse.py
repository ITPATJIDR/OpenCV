import cv2
img = cv2.imread("./images/f16.png")

def clickPosition(event,x,y,flags,param) :
    if event == cv2.EVENT_LBUTTONDOWN:
        x_y = str(x) + "," + str(y)
        cv2.putText(img,x_y, (x,y), cv2.FONT_HERSHEY_PLAIN,2,(255,0,0), cv2.LINE_4)
        cv2.imshow("output",img)


cv2.imshow("output",img)
cv2.setMouseCallback("output", clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()
