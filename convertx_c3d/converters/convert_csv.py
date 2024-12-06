import bpy
import c3d
import sys
import argparse
import csv
import os

# Configuração do parser para argumentos
parser = argparse.ArgumentParser(description='Convert a C3D file to CSV (text) format.')
parser.add_argument('-a', '--include-analog', action='store_true', help='output analog values after point positions')
parser.add_argument('-c', '--include-camera', action='store_true', help='output camera count with each point position')
parser.add_argument('-r', '--include-error', action='store_true', help='output error value with each point position')
parser.add_argument('-e', '--end', default='\\n', metavar='K', help='write K between records')
parser.add_argument('-s', '--sep', default=',', metavar='C', help='write C between fields in a record')
parser.add_argument('file_input', default=None, metavar='FILE', nargs='*', help='process data from this file_input FILE')


# Função para salvar o arquivo como CSV
def save_csv(filename, args, sep, end, n_points, analog_labels, reader):
    with open(filename.replace('.c3d', '.csv'), 'w', newline='') as output:
        writer = csv.writer(output, delimiter=sep, lineterminator=end)
        header = ["frame"]
        for i in range(1, n_points + 1):
            header.extend([f"x{i}", f"y{i}", f"z{i}"])
        if args.include_analog:
            header.extend(analog_labels)
        if args.include_error:
            header.extend([f"error{i}" for i in range(1, n_points + 1)])
        if args.include_camera:
            header.extend([f"camera{i}" for i in range(1, n_points + 1)])

        writer.writerow(header)

        for frame_no, points, analog in reader.read_frames(copy=False):
            fields = [frame_no]
            for x, y, z, err, cam in points:
                fields.extend([x, y, z])
                if args.include_error:
                    fields.append(err)
                if args.include_camera:
                    fields.append(cam)
            if args.include_analog:
                fields.extend(analog.flatten())
            writer.writerow(fields)
    print("Arquivo CSV salvo com sucesso!")


# Função para salvar no formato Blender (.blend)
'''def save_blend(filename):
    blend_file_path = filename.replace('.c3d', '_imported.blend')
    bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)
    print(f"Arquivo .blend salvo como: {blend_file_path}")


# Função para exportar para OpenSCAD
def save_openscad(filename, points):
    scad_file_path = filename.replace('.c3d', '.scad')
    with open(scad_file_path, 'w') as file:
        file.write("// Gerado automaticamente do CSV\n")
        for point in points:
            # Verifique se o ponto tem pelo menos 3 valores
            if len(point) >= 3:
                x, y, z = point[:3]  # Pegue os primeiros 3 valores
                file.write(f"translate([{x}, {y}, {z}]) sphere(r=0.1);\n")
            else:
                print(f"Ponto com dados insuficientes: {point}")
    print(f"Arquivo OpenSCAD salvo como: {scad_file_path}")

# Função para exportar para FBX
def save_fbx(filename):
    fbx_file_path = filename.replace('.c3d', '.fbx')
    bpy.ops.export_scene.fbx(filepath=fbx_file_path)
    print(f"Arquivo FBX salvo como: {fbx_file_path}")


# Função principal de conversão
def convert(filename, args, sep, end):
    file_input = sys.stdin
    output = sys.stdout
    open_file_streams = filename != '-'
    if open_file_streams:
        file_input = open(filename, 'rb')
        output = open(filename.replace('.c3d', '.csv'), 'w')

    try:
        # Lê os frames do arquivo C3D
        reader = c3d.Reader(file_input)
        n_points = reader.point_labels.shape[0]  # Número total de pontos
        analog_labels = reader.analog_labels  # Labels de canais analógicos, se existirem
        points = []

        # Processa os dados frame a frame
        for frame_no, points_data, analog in reader.read_frames(copy=False):
            points.extend(points_data)

        # Pergunta o formato de exportação
        user_choice = input("Escolha o formato de exportação (csv, blend, scad, fbx): ").strip().lower()

        if user_choice == 'csv':
            save_csv(filename, args, sep, end, n_points, analog_labels, reader)
        elif user_choice == 'blend':
            save_blend(filename)
        elif user_choice == 'scad':
            save_openscad(filename, points)
        elif user_choice == 'fbx':
            save_fbx(filename)
        else:
            print("Formato não reconhecido! Escolha entre 'csv', 'blend', 'scad' ou 'fbx'.")
    finally:
        if open_file_streams:
            file_input.close()
            output.close()


# Função principal do programa
def main():
    args = parser.parse_args()
    sep = args.sep.replace('\\t', '\t').replace('TAB', '\t')
    end = args.end.replace('\\r', '\r').replace('CR', '\r').replace('\\n', '\n').replace('NL', '\n')

    # Pergunta o nome do arquivo, caso não seja fornecido
    if not args.file_input or args.file_input == ['-']:
        filename = input("Digite o caminho do arquivo C3D: ").strip()
        args.file_input = [filename]

    for filename in args.file_input:
        convert(filename, args, sep, end)


if __name__ == "__main__":
    main()'''
