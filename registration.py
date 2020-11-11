import numpy as np
from vedo import *  # pip install vedo
data = np.load('img.npz')
img1 = data['img1']
point = [39, 105, 109]
img2 = data['img2']

from dipy.align.imwarp import SymmetricDiffeomorphicRegistration
from dipy.align.imwarp import DiffeomorphicMap
from dipy.align.metrics import CCMetric, SSDMetric
static, moving = img2, img1

metric = SSDMetric(3)
level_iters = [100, 20, 10]
sdr = SymmetricDiffeomorphicRegistration(metric, level_iters, ss_sigma_factor=2.5)
static_affine = np.eye(4)
moving_affine = np.eye(4)
pre_align = np.eye(4)


mapping = sdr.optimize(static, moving, static_affine, moving_affine, pre_align)
warped_moving = mapping.transform(moving)

newX = point[0] + mapping.forward[point[0], point[1], point[2]][0]
newY = point[1] + mapping.forward[point[0], point[1], point[2]][1]
newZ = point[2] + mapping.forward[point[0], point[1], point[2]][2]
p = Point(pos=[newZ, newY, newX])

vol1 = Volume((warped_moving>0.5).astype(np.int)).isosurface(1).c('b').alpha(0.3)
vol2 = Volume(img2).isosurface(1).c('r').alpha(0.3)
p = Point(pos=[point[2], point[1], point[0]])
show(vol1, p, at=0, N=2)
show(vol2, at=1, interactive=True)