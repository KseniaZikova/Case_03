# Фрактал Леви
# Developers: Zikova K. 75%, Bateneva M. 80%, Shlapakova K. 90%

import turtle


def levi(d, n):
    if n == 0:
        turtle.forward(d)
        return
    else:
        turtle.left(45)
        levi(d, n - 1)
        turtle.right(45)
        turtle.right(45)
        levi(d, n - 1)
        turtle.left(45)


def main():
    d = int(input("Длина стороны: "))
    n = int(input("Глубина рекурсии: "))
    turtle.up()
    turtle.speed('fastest')
    turtle.goto(-100, -100)
    turtle.down()
    levi(d, n)
    turtle.mainloop()


if __name__ == '__main__':
    main()
