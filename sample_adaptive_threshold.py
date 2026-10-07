"""比较了光照变化的图像的全局阈值和自适应阈值"""

#由于示例图片是截屏的，像素不高，所以显示的图像效果可能不好
#实际效果见"sample_threshold\3.png"

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt



img = cv.imread('sample_threshold\\2.jpg',0)
img = cv.medianBlur(img,5)
# 2. 全局阈值（作为对比组）
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# 3. 自适应均值阈值
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)
# 4. 自适应高斯阈值
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)

#5.生成对比图
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

