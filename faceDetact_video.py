import cv2

cap = cv2.VideoCapture("./images/Mark.mp4")
face_cascade = cv2.CascadeClassifier("./images/haarcascade_frontalface_default.xml")

while (cap.isOpened()):
    check, frame = cap.read()
    if check == True:
        gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        scaleFactor = 1.1 # scale down picture
        minNeighber = 5 # how much to detect face 
        face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor, minNeighber)
                
        for (x,y,w,h) in face_detect:
            print(x,y,w,h)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
            cv2.imshow("Output",frame)

        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
