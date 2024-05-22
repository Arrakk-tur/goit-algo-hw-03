import turtle


def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)
        t.right(120)
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)


def koch_snowflake(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)


def main():
    # Створення вікна для малювання
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)  # максимальна швидкість

    # Задання рівня рекурсії користувачем
    level = int(input("Введіть рівень рекурсії: "))

    # Позиціювання черепашки
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    # Малювання сніжинки Коха
    length = 400  # довжина ребра
    koch_snowflake(t, length, level)

    # Завершення
    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()
