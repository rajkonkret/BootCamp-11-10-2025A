import tkinter as tk


def get_entry_value():
    text = entry.get()
    print(f"Entered text: {text}")


root = tk.Tk()
root.title("Pole Entry, Przykład 2")
root.geometry("300x150")

# definiujemy pole Entry
entry = tk.Entry(root, width=30)  # szerokosc 30
# entry.pack()
entry.pack(pady=10)  # wcięcie, wewnętrny margines

entry.insert(0, "Type here...")  # wpisany tekst w pole Entry

button = tk.Button(root, text="Get Text", command=get_entry_value)
# button.pack()
button.pack(pady=5)

root.mainloop()
