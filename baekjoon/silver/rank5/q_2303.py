N = int(input())
scores = []

for _ in range(N):
    card = list(map(int, input().split()))
    max_score = 0
    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                digit = card[i] + card[j] + card[k]
                digit = digit % 10
                if digit >= max_score:
                    max_score = digit
    scores.append(max_score)

for i in range(N-1, -1, -1):
    if scores[i] == max(scores):
        print(i+1)
        break
