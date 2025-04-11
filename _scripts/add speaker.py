import bpy

bpy.ops.object.speaker_add(align='WORLD', location=(0, 0, 5), scale=(1, 1, 1))
bpy.ops.object.constraint_add(type='TRACK_TO')
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Camera"]
bpy.context.object.data.attenuation = 0

