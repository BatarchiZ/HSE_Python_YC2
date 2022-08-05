P = float(input())
R = int(input())
C = int(input())

R1 = R * 100
R1C = R1 + C

PR1C = round((R1C * (100 + P))) / 100

DecimalRep = (PR1C / 100)
Amount = str(int(PR1C))

INT = (Amount[-3::-1])
INT = INT[::-1]
D = Amount[-2::]
if D == '00':
    D = 0
print(INT, D)
