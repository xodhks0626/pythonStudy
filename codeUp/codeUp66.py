a, b, c = map(int, input().split())


def distinguish(a, b, c):
    x = a % 2
    y = b % 2
    z = c % 2

    if x == 0:
        print("even")
    else:
        print("odd")

    if y == 0:
        print("even")
    else:
        print("odd")

    if z == 0:
        print("even")
    else:
        print("odd")


distinguish(a, b, c)
