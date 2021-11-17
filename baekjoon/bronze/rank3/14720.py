n = int(input())
milks = list(map(int, input().split()))

# 0 딸기우유
# 1 초코우유
# 2 바나나우유

# 0 - 1 - 2 - 0 - 1 - 2

count = 0
current = 2
for milk in milks:
    if milk == 0 and current == 2:
        count += 1
        current = 0
    elif milk == 1 and current == 0:
        count += 1
        current = 1
    elif milk == 2 and current == 1:
        count += 1
        current = 2

print(count)