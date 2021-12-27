n = int(input())

files = []
for i in range(n):
    files.append(input())

file_dic = {}

for file in files:
    name, extention = file.split('.')
    if extention not in file_dic:
        file_dic[extention] = 1
    else:
        file_dic[extention] += 1

# file_dic.keys().sort()
file_dic = sorted(file_dic.items())
# print(file_dic)

for key, value in file_dic:
    print(key, value)