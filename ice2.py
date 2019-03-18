# "Ледяной" фрактал 2
# Developers: Zikova K. 75%, Bateneva M. 80%, Shlapakova K. 90%

import turtle


def ice3(d, n):
    if n == 0:
        turtle.forward(d)
        return
    else:
        ice3(d, n - 1)
        turtle.left(130)
        ice3(d // 2, n - 1)
        turtle.left(180)
        ice3(d // 2, n - 1)
        turtle.left(100)
        ice3(d // 2, n - 1)
        turtle.left(180)
        ice3(d // 2, n - 1)
        turtle.left(130)
        ice3(d, n - 1)


def main():
    d = int(input("Длина стороны: "))
    n = int(input("Глубина рекурсии: "))
    turtle.tracer(0)
    turtle.up()
    turtle.goto(-300, -100)
    turtle.down()
    ice3(d, n)
    turtle.mainloop()


if __name__ == '__main__':
    main()
