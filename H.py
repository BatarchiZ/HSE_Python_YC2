FN = int(input())

F0 = 0
F1 = 1
Fn = 0
x = 1
if FN == 0:
    print(0)
if FN == 1:
    print(1)
else:
    while True:
        Fn = F1 + F0
        F0 = F1
        F1 = Fn
        x = x + 1
        if Fn > FN:
            break
        if Fn == FN:
            break
    if Fn == FN:
        print(x)
    if Fn > FN:
        print(-1)
