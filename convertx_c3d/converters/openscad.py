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