#!/usr/bin/env python
# coding: utf-8

# In[9]:


get_ipython().system('pip install opencv-python')


# # 1. Import Dependencies

# In[5]:


# Import opencv
import cv2 

# Import uuid
import uuid

# Import Operating System
import os

# Import time
import time


# # 2. Define Images to Collect

# In[11]:


labels = ['endlerM', 'endlerF', 'phantom', 'shrimp']
number_imgs = 5


# # 3. Setup Folders 

# In[11]:


IMAGES_PATH = os.path.join('D:', 'Tensorflow', 'workspace', 'images', 'collectedimages')


# In[12]:


if not os.path.exists(IMAGES_PATH):
    if os.name == 'posix':
        get_ipython().system('mkdir -p {IMAGES_PATH}')
    if os.name == 'nt':
         get_ipython().system('mkdir {IMAGES_PATH}')
for label in labels:
    path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(path):
        get_ipython().system('mkdir {path}')


# # 4. Capture Images

# In[15]:


for label in labels:
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        print('Collecting image {}'.format(imgnum))
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()


# # 5. Image Labelling

# In[2]:


get_ipython().system('pip list')


# In[6]:


get_ipython().system('pip install --upgrade pyqt5 lxml')


# In[17]:


get_ipython().system('pip install --upgrade pyqt5 lxml')


# In[13]:


LABELIMG_PATH = os.path.join('Tensorflow', 'labelimg')


# In[14]:


if not os.path.exists(LABELIMG_PATH): # Clone the labelImg repository if it does not exist
    get_ipython().system('mkdir {LABELIMG_PATH}')
    get_ipython().system('git clone https://github.com/tzutalin/labelImg {LABELIMG_PATH}')


# In[15]:


import os


# In[16]:


if os.name == 'posix':
    get_ipython().system('make qt5py3')
if os.name =='nt':
    get_ipython().system('cd {LABELIMG_PATH} && pyrcc5 -o libs/resources.py resources.qrc')


# In[ ]:


get_ipython().system('cd {LABELIMG_PATH} && python labelImg.py')


# # 6. Move them into a Training and Testing Partition

# # OPTIONAL - 7. Compress them for Colab Training

# In[20]:


TRAIN_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'train')
TEST_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'test')
ARCHIVE_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'archive.tar.gz')


# In[21]:


get_ipython().system('tar -czf {ARCHIVE_PATH} {TRAIN_PATH} {TEST_PATH}')


# In[ ]:




