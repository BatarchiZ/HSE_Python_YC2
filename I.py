required_number = '0'
L = []
while True:
    number = input()
    if number == required_number:
        break
    else:
        L.append(number)
Lint = list(map(int, L))
x = 0
for element in Lint:
    if element % 2 == 0:
        x = x + 1
    else:
        continue
print(x)
