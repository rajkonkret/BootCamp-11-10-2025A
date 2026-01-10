import os.path
import tkinter as tk
from tkinter import filedialog


def wybierz_plik():
    # start_dir = os.path.expanduser("~/Documents")
    start_dir = os.getcwd()  # otwiera filedialog w miejscu uruchomienia skryptu
    plik = filedialog.askopenfilename(
        title="Wybierz plik",
        initialdir=start_dir,
        filetypes=[("Wszystkie pliki", "*.*")]
    )
    root.deiconify()  # powrót do okienka
    if plik:
        print(f"Wybrano plik: {plik}")


root = tk.Tk()
root.title("Demo wyboru pliku")

label_path = tk.Label(root, text="Brak pliku", wraplength=400)
label_path.pack(padx=20, pady=(20, 10))

btn_again = tk.Button(root, text="Wybierz plik ponownie",
                      command=lambda: [root.withdraw(), wybierz_plik()])
btn_again.pack(pady=(0, 20))

root.withdraw()  # ukrycie głownego okna
wybierz_plik()

root.mainloop()
