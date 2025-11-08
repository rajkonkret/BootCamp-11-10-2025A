from pathlib import Path

folder_path = Path("katalog/")

txt_files = list(folder_path.glob("*.txt"))
print(f"Pliki .txt: {[f.name for f in txt_files]}")
# Pliki .txt: ['file_1.txt', 'nowy.txt', 'results.txt']

for file_path in txt_files:
    content = file_path.read_text(encoding='utf-8')
    print(f"Plik: {file_path}, rozmiar: {len(content)} znaków.")
    with open(file_path, "r") as f:
        text = f.read()
    print(text)
# Plik: katalog/file_1.txt, rozmiar: 0 znaków.
# Plik: katalog/nowy.txt, rozmiar: 9 znaków.
# Plik: katalog/results.txt, rozmiar: 6 znaków.

# Plik: katalog/file_1.txt, rozmiar: 0 znaków.
#
# Plik: katalog/nowy.txt, rozmiar: 9 znaków.
# Nowy plik
# Plik: katalog/results.txt, rozmiar: 6 znaków.
# Treść
