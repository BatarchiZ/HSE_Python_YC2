import math

a = float(input())
b = float(input())
c = float(input())
while True:
    if a == 0 and b == 0 and c == 0:
        print(3)
        break
    if a == 0 and b != 0:
        x = (-c) / b

        x16 = x * (10 ** 6)
        x1trunc = math.floor(x16)
        x10 = x1trunc / float(10 ** 6)
        if x10 % 1 == 0:
            x = int(x)
        else:
            x = x10

        ans = [x, ]
        Sans = sorted(ans)
        print(1, Sans[0])

        break
    if a == 0 and b == 0:
        print(0)
        break
    disc = (b ** 2 - 4 * a * c)
    sqrt = math.sqrt(abs(disc))

    while True:
        if disc < 0:
            print(0)
            break

        if disc == 0:

            x1 = (-b + sqrt) / (2 * a)

            x16 = x1 * (10 ** 6)
            x1trunc = math.floor(x16)
            x10 = x1trunc / float(10 ** 6)
            if x10 % 1 == 0:
                x1 = int(x1)
            else:
                x1 = x10

            ans = [x1, ]
            Sans = sorted(ans)
            print(1, Sans[0])
            break

        if disc > 0:
            x2 = (-b - sqrt) / (2 * a)
            x1 = (-b + sqrt) / (2 * a)

            x16 = x1 * (10 ** 6)
            x1trunc = math.floor(x16)
            x10 = x16 / float(10 ** 6)
            if x10 % 1 == 0:
                x1 = int(x1)
            else:
                x1 = x10

            x26 = x2 * (10 ** 6)
            x2trunc = math.floor(x26)
            x20 = x26 / float(10 ** 6)
            if x20 % 1 == 0:
                x2 = int(x2)
            else:
                x2 = x20

            ans = [x1, x2]
            Sans = sorted(ans)
            print(2, Sans[0], Sans[1])

            break
    break
