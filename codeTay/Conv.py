import numpy as np
# tinh tich chap
class Convolution:
    def __init__(self,inpImg, soChieu , widthFilter, heightFilter , stride_width = 1 , stride_height =1 , p=0):
        self.inpImg = inpImg
        self.soChieu = soChieu
        self.widthFilter = widthFilter
        self.heightFilter = heightFilter
        self.stride_width = stride_width
        self.stride_height = stride_height
        self.p = p
    
    def hoatDong(self):
        wOld , hOld = self.inpImg.shape
        wNew = int((wOld - self.widthFilter + 2* self.p)/self.stride_width +1)
        hNew = int((hOld - self.heightFilter + 2* self.p)/self.stride_height + 1)
        
        allImg = []
        for i in range(self.soChieu):
            outImg = np.zeros((wNew, hNew))
            filter = np.random.randn(self.widthFilter, self.heightFilter)
            print(filter)

            # print(outImg)
            for i in range(wNew):
                for j in range(hNew):
                    outImg[i,j] = np.sum(self.inpImg[i:i+self.widthFilter,j:j+self.widthFilter]*filter)
            allImg.append(outImg)
                
        return np.array(allImg)
    
    