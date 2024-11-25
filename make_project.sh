#!/bin/bash

# Create the root directory of the project
#mkdir -p ConvertX_C3D
#cd ConvertX_C3D

# Create files in the root of the project
touch README.md LICENSE .gitignore requirements.txt setup.py

# Create documentation directory and files
mkdir -p docs
touch docs/user_guide.md docs/developer_guide.md

# Create the main code directory and subdirectories
mkdir -p convertx_c3d/{converters,utils}
touch convertx_c3d/__init__.py
touch convertx_c3d/convertxc3d.py

# Create files in the 'converters' subdirectory
touch convertx_c3d/converters/__init__.py
touch convertx_c3d/converters/blender.py
touch convertx_c3d/converters/openscad.py
touch convertx_c3d/converters/unity3d.py
touch convertx_c3d/converters/unreal.py
touch convertx_c3d/converters/csv.py

# Create files in the 'utils' subdirectory
touch convertx_c3d/utils/__init__.py
touch convertx_c3d/utils/c3d_reader.py
touch convertx_c3d/utils/file_utils.py

# Create tests directory and test files
mkdir -p tests
touch tests/test_c3d_reader.py
touch tests/test_blender.py
# Add other test files as needed

# Create examples directory and example files
mkdir -p examples
touch examples/example.c3d
touch examples/output_example.blend
# Add other example files as needed

echo "Project structure for ConvertX_C3D created successfully!"

