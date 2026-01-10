import tkinter as tk

root = tk.Tk()


class GradeCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Kalkulator Ocen")

        self.student_var = tk.StringVar(master)
        self.student_var.set("Uczeń 1")  # domyslna wartość
        self.student_dropdown = tk.OptionMenu(master, self.student_var, "Uczęń 1", "Uczeń 2", "Uczeń 3")
        self.student_dropdown.pack()


calculator = GradeCalculator(root)
root.mainloop()
