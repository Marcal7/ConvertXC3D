import bpy
def save_fbx(filename):
    fbx_file_path = filename.replace('.c3d', '.fbx')
    bpy.ops.export_scene.fbx(filepath=fbx_file_path)
    print(f"Arquivo FBX salvo como: {fbx_file_path}")