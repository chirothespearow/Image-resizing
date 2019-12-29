from PIL import Image
import math
import os
i=input('Please enter the directory address of the image:')    
im=Image.open(i)
width, height = im.size
h=300
w=(width*300)/height
if w>400:
	w=400
newsize=(int(w),h)
im1=im.resize(newsize)
os.mkdir('new_image')
os.chdir('new_image')
im1=im1.save('neww.png')
