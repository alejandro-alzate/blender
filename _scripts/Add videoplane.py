# Generar plano en frente de la camara
import bpy

# Create a new plane
bpy.ops.mesh.primitive_plane_add()

# Get the active object (the plane we just created)
plane = bpy.context.active_object

# Set location
plane.location = (0, 0, 5)

# Set rotation (90 degrees in X axis, converted to radians)
plane.rotation_euler = (1.5708, 0, 0)  # 90° = 1.5708 radians

# Set scale
plane.scale = (1.850, 1.050, 1)

# Set dimensions
plane.dimensions = (3.7, 2.1, 0)

plane.name = "VideoPlane"

# Create new material
mat = bpy.data.materials.new(name = "Plane_Material")
mat.use_nodes = True
nodes = mat.node_tree.nodes
links = mat.node_tree.links

# Clear default nodes
nodes.clear()

# Create and position nodes
tex_coord = nodes.new(type = 'ShaderNodeTexCoord')
tex_coord.location = (-900, 100)

mapping = nodes.new(type = 'ShaderNodeMapping')
mapping.location = (-700, 100)

tex_image = nodes.new(type = 'ShaderNodeTexImage')
tex_image.location = (-500, 100)
tex_image.interpolation = "Closest"
tex_image.image_user.use_auto_refresh = True

emission = nodes.new(type = 'ShaderNodeEmission')
emission.location = (-200, 100)

material_output = nodes.new(type = 'ShaderNodeOutputMaterial')
material_output.location = (0, 100)

# Create links between nodes
links.new(tex_coord.outputs['UV'], mapping.inputs['Vector'])
links.new(mapping.outputs['Vector'], tex_image.inputs['Vector'])
links.new(tex_image.outputs['Color'], emission.inputs['Color'])
links.new(emission.outputs['Emission'], material_output.inputs['Surface'])

# Assign material to plane
plane.data.materials.append(mat)

plane.active_material.shadow_method = 'NONE'


# Optional: To load an image (uncomment and replace with actual path)
# tex_image.image = bpy.data.images.load('path/to/your/image.png')