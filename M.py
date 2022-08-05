import math

N = float(input())
y, x = math.modf(N)
Y = (y * 100)
Y = round(Y)
print('{0} {1}'.format(int(x), int(Y)))
