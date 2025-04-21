import bpy

#EEVEE Settings
bpy.context.scene.eevee.taa_samples = 1
bpy.context.scene.eevee.taa_render_samples = 4
bpy.context.scene.eevee.use_bloom = True
bpy.context.scene.view_settings.view_transform = 'Standard'
#bpy.context.scene.eevee.use_bloom = False


#Output settings
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.ffmpeg.format = 'MKV' 
bpy.context.scene.render.ffmpeg.codec = 'H264'
bpy.context.scene.render.ffmpeg.constant_rate_factor = 'HIGH'
bpy.context.scene.render.ffmpeg.audio_codec = 'AAC'
bpy.context.scene.render.ffmpeg.audio_bitrate = 128
bpy.context.scene.render.fps = 60
bpy.context.scene.render.resolution_percentage = 100
bpy.context.scene.sync_mode = 'AUDIO_SYNC'
#bpy.context.scene.render.resolution_x = 1920
#bpy.context.scene.render.resolution_y = 1080

