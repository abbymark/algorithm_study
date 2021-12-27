n = int(input())

for i in range(n):
    num = int(input())
    divisors = ''
    while True:
        if num == 1:
            divisors = '1'
            break
        for i in range(9, 1, -1):
            if num % (i) == 0:
                divisors += str(i)
                num = num // (i)
                break
        else:
            num = -1
            break
        if num == 1:
            break
    if num == -1:
        print(-1)
    else:
        print(len(divisors))
