# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 20:13:44 2021

@author: WY
"""

import os
import cv2
import numpy as np
from PIL import Image
from glob import glob

base_dir = os.path.dirname(os.path.abspath(__file__))

files = glob(os.path.join(base_dir, 'img_process/*.jpg'))

for file in files:
    img = cv2.imread(file, cv2.IMREAD_COLOR)
    filepath, filename = os.path.split(file)
    name, extend = os.path.splitext(filename)
    data = np.array(img)
    
# =============================================================================
#     for i in range(0, 3072, 1024):
#         sub_data = data[384:1408,i:(i+2048)]
#         cv2.imwrite(os.path.join(os.path.join(base_dir, 'imgs/test_imgs'), name + '_%d.jpg'%(int(i/1024))), sub_data)
# =============================================================================
    k = 0
    for i in range(1024, 2049, 1024):
        for j in range(0, 7168, 1024):
            sub_data = data[i:(i+1024),j:(j+2048)]
            cv2.imwrite(os.path.join(os.path.join(base_dir, 'imgs/test_imgs'), name + '_%d.jpg'%(k)), sub_data)
            k += 1
# =============================================================================
# cv2.imshow('image',img)

# cv2.waitKey(0) #参数为0表示无限等待
# #cv2.destroyWindow() #销毁所有窗口
# cv2.destroyWindow('image') #销毁特定窗口
# =============================================================================
