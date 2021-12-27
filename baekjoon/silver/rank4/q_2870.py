n = int(input())
nums = []
for i in range(n):
    word = input()
    num = ''
    for j, letter in enumerate(word):
        if letter.isdigit():
            num += letter
        elif num:
            nums.append(int(num))
            num = ''
        if num and j == len(word) - 1:
            nums.append(int(num))
nums.sort()
for num in nums:
    print(num)