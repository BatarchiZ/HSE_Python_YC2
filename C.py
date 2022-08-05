N = int(input())

if N % 2 == 0:
    print(2)
else:
    i = 3
    while N % i != 0:
        i = i + 2
    print(i)
