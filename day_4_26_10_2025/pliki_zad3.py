import os
import shutil

root_dir = "katalog"
target_name = "results.txt"
dest_dir = "zebrane"

if not os.path.exists(root_dir):
    os.makedirs(root_dir)

source_path = os.path.join(root_dir, target_name)
with open(source_path, "w", encoding="utf-8") as src:
    src.write('Treść\n')
