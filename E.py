required_number = '0'
L = []
while True:
    number = input()
    if number == required_number:
        break
    else:
        L.append(number)
M = list(map(int, L))
X = sorted(M)
print(X[-2])
