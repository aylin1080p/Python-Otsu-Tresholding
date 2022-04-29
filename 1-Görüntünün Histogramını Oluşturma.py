#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[5]:


## Histogram oluşturma

import cv2 
import numpy as np

image_name = "sun.jpg" # Histogramı oluşturulacak görüntünün değişkene atanması 
img = cv2.imread (image_name) # imread komutu ile görüntü okuma 
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) ## cvtColor komutu ile renk dönüşümü

size_y = img.shape[0] # y koordinatına bir dizi tanımlanıp shape ile numpy dizisi haline getiriliyor 
size_x = img.shape[1]

flattened = img.reshape([size_x*size_y]) # Dizinin yeniden şekillendirilmesi, düzleştirilmesi

#histogram oluşturma için veri görselleştirme kütüphanesi projeye dahil edilir. 
from matplotlib import pyplot as plt # pylot projeye dahil edilir ailas plt

plt.title("Görüntünün Farklı Yayılımlarda Histogramlarının oluşturulması") 
plt.xlabel("x Eksenine Yayılım Gösteren 256 Kanallı Renk Dağılımı") 
plt.ylabel("y Eksenine Yayılım Gösteren Piksel Miktarları")

rhist,_ ,_ = plt.hist(flattened, bins = 256)# hist komutu ile her bir piksel için sayı değeri döndürülür

# bins = 256 ile x ekseninin 256 ayrı alana ayrılması işlevi sağlanır. 

# bins ile farklı histogram görüntüleri elde edilebilir.  
# plt.show() görüntüyü ekrana basar.


# In[ ]:





# In[ ]:




