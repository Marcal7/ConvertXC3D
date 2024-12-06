# 📁 ConvertXC3D: Conversão de Arquivos C3D para Múltiplos Formatos 🚀

## 🛠️ **Sobre o Projeto**

Este projeto é uma ferramenta poderosa para converter arquivos no formato **C3D** para diversos formatos, como **CSV**, **Blender (.blend)**, **OpenSCAD (.scad)** e **FBX**. Criado para facilitar o processamento e a visualização de dados biomecânicos, ele permite que pesquisadores e desenvolvedores trabalhem com seus dados em diferentes aplicações de maneira ágil.

O script principal encontra-se em:  
📂 **`convertx_c3d/converters/convertxc3d.py`**

---

## ✨ **Funcionalidades**

- **📊 Exportação para CSV:** Converte os dados dos marcadores e canais analógicos para um arquivo legível e editável.
- **🌀 Exportação para Blender (.blend):** Gera um arquivo de cena 3D para visualização e modelagem.
- **🔧 Exportação para OpenSCAD (.scad):** Cria um script OpenSCAD com objetos esféricos representando os pontos do C3D.
- **📂 Exportação para FBX:** Gera um arquivo compatível com softwares de modelagem 3D, como Maya e Unity.

---

## 🚀 **Como Usar**

1. Clone o repositório:
   ```bash
   git clone https://github.com/Marcal7/ConvertXC3D.git
   cd ConvertXC3D

2. Instale as dependências necessárias:
   ```bash
   pip install requirements.txt

3. Execute o script:
   ```bash
   python convertx_c3d/converters/convertxc3d.py


📚 Bibliotecas Utilizadas
- bpy: Para manipulação de arquivos Blender e exportação de modelos.
- c3d: Biblioteca para leitura e manipulação de arquivos C3D.
- argparse: Para gerenciar argumentos da linha de comando.
- csv: Para exportação de dados para formato tabular.
- os: Para manipulação de arquivos no sistema operacional.
- sys: Para manipulação de fluxos de entrada/saída do sistema.


🔗 Referências
- **py-c3d**: [Embodied Cognition - GitHub](https://github.com/EmbodiedCognition/py-c3d)

