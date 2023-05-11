import numpy as np

class Relu:
    def __init__(self,allImg):
        self.allImg = allImg
    def hoatDong(self):
        print(type(self.allImg))
        print(self.allImg[0,0,0])
        print(self.allImg[0].shape)
        w,h = self.allImg[0].shape
        for a in range(len(self.allImg)):
            for i in range(w):
                for j in range(h):
                    # self.allImg[a,i,j] = max(0,self.allImg[a,i,j])
                    self.allImg[a,i,j] =0.1*self.allImg[a,i,j] if self.allImg[a,i,j] < 0 else self.allImg[a,i,j]
        return np.array(self.allImg)