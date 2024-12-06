import bpy
import c3d
import sys
import argparse
import csv
import os
import blender
import unreal
import openscad
import convert_csv


# Configuração do parser para argumentos
parser = argparse.ArgumentParser(description='Convert a C3D file to CSV (text) format.')
parser.add_argument('-a', '--include-analog', action='store_true', help='output analog values after point positions')
parser.add_argument('-c', '--include-camera', action='store_true', help='output camera count with each point position')
parser.add_argument('-r', '--include-error', action='store_true', help='output error value with each point position')
parser.add_argument('-e', '--end', default='\\n', metavar='K', help='write K between records')
parser.add_argument('-s', '--sep', default=',', metavar='C', help='write C between fields in a record')
parser.add_argument('file_input', default=None, metavar='FILE', nargs='*', help='process data from this file_input FILE')


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
            convert_csv.save_csv(filename, args, sep, end, n_points, analog_labels, reader)
        elif user_choice == 'blend':
            blender.save_blend(filename)
        elif user_choice == 'scad':
            openscad.save_openscad(filename, points)
        elif user_choice == 'fbx':
            unreal.save_fbx(filename)
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
    main()
