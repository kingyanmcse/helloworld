import turtle

t = turtle.Pen()


def mycircle(red, green, blue):
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()


def mysquare(size):
    for x in range(1, 5):
        t.forward(size);
        t.left(90)


mycircle(0, 0, 0)
t.reset()
mysquare(50)
mysquare(100)
mysquare(150)
