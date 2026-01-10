import tkinter as tk


def on_text_click(event):
    print("Kliknięto tekst:", event.x, event.y)


root = tk.Tk()
c = tk.Canvas(root, width=300, height=200, bg="white")
c.pack()

text_id = c.create_text(
    150, 100,
    text="Kliknij mnie!",
    font=("Helvetica", 18),
    fill="darkblue"
)

# gdy kliknięto tekst
c.tag_bind(text_id, '<Button-1>', on_text_click)

root.mainloop()
