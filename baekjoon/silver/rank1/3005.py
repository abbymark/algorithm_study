r, c = map(int, input().split())

puzzle = []

for i in range(r):
    puzzle.append(list(input()))


words = []
# breakpoint()
for i in range(r):
    word = []
    for j in range(c):
        if puzzle[i][j] != '#':
            word.append(puzzle[i][j])
        else:
            if len(word) >= 2:
                words.append(''.join(word))
            word = []

        if j == c-1 and len(word) >= 2:
            words.append(''.join(word))

for i in range(c):
    word = []
    for j in range(r):
        if puzzle[j][i] != '#':
            word.append(puzzle[j][i])
        else:
            if len(word) >= 2:
                words.append(''.join(word))
            word = []
        
        if j == r-1 and len(word) >= 2:
            words.append(''.join(word))

words.sort()
print(words[0])