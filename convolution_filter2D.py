import cv2 
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread("./images/noise.png")
kernel = np.ones((6,6), np.float32)/36

convo = cv2.filter2D(img,-1,kernel)

mean = cv2.blur(img,(5,5))

blur = cv2.medianBlur(img,5)

gaussian = cv2.GaussianBlur(img,(5,5),0)

titles = ["ORIGINAL", "FILTER 2D", "MEAN", "BLUR", "GAUSSIAN"]
images = [img, convo, mean, blur, gaussian]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
