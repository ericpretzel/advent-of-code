# calculates execution time of a script

import timeit
import sys
from math import floor, log10

# round to n sig figs
round_to_n = lambda x, n: round(x, -int(floor(log10(abs(x)))) + (n - 1))

def print_execution_time(path):
    try:
        with open(path) as f:
            code = "".join(f.readlines())
    except:
        print('File not found:', path)
        exit()
    
    # fix input file path
    input_file_path = path[:path.rindex('/')] + '/input.in'
    code = code.replace('input.in', input_file_path)

    print('Running:', path)
    print('-'*10 + 'Program output' + '-'*10)
    execution_time = timeit.timeit(code, number=1)
    print('-'*(20+len('Program output')))
    print()
    print('Execution time:', round_to_n(execution_time, 4), 's')

if len(sys.argv) > 2:
    print('usage:', 'python3 execution_time.py optional/path/to/file')
    exit()
elif len(sys.argv) == 2:
    path = sys.argv[1]
    print_execution_time(path)
    exit()

print('Solution to run (if one file, put part=0)')
year = input('Year: ')
day = input('Day: ').zfill(2)
part = input('Part: ')
if part == '0': part = 'solution'
else: part = 'part'+part

path = f'{year}/day{day}/{part}.py'

print_execution_time(path)