import cv2

video = cv2.VideoCapture("./images/f16_cut.mp4")

while (video.isOpened()) :
    check, frame = video.read()

    if check == True :
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("output", gray)
        if cv2.waitKey(30) & 0xFF == ord("e"):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()
