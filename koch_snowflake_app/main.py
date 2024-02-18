import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


def get_recursion_level():
    while True:
        try:
            level = int(input("Enter the recursion level: "))
            if level < 0:
                print("Recursion level must be more or equal to 0. Chosen level is 0.")
                return 0

            if level >= 6:
                print("Recursion level must be less than 6. Chosen level id 6.")
                return 6

            else:
                return level
        except ValueError:
            print("Invalid input. Recursion level must be a non-negative integer.")
        except KeyboardInterrupt:
            print("\nProgram was interrupted by user")
            exit()


def main():
    recursion_level = get_recursion_level()

    draw_koch_curve(recursion_level)


if __name__ == "__main__":
    main()
