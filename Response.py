import numpy as np
import os

class Response_Func(object):
    def __init__(self,mode="classic",k=0.04):
        self.mode=mode
        self.k=k

    def __call__(self, Ixx,Iyy,Ixy):
        if(self.mode=="classic"):
            return self.compute_classic_response(Ixx,Iyy,Ixy)
        else:
            return self.compute_imporve_response(Ixx,Iyy,Ixy)
    def compute_classic_response(self,Ixx,Iyy,Ixy):
        Idet=Ixx*Iyy - Ixy**2
        Itrans=Ixx + Iyy
        return Idet-self.k*(Itrans**2)
    def compute_imporve_response(self,Ixx,Iyy,Ixy):
        return (Ixx*Iyy-Ixy**2)/(Ixx+Iyy+0.000000001)

