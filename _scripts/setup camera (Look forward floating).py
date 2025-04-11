from bpy import data as D
from mathutils import *; from math import *

camera = D.objects["Camera"]

camera.location = Vector((0, -5, 5))

# WTF
camera.rotation_euler = Euler((1.5707963705062866, 0.0, 0.0), 'XYZ')