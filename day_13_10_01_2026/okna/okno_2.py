import tkinter as tk

root = tk.Tk()
root.title("Wyśrodkowane okno")

# jawnie określenie rozmiaru okna
root.geometry("300x200")

# czekamy na to, aż window manager ustali rozmiary
root.update_idletasks()

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
ww = root.winfo_width()
wh = root.winfo_height()

# obliczanie pozycjy startowej
x = (sw - ww) // 2  # część całkowita z dzielenia
y = (sh - wh) // 2

root.geometry(f"{ww}x{wh}+{x}+{y}")

root.mainloop()
