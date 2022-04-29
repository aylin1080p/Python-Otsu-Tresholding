#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
from matplotlib import pyplot as plt
img = cv2.imread("brain.jpg") # oku
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # bgr den grayscale yap

im1 = img.copy()
ret,im1 = cv2.threshold(im1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # imge otsu thresholding e maruz kaliyor

plt.figure(1)
plt.subplot(121)
plt.imshow(img,cmap='gray')

plt.subplot(122)
plt.imshow(im1,cmap='gray')
plt.show() # goster


# In[ ]:





# In[ ]:




