def largestMerge(word1: str, word2: str) -> str:
    merge = []
    word1_pos = 0
    word2_pos = 0

    # word1_dict = {}
    # word2_dict = {}

    # for letter in word1:
    #     if letter in word1_dict:
    #         word1_dict[letter] += 1
    #     else:
    #         word1_dict[letter] = 1
    
    # for letter in word2:
    #     if letter in word2_dict:
    #         word2_dict[letter] += 1
    #     else:
    #         word2_dict[letter] = 1
    
    # word1_dict = dict(sorted(word1_dict.items(), reverse=True, key = lambda item: item[0]))
    # word2_dict = dict(sorted(word2_dict.items(), reverse=True, key = lambda item: item[0]))

    word1_num = ""
    word2_num = ""

    for i, letter in enumerate(word1):
        if len(str(ord(letter))) == 3:
            word1_num += '1' + str(ord(letter))
        else:
            word1_num += '10' + str(ord(letter))
    for i, letter in enumerate(word2):
        if len(str(ord(letter))) == 3:
            word2_num += '1' + str(ord(letter))
        else:
            word2_num += '10' + str(ord(letter))

    word1_num = int(word1_num)
    word2_num = int(word2_num)

    while len(word1) != word1_pos or  len(word2) != word2_pos:
        if len(word1) == word1_pos:
            merge.append(word2[word2_pos])
            word2_pos += 1
            continue
        
        if len(word2) == word2_pos:
            merge.append(word1[word1_pos])
            word1_pos += 1
            continue
        
        letter1 = word1[word1_pos]
        letter2 = word2[word2_pos]

        if ord(letter1) > ord(letter2):
            merge.append(letter1)
            word1_pos += 1
            word1_num = str(word1_num)
            if len(word1_num) == 4:
                continue
            if len(str(ord(letter1))) == 2:
                word1_num = int(word1_num[2+len(str(ord(letter1))):])
            else:
                word1_num = int(word1_num[1+len(str(ord(letter1))):])
            # word1_num -= ord(letter1) * (len(word1) - word1_pos)
            # word1_dict[letter1] -= 1
            # if word1_dict[letter1] == 0:
            #     word1_dict.pop(letter1)
        elif ord(letter1) < ord(letter2):
            merge.append(letter2)
            word2_pos += 1
            word2_num = str(word2_num)
            if len(word2_num) == 4:
                continue
            if len(str(ord(letter2))) == 2:
                word2_num = int(word2_num[2+len(str(ord(letter2))):])
            else:
                word2_num = int(word2_num[1+len(str(ord(letter2))):])
            # word2_num -= ord(letter2) * (len(word2) - word2_pos)
            # word2_dict[letter2] -= 1
            # if word2_dict[letter2] == 0:
            #     word2_dict.pop(letter2)
        else:
            word1_rev = word1_num / (10 ** len(str(word1_num)))
            word2_rev = word2_num / (10 ** len(str(word2_num)))


            if word1_rev > word2_rev:
                merge.append(letter1)
                word1_pos += 1
                word1_num = str(word1_num)
                if len(word1_num) == 4:
                    continue
                if len(str(ord(letter1))) == 2:
                    word1_num = int(word1_num[2+len(str(ord(letter1))):])
                else:
                    word1_num = int(word1_num[1+len(str(ord(letter1))):])
            else:
                merge.append(letter2)
                word2_pos += 1
                word2_num = str(word2_num)
                if len(word2_num) == 4:
                    continue
                if len(str(ord(letter2))) == 2:
                    word2_num = int(word2_num[2+len(str(ord(letter2))):])
                else:
                    word2_num = int(word2_num[1+len(str(ord(letter2))):])

            # if ord(next(iter(word1_dict))) > ord(next(iter(word2_dict))):
            #     merge.append(letter1)
            #     word1_pos += 1
            #     word1_dict[letter1] -= 1
            #     if word1_dict[letter1] == 0:
            #         word1_dict.pop(letter1)
            # elif len(word2) != word2_pos:
            #     merge.append(letter2)
            #     word2_pos += 1
            #     word2_dict[letter2] -= 1
            #     if word2_dict[letter2] == 0:
            #         word2_dict.pop(letter2)

    return ''.join(merge)

print(largestMerge(
    "qqqqqqqqqeqeqqeeqqq"
    ,"qqqqqqqqeqqqeeqqeeqqqqqeq"
    ))