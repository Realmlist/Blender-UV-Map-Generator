################################################
#                 !!WARNING!!                  #
#                                              #
# THIS SCRIPT WILL DELETE ALL EXISTING UV MAPS #
#            ON THE SELECTED OBJECTS           #
#       PLEASE SAVE AND BACKUP YOUR WORK       #
#                                              #
#                 ~Realmlist                   #
################################################



import bpy

selection = bpy.context.selected_objects

# Deselect all objects
bpy.ops.object.select_all(action='DESELECT')

for obj in selection:
    
    # Select each object
    obj.select_set(True)

    # Make it active
    bpy.context.view_layer.objects.active = obj
    active_object = bpy.context.active_object
    
    uvl = bpy.context.active_object.data.uv_layers

    # Clear old (all) UVs
    uvs = [uv for uv in uvl]
    while uvs:
        uvl.remove(uvs.pop())
        
    # Toggle into Edit Mode
    bpy.ops.object.mode_set(mode='EDIT')

    # Select the geometry
    bpy.ops.mesh.select_all(action='SELECT')

    # Create new UVMaps & UVs
    uvl.new(name='UV0')
    uvl[0].active = True
    bpy.ops.uv.unwrap()

    uvl.new(name='UV1')
    uvl[1].active = True
    # Smart project for lightmap UV on Reava's recommendation: https://twitter.com/Reava_VR/status/1614982278333202439
    bpy.ops.uv.smart_project()
    
    # Set UV0 back as active
    uvl[0].active = True
    
    # Toggle out of Edit Mode
    bpy.ops.object.mode_set(mode='OBJECT')

    # Deselect the object
    obj.select_set(False)

# Restore the selection
for obj in selection:
    obj.select_set(True)
