import bpy

# Função para salvar no formato Blender (.blend)
def save_blend(filename):
    blend_file_path = filename.replace('.c3d', '_imported.blend')
    bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)
    print(f"Arquivo .blend salvo como: {blend_file_path}")