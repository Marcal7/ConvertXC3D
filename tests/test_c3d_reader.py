import c3d
import sys
import argparse

parser = argparse.ArgumentParser(description='Convert a C3D file to CSV (text) format.')
parser.add_argument('-a', '--include-analog', action='store_true', help='output analog values after point positions')
parser.add_argument('-c', '--include-camera', action='store_true', help='output camera count with each point position')
parser.add_argument('-r', '--include-error', action='store_true', help='output error value with each point position')
parser.add_argument('-e', '--end', default='\\n', metavar='K', help='write K between records')
parser.add_argument('-s', '--sep', default=',', metavar='C', help='write C between fields in a record')
parser.add_argument('input', default=None, metavar='FILE', nargs='*', help='process data from this input FILE')


def convert(filename, args, sep, end):
    input = sys.stdin
    output = sys.stdout
    open_file_streams = filename != '-'
    if open_file_streams:
        input = open(filename, 'rb')
        output = open(filename.replace('.c3d', '.csv'), 'w')
    try:
        # Lê os frames do arquivo C3D
        reader = c3d.Reader(input)
        n_points = reader.point_labels.shape[0]  # Número total de pontos
        analog_labels = reader.analog_labels  # Labels de canais analógicos, se existirem

        # Gera o cabeçalho
        header = ["frame"]
        for i in range(1, n_points + 1):
            header.extend([f"x{i}", f"y{i}", f"z{i}"])
        if args.include_analog:
            header.extend(analog_labels)
        if args.include_error:
            header.extend([f"error{i}" for i in range(1, n_points + 1)])
        if args.include_camera:
            header.extend([f"camera{i}" for i in range(1, n_points + 1)])

        # Escreve o cabeçalho no arquivo de saída
        print(*header, sep=sep, end=end, file=output)

        # Processa os dados frame a frame
        for frame_no, points, analog in reader.read_frames(copy=False):
            fields = [frame_no]
            for x, y, z, err, cam in points:
                fields.extend([str(x), str(y), str(z)])
                if args.include_error:
                    fields.append(str(err))
                if args.include_camera:
                    fields.append(str(cam))
            if args.include_analog:
                fields.extend(str(x) for x in analog.flatten())
            print(*fields, sep=sep, end=end, file=output)
    finally:
        if open_file_streams:
            input.close()
            output.close()


def main():
    args = parser.parse_args()
    sep = args.sep.replace('\\t', '\t').replace('TAB', '\t')
    end = args.end.replace(
        '\\r', '\r').replace('CR', '\r').replace(
        '\\n', '\n').replace('NL', '\n')

    # Pergunta o nome do arquivo, caso não seja fornecido
    if not args.input or args.input == ['-']:
        filename = input("Digite o caminho do arquivo C3D: ").strip()
        args.input = [filename]

    for filename in args.input:
        convert(filename, args, sep, end)


if __name__ == '__main__':
    main()
