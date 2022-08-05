numbers = []
maximums = []
i = int(input())
while i != 0:
    numbers.append(i)
    i = int(input())

for i in range(1, len(numbers) - 1):
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        maximums.append(i)

if len(maximums) > 1:
    least_distance = min([maximums[i + 1] - maximums[i] for i in range(0, len(maximums) - 1)])
    print(least_distance)
else:
    print(0)
