# Снежинка Коха
import turtle


def koch(order, size):
    turtle.hideturtle()
    if order == 0:
        turtle.forward(size)
    else:
        koch(order-1, size/3)
        turtle.left(60)
        koch(order-1, size/3)
        turtle.right(120)
        koch(order-1, size/3)
        turtle.left(60)
        koch(order-1, size/3)


def main():
    turtle.hideturtle()
    turtle.color('blue')
    turtle.begin_fill()
    turtle.color('blue')
    turtle.tracer(0)
    turtle.up()
    turtle.goto(-300,0)
    turtle.down()
    n = int(input('Глубина рекурсии: '))
    a = int(input('Длина стороны: '))
    koch(n, a)
    turtle.right(120)
    koch(n, a)
    turtle.right(120)
    koch(n, a)
    turtle.end_fill()
    turtle.mainloop()


if __name__ == '__main__':
    main()
