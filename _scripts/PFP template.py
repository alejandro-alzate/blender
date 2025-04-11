import bpy

bpy.ops.mesh.primitive_circle_add(radius=1, enter_editmode=False, align='WORLD', location=(0, -0.1, 0), scale=(0.5, 0.5, 0.5))
obj = bpy.context.active_object
obj.rotation_euler = (-1.5708, 1.6581, -3.1416)  # -90°, 95°, -180° in radians
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.edge_face_add()
bpy.ops.object.editmode_toggle()
obj.name = "ProfilePicture"

# Create material and setup nodes 
mat = bpy.data.materials.new(name="Material")
mat.use_nodes = True
mat.blend_method = 'BLEND'
nodes = mat.node_tree.nodes
links = mat.node_tree.links
nodes.clear()

# Create nodes
output = nodes.new(type='ShaderNodeOutputMaterial')
output.location = (700, 200)
output.hide = True

mix_shader = nodes.new(type='ShaderNodeMixShader')
mix_shader.location = (500, 200)
mix_shader.hide = True

transparent = nodes.new(type='ShaderNodeBsdfTransparent')
transparent.location = (300, 150)
transparent.hide = True

emission = nodes.new(type='ShaderNodeEmission')
emission.location = (300, 250)
emission.hide = True

tex_image = nodes.new(type='ShaderNodeTexImage')
tex_image.location = (0, 250)
tex_image.interpolation = 'Closest'

mapping = nodes.new(type='ShaderNodeMapping')
mapping.location = (-300, 250)
mapping.hide = True

tex_coord = nodes.new(type='ShaderNodeTexCoord')
tex_coord.location = (-600, 250)
tex_coord.hide = True

# Create links
links.new(tex_coord.outputs[2], mapping.inputs[0])
links.new(mapping.outputs[0], tex_image.inputs[0])
links.new(tex_image.outputs[0], emission.inputs[0])
links.new(tex_image.outputs[1], mix_shader.inputs[0])
links.new(transparent.outputs[0], mix_shader.inputs[1])
links.new(emission.outputs[0], mix_shader.inputs[2]) 
links.new(mix_shader.outputs[0], output.inputs[0])

# Assign material
bpy.context.active_object.data.materials.append(mat)

# Create UV projection
if not bpy.context.active_object.mode == 'EDIT':
    bpy.ops.object.editmode_toggle()
bpy.ops.uv.smart_project()
bpy.ops.object.editmode_toggle()

# Add copy location constraint
# Target is manual
constraint = obj.constraints.new('COPY_LOCATION')
constraint.target = None
constraint.use_offset = True