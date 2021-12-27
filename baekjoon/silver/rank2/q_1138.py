n = int(input())

left_height = list(map(int, input().split()))

sorted_height = [0] * n
# breakpoint()
for i, height in enumerate(left_height):
    count = 0
    for j, loc in enumerate(sorted_height):
        if loc == 0:
            count += 1
        if count-1 == height:
            sorted_height[j] = i+1
            break

print(' '.join(list(map(str, sorted_height))))
