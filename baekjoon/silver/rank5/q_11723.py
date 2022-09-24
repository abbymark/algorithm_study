M = int(input())

v_set = set()

for i in range(M):
    command = input().split()
    if len(command) == 2:
        num = int(command[1])
    command = command[0]
    if num >= 1 and num <= 20:
        if command == 'add':
            v_set.add(num)
        elif command == 'remove':
            # if num in v_set:
            try:
                v_set.remove(num)
            except:
                pass
        elif command == 'check':
            if num in v_set:
                print('1')
            else:
                print('0')
        elif command == 'toggle':
            if num in v_set:
                v_set.remove(num)
            else:
                v_set.add(num)
        elif command == 'all':
            v_set = set(i for i in range(1, 21))
        elif command == 'empty':
            v_set = set()