n = int(input())
N0 = 0
N1 = 1
x = 1
if n == 0:
    print(0)
    exit()
while x != n or n < x:
    FN = N1 + N0
    N0 = N1
    N1 = FN
    x = x + 1

if n == 1:
    print(1)
else:
    print(FN)
