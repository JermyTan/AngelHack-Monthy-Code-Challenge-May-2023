MOD = 7
num = 1867
digits = list(str(num))
result = []

def permutate(i=0):
    if i == len(digits):
        result.append(int("".join(digits)))
        return

    permutate(i+1)

    for j in range(i+1, len(digits)):
        digits[i], digits[j] = digits[j], digits[i]

        permutate(i+1)

        digits[i], digits[j] = digits[j], digits[i]

permutate()

divisible_by_MOD = list(filter(lambda n: n % MOD == 0, result))
avg = (max(divisible_by_MOD) + min(divisible_by_MOD)) / 2 if len(divisible_by_MOD) > 1 else max(divisible_by_MOD, default=0)
print(avg)