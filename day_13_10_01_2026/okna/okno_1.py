# https://docs.python.org/3/library/tkinter.html
import tkinter as tk

# mvc - model - view - controller

# biblioteka do działań z okienkami

# tworzenie okna
root = tk.Tk()

# ustawienie tytułu okna
root.title("Moje Pierwsze Okienko")

# wielkośc okna
root.geometry("400x300")
# root.geometry("<szerokosc>x<wysokosc>+<pozycja_x>+<pozycja_y>")
root.geometry("400x300+100+100")

# uruchomienie okna
root.mainloop()
