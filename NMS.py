import numpy as np


class NMS(object):
    def __init__(self,mode="pixes",size=3,threshold=None):
        self.mode=mode
        self.size=size
        self.threshold=threshold
    def __call__(self, img,scores=None):
        if(self.mode=="pixes"):
            return self.nms_pixes(img)
    def nms_pixes(self, img):
        w_img, h_img = img.shape
        filtered_w, filtered_h = w_img - self.size + 1, h_img - self.size + 1
        filtered_array = np.zeros((filtered_w, filtered_h))
        for i in range(filtered_w):
            for j in range(filtered_h):
                slice_img = img[i:i + self.size, j:j + self.size]
                if(img[i,j]==np.max(slice_img)):
                    filtered_array[i,j]=255
        return filtered_array
    def nms_bboxes(self,bboxes,scores):
        bboxes=np.array(bboxes)
        scores=np.array(scores)
        nmsed_bboxes=[]
        index_scores=np.argsort(scores)
        nmsed_bboxes.append(bboxes[index_scores[0]])
        while(len(index_scores)>0):
            nmsed_bboxes.append(bboxes[index_scores[0]])
            index_scores = index_scores[1:]
            index_scores1=index_scores.copy()
            for i,item in enumerate(index_scores1):
                iou=self.compute_iou(nmsed_bboxes[-1],bboxes[item])
                if(iou>self.threshold):
                    index_scores=np.delete(index_scores,i)
        return  np.array(nmsed_bboxes)

    def compute_iou(self,bbox1,bbox2):
        assert len(bbox1)!=4,"length of bbox1 != 4"
        assert len(bbox2)!=4,"length of bbox2 != 4"
        area1=(bbox1[3]-bbox1[1])*(bbox1[2]-bbox1[1])
        area2=(bbox2[3]-bbox2[1])*(bbox2[2]-bbox2[1])
        left_x=max(bbox1[0],bbox2[0])
        left_y=max(bbox1[1],bbox2[1])
        right_x=min(bbox1[2],bbox2[2])
        right_y=min(bbox1[3],bbox2[3])
        if(left_x >= right_x or left_y >= right_y):
            return 0
        else:
            intersetion=(right_y-left_y)*(right_x-left_x)
            return intersetion/(area2+area1-intersetion)