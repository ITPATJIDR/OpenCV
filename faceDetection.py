import cv2

img = cv2.imread("./images/human.jpg")
img = cv2.resize(img, (500,700))

face_cascade = cv2.CascadeClassifier("./images/haarcascade_frontalface_default.xml")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

scaleFactor = 1.1 # scale down picture
minNeighber = 3 # how much to detect face 
face_detect = face_cascade.detectMultiScale(gray,scaleFactor, minNeighber)

for (x,y,w,h) in face_detect:
    print(x,y,w,h)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

cv2.imshow("original", img)
#cv2.imshow("result", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
