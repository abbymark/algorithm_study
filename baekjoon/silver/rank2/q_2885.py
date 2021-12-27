n = int(input())

squares = []
square = 1
while square < 2000000:
    squares.append(square)
    square *= 2
# print(squares)

used_square = 0
for square in squares:
    if square >= n:
        used_square = square
        break
print(used_square, end=' ')
cut = 0
while True:
    if used_square == 1:
        break
    if n % used_square == 0:
        break
    else:
        used_square = used_square // 2
        cut += 1
print(cut)