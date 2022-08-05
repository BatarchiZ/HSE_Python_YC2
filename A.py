# Input
ij = input().split()
N = input()
# Convert to LC and apply ordinals
NL = N.lower()
Nord = []
for element in NL:
    if ord(element) >= 97:
        Nord.append(ord(element) - 87)
    else:
        Nord.append(element)
iv = int(ij[0])
jv = int(ij[1])
Nint = list(map(int, Nord))
# Multiply input by base 10
x = len(Nint) - 1
baselist = []
for element in Nint:
    new = element * (iv ** x)
    x = x - 1
    baselist.append(new)
# Summing up the converted list
INT10 = sum(baselist)

# Dividing
y = INT10
r = []
while y != 0:
    if y % jv > 9:
        r.append((chr(y % jv + 87)).upper())
    else:
        r.append(y % jv)
    y = y // jv
# Printing Output
rstring = list(map(str, r))
finished = ''.join(rstring)
finished2 = finished[::-1]

if (len(finished) == 0):
    print(0)
else:
    print((finished2))
