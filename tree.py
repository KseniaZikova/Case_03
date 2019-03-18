# Дерево
import turtle
import random


def tree(d, n, color='green', count=0):
    turtle.hideturtle()

    if count == 0:
        turtle.left(90)

    if n == 0:
        return

    turtle.speed('fastest')
    turtle.down()
    turtle.color(color)
    turtle.forward(d)
    turtle.right(20)

    count += 1
    color = random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

    tree(d*0.9, n-1, color, count)

    turtle.left(40)

    tree(d*0.9, n-1, color, count)

    turtle.right(20)
    turtle.backward(d)


def main():
    turtle.hideturtle()
    turtle.up()
    turtle.tracer(0)
    turtle.goto(0, -200)
    turtle.down()
    d = int(input("Длина стороны: "))
    n = int(input("Глубина рекурсии: "))
    tree(d, n)
    turtle.mainloop()


if __name__ == '__main__':
    main()
