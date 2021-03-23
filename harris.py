import numpy as np
import cv2
from Convelution import Conv
from Response import Response_Func
from NMS import NMS
from filter import Gauss_filter



class Harris(object):
    def __init__(self,threshold=0.01):
        self.dx_kernel=[[-1, -1, -1], [0, 0, 0], [1, 1, 1]]
        self.dy_kernel=[[-1,0,1],[-1,0,1],[-1,0,1]]
        self.threshold=threshold
    def __call__(self, img):
        dx_filter = Conv(kernel=self.dx_kernel, padding=None)
        dy_filter = Conv(kernel=self.dy_kernel, padding=None)
        dx = dx_filter(img)
        dx = Gauss_filter()(dx)
        dy = dy_filter(img)
        dy = Gauss_filter()(dy)
        dxy = dx*dy
        response=Response_Func()(dx,dy,dxy)
        nmsed_response=NMS()(response)
        max_response=np.max(nmsed_response)
        nmsed_response[nmsed_response>=self.threshold*max_response]=255
        nmsed_response[nmsed_response<self.threshold*max_response]=0
        return nmsed_response






