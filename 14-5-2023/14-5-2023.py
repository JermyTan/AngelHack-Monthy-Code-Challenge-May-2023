from functools import cache

inf = float("inf")
s = "kjslaqpwoereeeeewwwefifjdksjdfhjdksdjfkdfdlddkjdjfjfjfjjjjfjffnefhkjgefkgjefkjgkefjekihutrieruhigtefhgbjkkkknbmssdsdsfdvneurghiueor"

@cache
def dp(i, j):
    if i > j:
        return 0
    if i == j:
        return 1
    
    # case 1: just delete ith character
    case1 = dp(i+1, j) + 1

    # case 2: delete letters between 2 matching chars s[i] and s[k]
    case2 = min((dp(i+1, k-1) + dp(k, j) for k in range(i+1, j+1) if s[i] == s[k]), default=inf)
    
    return min(case1, case2)

print(dp(0, len(s)-1))


        