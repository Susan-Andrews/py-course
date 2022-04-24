#images used here can be varied according to the use
'''

import random
import matplotlib.pyplot as plt
account=0
x=[]
y=[]
for i in range(365):
    x.append(i+1)     # for loop start with 0.so graph begins with 1 so.i+1
    bet=random.randint(1,10)
    lucky_draw=random.randint(1,10)
    if bet==lucky_draw:
        account=account+900-100
    else:
        account=account-100  
    y.append(account)
print("total amount in account is"+str(account))    
plt.plot(x,y)  
plt.show()    
'''

#image processing using k
'''
from PIL import Image
img=Image.open("k.jpeg")
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)
transposed_img.save("newflipped.jpeg")
print("done flipping")
''' 

#image enhancement using an image     CLAHE(technique used to improve contrast of images)
import cv2
img=cv2.imread("enhance1.jpeg") # read the image
clahe=cv2.createCLAHE() #preparation for clahe
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert to gray scale image
enhance_img=clahe.apply(gray_img) #apply enhancement
cv2.imwrite("enhanced.png",enhance_img) # save it to a file
print("done enhancing")

