import tkinter as tk


def on_key_press(event):
    print(f"Key pressed: {event.char}")


def on_key_return(event):
    print("Return key pressed!!!")
    text = entry.get()
    print(f"Entered: {text}")
    clear_entry()


def clear_entry():
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Keyboard Event Example")
root.geometry("300x150")

entry = tk.Entry(root)
entry.pack(pady=20)
entry.focus_set()  # ustawienie pola jako aktywne

# podłaczenie funkcji pod naciśnięcie kalwisza
entry.bind("<Key>", on_key_press)

entry.bind("<Return>", on_key_return)

# dodanie pola typu Label
tk.Label(root, text="Type in entry field and press Enter ").pack()

root.mainloop()
