def mysum(*input_nums):
    summed_num = 0
    for num in input_nums:
        summed_num += num
    return summed_num

print(mysum(2,4,5,2,1,2))

def mysum2(numbers, starting_num):
    summed_num = 0
    for num in numbers:
        summed_num += num
    return summed_num+ starting_num

print(mysum2([1,2,3], 4))

def mysum_average(*nums):
    summed_num = 0
    for num in nums:
        summed_num += num
    return summed_num/len(nums)

print(mysum_average(1,5,3,2))

def mysum_strings(*strings):
    min_ = 99999999
    max_ = 0
    summed = 0
    for str_ in strings:
        if len(str_) > max_:
            max_ = len(str_)
        if len(str_) < min_:
            min_ = len(str_)
        summed += len(str_)
    return min_, max_, summed/len(strings)

print(mysum_strings('hello', 'w', 'hi'))

def mysum_objects(*objects):
    summed = 0
    for object in objects:
        try:
            int(object)
        except:
            pass
        else:
            summed += int(object)
    return summed

print(mysum_objects(object, object))
