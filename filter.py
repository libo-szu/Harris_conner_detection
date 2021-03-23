import numpy as np
from Convelution  import Conv

class Gauss_filter(object):
    def __init__(self,kernel_w=3,kernel_h=3,sigma=0.01):
        self.kernel_w=kernel_w
        self.kernel_h=kernel_h
        self.sigma=sigma
        self.kernel=np.zeros((self.kernel_w,self.kernel_h))
        for i in range(self.kernel_w):
            for j in range(self.kernel_h):
                self.kernel[i, j] = np.exp(
                    ((i - self.kernel_w // 2) ** 2 + (j - self.kernel_h // 2) ** 2) / 2 * self.sigma)
        self.kernel=self.kernel/np.sum(self.kernel)
    def __call__(self,img):
        filter_conv=Conv(self.kernel)
        return filter_conv(img)




