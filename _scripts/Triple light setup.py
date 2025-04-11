from bpy import context as C
from bpy import data as D
from mathutils import *; from math import *
import bpy


# LIGHT FOCUS: empty
bpy.ops.object.empty_add(type='PLAIN_AXES')
focus_empty = bpy.context.active_object
focus_empty.name = "Light Setup Focus"
focus_empty.location = (0, 0, 2)

# KEY LIGHT: light
bpy.ops.object.light_add(type="AREA")
key_light = C.active_object
key_light.name = "Key Light"
key_light.data.energy = 1000
key_light.data.size = 5
key_light.location = (5, -5, 5)

# FILL LIGHT: light
bpy.ops.object.light_add(type='AREA')
fill_light = bpy.context.active_object
fill_light.name = "Fill Light"
fill_light.data.energy = 800
fill_light.data.size = 5
fill_light.location = (-5, -5, 5)

# BACK LIGHT: light
bpy.ops.object.light_add(type = 'AREA')
back_light = bpy.context.active_object
back_light.name = "Back Light"
back_light.data.energy = 200
back_light.data.size = 5
back_light.location = (0, 5, 5)

# Add `Track To` constraint to each light, targeting the focus empty
for light in [key_light, fill_light, back_light]:
    constraint = light.constraints.new(type='TRACK_TO')
    constraint.target = focus_empty
    

# Create a new collection named "Light Setup"
collection = bpy.data.collections.new("Light Setup")
bpy.context.scene.collection.children.link(collection)

# Move the lights and focus empty to the new collection
for obj in [key_light, fill_light, back_light, focus_empty]:
    bpy.context.scene.collection.objects.unlink(obj)
    collection.objects.link(obj)