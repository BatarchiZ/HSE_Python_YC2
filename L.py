import math

P = float(input())
R = int(input())
C = int(input())
T = int(input())

t = T

PTXY = (R * 100) + C

while t != 0:
    PTXY = PTXY * (100 + P)

    PTXY = PTXY / 100

    rnd100PTXY = math.floor(PTXY)

    PTXY = rnd100PTXY

    t = t - 1

Amount = str(int(PTXY))

INT = (Amount[-3::-1])
INT = INT[::-1]
D = Amount[-2::]
if D == '00':
    D = 0
print(INT, D)
