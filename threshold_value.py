import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./images/f16.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresh_value = [50, 100, 130, 189, 242]
plt.subplot(231,xticks=[],yticks=[])
plt.title("Original")
plt.imshow(img,cmap="gray")

for i in range(len(thresh_value)):
    thresh,result = cv2.threshold(img,thresh_value[i],255,cv2.THRESH_BINARY)
    plt.subplot(232+i)
    plt.title("%d"%thresh_value[i])
    plt.imshow(result,cmap="gray")
    plt.xticks([])
    plt.yticks([])
    
plt.show()
