import tkinter as tk


class MainView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.listbox = tk.Listbox(self)
        self.listbox.pack()

        tk.Button(self, text="Odśwież", command=self.refresh).pack()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for u in self.controller.list_users():
            self.listbox.insert(tk.END, f"{u[0]} - {u[1]}")
