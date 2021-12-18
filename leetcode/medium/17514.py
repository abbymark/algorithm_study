def largestMerge(word1: str, word2: str) -> str:
    merge = []
    word1_pos = 0
    word2_pos = 0

    word1_dict = {}
    word2_dict = {}

    for letter in word1:
        if letter in word1_dict:
            word1_dict[letter] += 1
        else:
            word1_dict[letter] = 1
    
    for letter in word2:
        if letter in word2_dict:
            word2_dict[letter] += 1
        else:
            word2_dict[letter] = 1
    
    word1_dict = dict(sorted(word1_dict.items(), reverse=True, key = lambda item: item[0]))
    word2_dict = dict(sorted(word2_dict.items(), reverse=True, key = lambda item: item[0]))

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
            word1_dict[letter1] -= 1
            if word1_dict[letter1] == 0:
                word1_dict.pop(letter1)
        elif ord(letter1) < ord(letter2):
            merge.append(letter2)
            word2_pos += 1
            word2_dict[letter2] -= 1
            if word2_dict[letter2] == 0:
                word2_dict.pop(letter2)
        else:
            if ord(next(iter(word1_dict))) > ord(next(iter(word2_dict))):
                merge.append(letter1)
                word1_pos += 1
                word1_dict[letter1] -= 1
                if word1_dict[letter1] == 0:
                    word1_dict.pop(letter1)
            elif len(word2) != word2_pos:
                merge.append(letter2)
                word2_pos += 1
                word2_dict[letter2] -= 1
                if word2_dict[letter2] == 0:
                    word2_dict.pop(letter2)

    return ''.join(merge)

print(largestMerge("cabaa", "bcaaa"))