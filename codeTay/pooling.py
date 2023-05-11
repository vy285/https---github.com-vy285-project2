
import numpy as np
class Pooling:
    def __init__(self,allImg, widthPoo , heightPoo, stride =1):
        self.allImg = allImg
        self.widthPoo = widthPoo
        self.heightPoo = heightPoo
        self.stride = stride
    
    def hoatDong(self):
        wOld,hOld = self.allImg[0].shape
        wNew = int((wOld - self.widthPoo) / self.stride) +1
        hNew = int((hOld - self.heightPoo) / self.stride) +1
        outAllImg = []
        for a in range(len(self.allImg)):
            imgNew = np.zeros((wNew,hNew))
            for i in range(wNew):
                for j in range(hNew):
                    imgNew[i,j] = np.max(self.allImg[a,i:i+self.widthPoo,j:j+self.heightPoo])
            outAllImg.append(imgNew)
        return np.array(outAllImg)
    