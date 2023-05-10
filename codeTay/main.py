import cv2
import numpy as np
import matplotlib.pyplot as plt
from Conv import Convolution 

image = cv2.imread("codeTay/vy.jpg",0)
print(image.shape)

conv = Convolution(image,3,3,3)
allOutImg =conv.allOutImg()

fig,axi = plt.subplots(nrows =2,ncols =3 ,figsize=(5,10))
axi[0,1].imshow(image,cmap='gray')
axi[0,1].set_title('cu')
axi[1,0].imshow(allOutImg[0],cmap='gray')
axi[1,1].imshow(allOutImg[1],cmap='gray')

axi[1,2].imshow(allOutImg[2],cmap='gray')

plt.show()
plt.axis(False)


 