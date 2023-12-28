import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./images/f16.png")
thresh, result = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
thresh, result2 = cv2.threshold(img,128,255,cv2.THRESH_BINARY_INV)
thresh, result3 = cv2.threshold(img,128,255,cv2.THRESH_TRUNC)
thresh, result4 = cv2.threshold(img,128,255,cv2.THRESH_TOZERO)
thresh, result5 = cv2.threshold(img,128,255,cv2.THRESH_TOZERO_INV)

images = [img,result,result2,result3,result4,result5]
title = ["Original","BIN","BIN_INV","TRUNC","THRESH_TOZERO","THRESH_TOZERO_INV"]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

