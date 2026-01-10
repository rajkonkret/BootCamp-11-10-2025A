import tkinter as tk


def on_click():
    print("Przycisk został naciśnięty")


app = tk.Tk()
app.title("Przykład Button")
app.geometry("300x200")

# definiowanie obiektu typu Button
button = tk.Button(app, text="Kliknij mnie", command=on_click)  # podajemy referencje funkcji (adres)

# wstawienie elemntu Button do okienka tak by się wyświetlał
button.pack()

app.mainloop()
