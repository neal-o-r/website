import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# Read the image
im = Image.open("image.png").convert('RGBA')
p = np.array(im) # convert it to a numpy array

plt.figure()
plt.imshow(im, origin='upper')


r = p[:,:,0].flatten() # flatten them into 1-d arrays
g = p[:,:,1].flatten()
b = p[:,:,2].flatten()
l = p[:,:,3].flatten()

indices = np.argsort( g ) # generate the sort indices

r_sort = np.zeros(len(r))

g_sort = np.zeros(len(r))
b_sort = np.zeros(len(r))
l_sort = np.zeros(len(r)) #r_sort

for index, value in enumerate(indices):

     r_sort[index] = r[value] # sort all of the array by the indices of one colour
     g_sort[index] = g[value]
     b_sort[index] = b[value]
     l_sort[index] = l[value]


sorted_array = np.zeros((p.shape[0], p.shape[1], p.shape[2]),dtype=np.dtype('uint8'))

sorted_array[:,:,0] = np.reshape(r_sort, (p.shape[0], p.shape[1]))
sorted_array[:,:,1] = np.reshape(g_sort, (p.shape[0], p.shape[1]))
sorted_array[:,:,2] = np.reshape(b_sort, (p.shape[0], p.shape[1]))
sorted_array[:,:,3] = np.reshape(l_sort, (p.shape[0], p.shape[1]))

# re-shape and turn it back into an image
sorted_image = Image.fromarray(sorted_array, mode='RGBA')

plt.figure()
plt.imshow(sorted_image, origin='upper')

plt.show()
