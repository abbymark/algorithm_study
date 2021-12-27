boxs, books = input().split()

box_cap = list(map(int, input().split()))
book_size = list(map(int, input().split()))

book_start = 0
break_flag = False
for i in range(len(box_cap)):
    for j in range(book_start, len(book_size)):
        if box_cap[i] >= book_size[j]:
            box_cap[i] -= book_size[j]

            book_start = j + 1

            if j == len(book_size)-1:
                break_flag = True
                break
        else:
            break
    
    if break_flag:
        break

# print(box_cap)
print(sum(box_cap))
