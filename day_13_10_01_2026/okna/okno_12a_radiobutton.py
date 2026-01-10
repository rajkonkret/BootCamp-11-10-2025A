import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkfont


class MyGui:
    """
    Klasa odwzorowująca okno
    """

    def __init__(self):
        """
        Metoda inicjalizująca, konstruktor
        """

        self.main_window = tk.Tk()
        self.main_window.title("Okno wyboru")
        self.main_window.geometry("400x400")

        self.top_frame = tk.Frame(self.main_window)

        self.radio_var = tk.IntVar()
        self.radio_var.set(1)  # ustawiamy jako aktywny pierwszy wybór

        my_font = tkfont.Font(family="Helvetica", size=18, weight="bold")

        self.label1 = tk.Label(self.top_frame, text="Start", font=my_font)

        self.rb1 = tk.Radiobutton(self.top_frame, text="Opcja 1", variable=self.radio_var, value=1)
        self.rb2 = tk.Radiobutton(self.top_frame, text="Opcja 2", variable=self.radio_var, value=2)
        self.rb3 = tk.Radiobutton(self.top_frame, text="Opcja 3", variable=self.radio_var, value=3)

        self.label1.pack()

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.top_frame.pack()

        tk.mainloop()


gui = MyGui()
