import numpy as np
import cv2
import matplotlib.pyplot as plt


class Conv(object):
    def __init__(self,kernel,padding=None):
        self.padding=padding
        self.kernel=np.array(kernel)
        self.w_kernel,self.h_kernel=self.kernel.shape
    def __call__(self,img):
        if(self.padding!=None):
            img=Padding(self.w_kernel,self.h_kernel)(img)
            # print(img.shape)
        if(len(img.shape)==2):
            return self.filter_gray(img)
        else:
            return self.filter_color(img)

    def filter_gray(self,img):
        w_img,h_img=img.shape
        filtered_w,filtered_h=w_img-self.w_kernel+1,h_img-self.h_kernel+1
        filtered_array=np.zeros((filtered_w,filtered_h))
        for i in range(filtered_w):
            for j in range(filtered_h):
                slice_img=img[i:i+self.w_kernel,j:j+self.h_kernel]
                filtered_array[i,j]=np.sum(slice_img*self.kernel)
        return filtered_array

    def filter_color(self,img):
        c=img.shape[-1]
        for i in range(c):
            img[:,:,i]=self.filter_gray(img[:,:,i])
        return img

class Padding(object):
    def __init__(self,kernel_w,kernel_h,mode="constant",constant_values=(0,0)):
        self.mode=mode
        self.kernel_w=kernel_w
        self.kernel_h=kernel_h
        self.constant_values=constant_values
    def __call__(self,img):
        padding_w,padding_h=self.kernel_w//2,self.kernel_h//2
        if(self.mode=="constant"):
            return np.pad(img, ((padding_h, padding_h), (padding_w, padding_w)), 'constant',constant_values=self.constant_values)
        else:
            return np.pad(img, ((padding_h, padding_h), (padding_w, padding_w)), self.mode)

if __name__=="__main__":

    img=cv2.imread("2.jpg",0)
    # print(img.shape)
    # padding=Padding(3,3,"mean")
    # img=padding(img)
    # print(img.shape)
    filter=Conv(kernel=[[-1,-1,-1],[0,0,0],[1,1,1]],padding=None)
    filtered_img=filter(img)
    print(filtered_img.shape)
    plt.imshow(filtered_img)
    plt.show()








