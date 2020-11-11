import numpy as np
from vedo import *  # pip install vedo
data = np.load('img.npz')
img1 = data['img1']
point = [39, 105, 109]
img2 = data['img2']

vol1 = Volume(img1).isosurface(1).c('b').alpha(0.3)
vol2 = Volume(img2).isosurface(1).c('r').alpha(0.3)
p = Point(pos=[point[2], point[1], point[0]])
show(vol1, p, at=0, N=2)
show(vol2, at=1, interactive=True)