import tkinter as tk


def show_text():
    text = entry.get()
    print(f"Wprowadzony tekst: {text}")


app = tk.Tk()
app.title("Pole wprowadzania")

# definiowanie i umieszczanie na oknie pola wprowadzania
entry = tk.Entry(app)
entry.pack()

# Button
button = tk.Button(app, text="Pokaż tekst", command=show_text)
button.pack()

app.mainloop()
# Wprowadzony tekst: tekst2
# Wprowadzony tekst: tekst3
# Wprowadzony tekst: nowy tekst
