import glob

folder_path = "katalog/"

# wzcytuje nazwy plików z rozszerzeniem .txt
txt_files = glob.glob(f"{folder_path}*.txt")
print(f"Znalezione pliki .txt: {txt_files}")
# Znalezione pliki .txt: ['katalog/nowy.txt', 'katalog/results.txt']

# pliki z wzorcem
pattern_files = glob.glob(f"{folder_path}file_[0-2].txt")
print(f"Znalezione pliki (wzorzec) [0-2]: {pattern_files}")
# Znalezione pliki (wzorzec) [0-2]: ['katalog/file_1.txt']

all_txt_recursive = glob.glob("**/*.txt", recursive=True)
print(f"Znalezione pliki (rekursywnie): {all_txt_recursive}")
# 'ops_example/A/D/ex2.txt', 'katalog/file_1.txt', 'katalog/nowy.txt', 'katalog/results.txt', 'zebrane/results.txt']
