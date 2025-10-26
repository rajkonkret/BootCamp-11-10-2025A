import shutil
from pathlib import Path

base_path = Path('ops_example')
base_path2 = Path('ops_example/D')

if base_path.exists() and base_path.is_dir():
    # Recursively delete a directory tree
    shutil.rmtree(base_path)

# tworzenie katalogu
base_path.mkdir()

path_b = base_path / "A" / "B"
path_c = base_path / "A" / "C"
path_d = base_path / "A" / "D"
