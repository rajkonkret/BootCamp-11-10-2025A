import tkinter as tk
from tkinter import ttk
import sqlite3


def fetch_data():
    # połaczenie z bazą
    conn = sqlite3.connect('moja_baza.db')
    cur = conn.cursor()
    cur.execute("SELECT id, nazwa FROM przyklad;")
    rows = cur.fetchall()
    conn.close()
    return rows


root = tk.Tk()
root.title("Dane z SQLite")

# definujemy kolumny
columns = ('id', 'nazwa')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.pack(fill=tk.BOTH, expand=True)

# nagłowki
tree.heading('id', text="ID")
tree.heading('nazwa', text="Nazwa")

# szerokość kolumn
tree.column("id", width=50, anchor=tk.CENTER)
tree.column("nazwa", width=150, anchor=tk.W)

# wczzytanie danych i wstawienie danych do widoku
for row in fetch_data():
    tree.insert("", tk.END, values=row)

root.mainloop()
