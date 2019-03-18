# "Ледяной" фрактaл 1
# Developers: Zikova K. 75%, Bateneva M. 80%, Shlapakova K. 90%

import turtle


def ice(d, n):
    if n == 0:
        turtle.forward(d)
        return
    else:
        ice(d, n - 1)
        turtle.left(90)
        ice(d // 2, n - 1)
        turtle.right(180)
        ice(d // 2, n - 1)
        turtle.left(90)
        ice(d, n - 1)


def main():
    d = int(input("Длина стороны: "))
    n = int(input("Глубина рекурсии: "))
    turtle.tracer(0)
    turtle.up()
    turtle.goto(-300, -100)
    turtle.down()
    ice(d, n)
    turtle.mainloop()


if __name__ == '__main__':
    main()
