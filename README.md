# Harris_conner_detection
Harris conner detection code using python
********************************************Harris 角点检测的python实现***************************************************
这是一个python版本的Harris角点检测代码库，它包括以下几个文件：
1、Convelution.py：这个文件实现了卷积和padding两个类，已实现图像卷积
2、filter.py：这个文件实现了空间域高斯滤波
3、NMS.py：这个文件实现了NMS类，它包括Harris中使用的像素邻域的非极大值抑制，同时，它也实现了针对bounding box的非极大值抑制已用于目标检测的复用
4、Response.py：这个文件实现两种Harris的响应函数，一种是经典的det(x1*x2)-k*(x1+x2),一种是简化版的响应函数：(dxx*dyy-dxy**2)/(dxx+dyy)
5、harris.py：这个文件实现Harris算法，它的流程是：
              （1） 计算x方向梯度
              （2） 计算y方向梯度
               (3)  对（1），（2）结果做高斯平滑
               (4)  计算相应函数值
               (5)  对（4)结果做非极大值抑制
              （6）  对（5）结果进行阈值处理
