# Собственного сочинения
# Developers: Zikova K. 75%, Bateneva M. 80%, Shlapakova K. 90%

import turtle
import random


def snow(n, d, l, color='purple'):
    if n == 0:
        turtle.forward(d)
    else:
        color = random.choice(l)
        turtle.color(color)
        turtle.begin_fill()
        snow(n-1, d/3, l, color)
        turtle.left(60)
        snow(n-1, d/3, l, color)
        turtle.right(120)
        snow(n-1, d/3, l, color)
        turtle.left(60)
        snow(n-1, d/3, l, color)
        turtle.right(120)
        turtle.end_fill()


def main():
    turtle.ht()
    turtle.tracer(0)
    turtle.up()
    turtle.goto(0, 0)
    turtle.down()
    l = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'cyan', 'magenta']
    n = int(input('Глубина рекурсии: '))
    d = int(input('Длина стороны: '))
    snow(n, d, l)
    turtle.mainloop()


if __name__ == '__main__':
    main()
