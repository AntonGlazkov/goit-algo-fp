import turtle

def pythagoras_tree(t, length, level):
    if level == 0:
        return

    t.forward(length)

    t.left(45)
    pythagoras_tree(t, length * 0.7, level - 1)

    t.right(90)
    pythagoras_tree(t, length * 0.7, level - 1)

    t.left(45)
    t.backward(length)


def main():
    level = int(input("Вкажіть рівень рекурсії: "))

    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)

    pythagoras_tree(t, 100, level)

    screen.mainloop()


if __name__ == "__main__":
    main()

