n = int(input())

goods = []
for i in range(n):
    goods.append(list(map(int, input().split())))

v = sorted(goods, key=lambda x: (x[0], -x[1]), reverse=True)
p = sorted(goods, key=lambda x: (x[1], -x[0]))

print(v[0][0], v[0][1], v[1][0], v[1][1])
print(p[0][0], p[0][1], p[1][0], p[1][1])
