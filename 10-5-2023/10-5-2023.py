efficiencies = [1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111, 123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]
efficiencies.sort()

min_cost = float("inf")
for i in range(len(efficiencies)):
    temp = list(efficiencies)
    temp.pop(i)
    cost = 0

    for i in range(0, len(temp), 2):
        cost += temp[i+1] - temp[i]

    min_cost = min(min_cost, cost)

print(min_cost)