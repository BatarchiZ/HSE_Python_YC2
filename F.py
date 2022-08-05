required_number = '0'
L = []
while True:
    number = int(input())
    if number == int(required_number):
        break
    else:
        L.append(number)

X = sorted(L)
if len(X) != 0:
    print(X.count(max(X)))
else:
    print(0)
