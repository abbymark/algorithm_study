E, S, M = map(int, input().split())

year = 1
while True:
    if year % 15 == 0:
        pre_E = 15
    else:
        pre_E = year % 15

    pre_S = year % 28 if year % 28 != 0 else 28 
    pre_M = year % 19 if year % 19 != 0 else 19

    if E == pre_E and S == pre_S and M == pre_M:
        print(year)
        break
    year += 1
