import ezc3d

def read_c3d(c3d_file):
    # Carregar o arquivo C3D
    c3d = ezc3d.c3d(c3d_file)

    # Explorar o cabeçalho (header)
    print("Header:", c3d["header"])

    # Explorar os parâmetros
    print("Parameters:", c3d["parameters"])

    # Verificar a estrutura do bloco de dados
    print("Data keys:", c3d["data"].keys())

    # Dados de marcadores (3D): [3, número de frames, número de marcadores]
    print("Dimensão dos marcadores:", c3d["data"]["points"].shape)

    # Dados analógicos (forças, sinais de EMG, etc.): [número de canais, número de frames]
    print("Dimensão dos sinais analógicos:", c3d["data"]["analogs"].shape)

    # Parâmetros individuais (exemplo: nomes dos marcadores)
    marker_labels = c3d["parameters"]["POINT"]["LABELS"]["value"]
    print("Marcadores:", marker_labels)


read_c3d('examples/ibm2401.c3d')