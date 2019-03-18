import turtle


def k(d, n):
    if n == 0:
        return
    turtle.up()
    turtle.right(20)
    turtle.forward(d//4)
    turtle.down()
    for i in range(4):
        turtle.forward(d)
        turtle.right(90)
    return k(d*0.9, n-1)


def main():
    d = int(input("Длина стороны: "))
    n = int(input("Глубина рекурсии: "))
    print(k(d,n))


if __name__ == '__main__':
    main()
