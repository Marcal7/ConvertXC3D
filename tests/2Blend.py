import bpy
import csv
import os


def import_csv_to_blender(csv_file):
    """Importa dados de um arquivo CSV para o Blender como objetos separados por frame."""
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Lê o cabeçalho

        # Verifica o formato do cabeçalho
        if header[0] != "frame" or not all(h.startswith(("x", "y", "z")) for h in header[1:]):
            print("O formato do arquivo CSV não é compatível. Certifique-se de que o cabeçalho está correto.")
            return

        # Determina o número de pontos por frame
        num_points = (len(header) - 1) // 3
        print(f"Encontrados {num_points} pontos por frame.")

        current_frame = None
        vertices_by_frame = {}

        # Processa as linhas do CSV
        for row in reader:
            frame_no = int(row[0])  # Número do frame
            vertices = []

            # Extrai coordenadas X, Y, Z para cada ponto
            for i in range(num_points):
                try:
                    x = float(row[1 + i * 3])
                    y = float(row[2 + i * 3])
                    z = float(row[3 + i * 3])
                    vertices.append((x, y, z))
                except ValueError:
                    print(f"Coordenadas inválidas no frame {frame_no}, ponto {i + 1}. Ignorando.")

            # Agrupa vértices por frame
            if frame_no not in vertices_by_frame:
                vertices_by_frame[frame_no] = []
            vertices_by_frame[frame_no].extend(vertices)

    # Cria objetos no Blender
    for frame, vertices in vertices_by_frame.items():
        if not vertices:
            continue

        # Cria uma nova malha e objeto
        mesh = bpy.data.meshes.new(f"Frame_{frame}_Mesh")
        obj = bpy.data.objects.new(f"Frame_{frame}_Object", mesh)

        # Adiciona o objeto à cena
        bpy.context.collection.objects.link(obj)

        # Define a geometria
        mesh.from_pydata(vertices, [], [])
        mesh.update()

        print(f"Frame {frame}: {len(vertices)} vértices adicionados.")

    print("Importação concluída.")


def export_to_blender(csv_file):
    """Salva o arquivo atual do Blender em formato .blend"""
    save_file_path = csv_file.replace(".csv", "_imported.blend")  # Define o caminho para o arquivo salvo
    try:
        bpy.ops.wm.save_as_mainfile(filepath=save_file_path)
        print(f"Arquivo salvo como: {save_file_path}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")


def export_to_openscad(csv_file):
    """Exporta os dados do CSV para o formato OpenSCAD (.scad)"""
    scad_file_path = csv_file.replace(".csv", ".scad")  # Define o caminho para o arquivo OpenSCAD
    try:
        with open(scad_file_path, 'w') as file:
            file.write("// Gerado automaticamente do CSV\n")
            for row in open(csv_file, 'r'):
                # Processa as coordenadas e escreve no formato OpenSCAD
                data = row.strip().split(',')
                if data[0] == "frame":
                    continue  # Ignora o cabeçalho
                x, y, z = data[1], data[2], data[3]
                file.write(f"translate([{x}, {y}, {z}]) sphere(r=0.1);\n")
        print(f"Arquivo OpenSCAD salvo como: {scad_file_path}")
    except Exception as e:
        print(f"Erro ao salvar arquivo OpenSCAD: {e}")


def export_to_fbx(csv_file):
    """Exporta os dados do CSV para o formato FBX (.fbx)"""
    fbx_file_path = csv_file.replace(".csv", ".fbx")  # Define o caminho para o arquivo FBX
    try:
        bpy.ops.export_scene.fbx(filepath=fbx_file_path)
        print(f"Arquivo FBX salvo como: {fbx_file_path}")
    except Exception as e:
        print(f"Erro ao salvar arquivo FBX: {e}")


# Exemplo de uso
csv_file_path = "ibm2402.csv"  # Substitua pelo caminho do seu arquivo CSV
import_csv_to_blender(csv_file_path)

# Salvar em diferentes formatos
export_to_blender(csv_file_path)
export_to_openscad(csv_file_path)
export_to_fbx(csv_file_path)
