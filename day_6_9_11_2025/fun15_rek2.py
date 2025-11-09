import colorsys
import turtle

# turtle - rysowanie żółwiem

t = turtle.Turtle()
# t.speed(1)
t.speed(-1)  # najwyzsza szybkość
t.setheading(90)
t.penup()
t.goto(0, -200)
t.pendown()

call_counter = 0


def branch(t, len):
    global call_counter
    if len == 0: return

    call_counter += 1
    hue = (call_counter % 100) / 100
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    t.color(r, g, b)

    nt = t.clone()
    nt.forward(50)
    nt.left(20)
    branch(nt, len - 1)
    nt.right(40)
    branch(nt, len - 1)


branch(t, 7)
window = turtle.Screen()
window.exitonclick()
