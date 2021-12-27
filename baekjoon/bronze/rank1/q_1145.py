n = list(map(int, input().split()))
n = sorted(n)
count = 0
add = 0
while True:
    target = n[2] + add
    for num in n:
        if target % num == 0:
            count +=1
        if count >2:
            break
    # print('working')
    if count > 2:
        break
    else:
        count = 0
        add += 1
print(n[2] + add)