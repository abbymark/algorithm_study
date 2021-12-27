n, m = map(int, input().split())

prices = []

for i in range(m):
    prices.append(int(input()))

prices.sort()

result = 0
max = 0
price = 0

for i in range(m):
    if m-i < n:
        result = prices[i] * (m-i)
    else:
        result = prices[i] * n
    
    if max < result:
        price = prices[i]
        max = result
    
print(price, max)

