import tkinter as tk

root = tk.Tk()
root.title("Place Layout Example")
root.geometry("400x300")

tk.Label(root, text="Absolute position", bg="lightblue").place(x=50, y=50)

tk.Button(root, text="Relative position").place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()
