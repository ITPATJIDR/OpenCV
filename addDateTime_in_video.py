import cv2
import datetime

video = cv2.VideoCapture("./images/f16_cut.mp4")

while (video.isOpened()) :
    check, frame = video.read()

    if check == True :
        currentDate = datetime.datetime.now()
        cv2.putText(frame,str(currentDate), (10,30),cv2.FONT_HERSHEY_PLAIN,0.9,(0,0,0),2)
        cv2.imshow("output", frame)
        if cv2.waitKey(30) & 0xFF == ord("e"):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()
