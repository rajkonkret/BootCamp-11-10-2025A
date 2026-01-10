import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tk.Label(root, text="Login - labelka tkinter").pack()
ttk.Label(root, text="Login - labelka ttk").pack()
ttk.Entry(root).pack()  # pole z ttk
tk.Entry(root).pack()  # pole z tkinter
ttk.Button(root, text="Ok - ttk").pack()
tk.Button(root, text="Ok - tkinter").pack()

root.mainloop()
