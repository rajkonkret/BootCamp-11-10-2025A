import tkinter as tk

root = tk.Tk()
root.title('Pack Layout Example')
root.geometry("400x300")

tk.Label(root, text="Top", bg="red").pack(side=tk.TOP, fill=tk.X)
tk.Label(root, text="Bottom", bg="blue").pack(side=tk.BOTTOM, fill=tk.X)
tk.Label(root, text="Left", bg="green").pack(side=tk.LEFT, fill=tk.Y)
tk.Label(root, text="Right", bg="purple").pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()
