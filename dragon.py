# Фрактал дракона
# Developers: Zikova K. 75%, Bateneva M. 80%, Shlapakova K. 90%

import turtle


def dr(d, n, c=45):
    if n == 0:
        turtle.forward(d)
        return
    else:
        turtle.right(c)
        dr(d, n-1, 45)
        turtle.left(c*2)
        dr(d, n-1, 315)
        turtle.right(c)


def main():
    d = int(input("Длина стороны: "))
    n = int(input("Глубина рекурсии: "))
    turtle.tracer(0)
    turtle.up()
    turtle.goto(-120, 0)
    turtle.down()
    dr(d, n)
    turtle.mainloop()


if __name__ == '__main__':
    main()
