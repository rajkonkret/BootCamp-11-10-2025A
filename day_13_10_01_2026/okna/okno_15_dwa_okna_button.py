import tkinter as tk

root = tk.Tk()
root.title("Główne okno")


def open_second_window():
    second_window = tk.Toplevel(root)
    second_window.title("Drugie okno")

    label = tk.Label(second_window, text="To jest drugie okno")
    label.pack(padx=10, pady=10)


button = tk.Button(root, text="Otwórz drugie okno", command=open_second_window)
button.pack(pady=10, padx=10)

root.mainloop()
