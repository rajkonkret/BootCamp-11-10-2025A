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

# FileNotFoundError: [Errno 2] No such file or directory: 'ops_example/A/B'
# nie ma katalogu A, nie może stworzyc katalogu B
# path_b.mkdir()
path_b.mkdir(parents=True)  # parents=True - tworzy wszystkie pośrednie katalogi w drzewie

# zadziała bo katalog A już istnieje
path_c.mkdir()

# utworzenie plików w katalogu path_b
for filename in ('ex1.txt', "ex2.txt", 'ex3.txt'):
    with open(path_b / filename, "w", encoding="utf-8") as stream:
        stream.write(f"Jakaś treść pliku: {filename}")

# przeniesienie plików do innego katalogu
# stworzył katalog D, usunął katalog B
shutil.move(path_b, path_d)

# kopiowanie pliku
shutil.copy(path_d / 'ex1.txt', path_c / 'ex1.txt')
