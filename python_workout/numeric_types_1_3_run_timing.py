def run_timing():
    run_times = []
    while True:
        run_time = input('Enter 10 km run time: ')
        if not run_time and len(run_times) != 0:
            print(f'Average of {sum(run_times)/len(run_times)}, over {len(run_times)} runs')
            break
        elif not run_times:
            break
        run_times.append(int(run_time))

# run_timing()

def run_timing2():
    float_num = float(input())
    before = int(input())
    after = int(input())

    print(f'{float_num:{before}.{after}f}')

run_timing2()