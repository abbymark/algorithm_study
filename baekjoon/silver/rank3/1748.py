n = input()

num = 0
# breakpoint()
for i in range(len(n)):
    if i == 0:
        add = len(n) * (int(n) - 10 **(len(n) - 1) + 1)
        num += add
    else:
        add = (len(n) - i) * 9 * 10 ** (len(n) - i -1 )
        num += add
print(num)