n_burgers, n_sides, n_drinks = map(int, input().split())

burgers = list(map(int, input().split()))
sides = list(map(int, input().split()))
drinks = list(map(int, input().split()))

print(sum(burgers) + sum(sides) + sum(drinks))

burgers.sort(reverse=True)
sides.sort(reverse=True)
drinks.sort(reverse=True)

max_len = max([n_burgers, n_sides, n_drinks])

result = 0
for i in range(max_len):
    burger = burgers[i] if n_burgers > i else 0
    side = sides[i] if n_sides > i else 0
    drink = drinks[i] if n_drinks > i else 0
    
    if all([burger, side, drink]):
        result += sum([burger, side, drink]) * 0.9
    else:
        result += sum([burger, side, drink])

print(int(result))
