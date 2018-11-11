from visual import *

from Bone import Bone

length = 0
height = 0
width = 0

size = 12

#Ball red of center
sphere(pos=vector(0, 0, -1),
       radius=1,
       color=color.red)

osso = Bone(size)
osso.setVector(1, height, width)
osso.generate()