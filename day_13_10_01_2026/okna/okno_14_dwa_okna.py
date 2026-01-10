import tkinter as tk

root = tk.Tk()
root.title("Głowne okno")

label1 = tk.Label(root, text="To jest główne okno")
label1.pack(padx=10, pady=10)

root.mainloop()
