# Conversor de Arquivos C3D

Este projeto é uma ferramenta para conversão de arquivos C3D em diversos formatos, incluindo **CSV**, **Blender (.blend)**, **OpenSCAD (.scad)** e **FBX (.fbx)**.

## Funcionalidades

- **CSV**: Exporta dados do arquivo C3D em formato tabular.
- **Blender**: Salva os dados importados em um arquivo `.blend`.
- **OpenSCAD**: Exporta pontos como objetos 3D no formato `.scad`.
- **FBX**: Gera um arquivo `.fbx` para uso em outras aplicações 3D.
  
## Requisitos

- **Python 3.x**
- Bibliotecas necessárias:
  - `bpy` (Blender Python API)
  - `c3d`
  - `argparse`
  - `csv`
  - `os`

## Instalação

1. Instale o Python e certifique-se de que ele esteja disponível no seu sistema.
2. Instale as dependências usando o comando:

```bash
pip install bpy c3d
