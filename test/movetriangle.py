from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)


def movetriangle(event):
    if event.keysym == 'w':
        canvas.move(1, 0, -3)
    elif event.keysym == 's':
        canvas.move(1, 0, 3)
    elif event.keysym == 'a':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)


canvas.bind_all('<KeyPress-w>', movetriangle)
canvas.bind_all('<KeyPress-s>', movetriangle)
canvas.bind_all('<KeyPress-a>', movetriangle)
canvas.bind_all('<KeyPress-d>', movetriangle)
print('a')


