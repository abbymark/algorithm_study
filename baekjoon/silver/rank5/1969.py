from collections import Counter
n, m = map(int, input().split())

dnas = []
for i in range(n):
    dnas.append(input())

letters = [[] for i in range(m)]

for i, dna in enumerate(dnas):
    for j, letter in enumerate(dna):
        letters[j].append(letter)

result = ''
for letter in letters:
    result += sorted(Counter(letter).most_common(), key= lambda x: (-x[1],x[0]))[0][0]
    print(sorted(Counter(letter).most_common(), key= lambda x: (-x[1], x[0]))[0][0], end='')
print()

hammingDist = 0
for dna in dnas:
    for i,letter in enumerate(dna):
        if letter != result[i]:
            hammingDist += 1
print(hammingDist)
