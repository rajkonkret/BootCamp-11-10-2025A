import os

print(os.path.abspath("../main.py"))
# /Users/radoslawjaniak/PycharmProjects/BootCamp-11-10-2025A/main.py

# for root, dirs, files in os.walk("../.."):  # dwa poziomy wyżej
# for root, dirs, files in os.walk("../"):  #
for root, dirs, files in os.walk("../day_6_9_11_2025"):  # dwa poziomy wyżej
    abs_root = os.path.abspath(root)
    # print(abs_root)
    if dirs:
        print("Directories:")
        for dir_ in dirs:
            print(dir_)

    if files:
        print("Files:")
        for filename in files:
            print(filename)
