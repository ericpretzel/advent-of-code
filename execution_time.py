# calculates execution time of a script

import timeit
import sys

if len(sys.argv) != 2:
    print('usage:', 'python3 execution_time.py path/to/file')
    exit()

path = sys.argv[1]
with open(path) as f:
    code = "".join(f.readlines())

# fix input file path
input_file_path = path[:path.rindex('/')] + '/input.in'
code = code.replace('input.in', input_file_path)

print('-'*10 + 'Program output' + '-'*10)
execution_time = timeit.timeit(code, number=1)
print('-'*(20+len('Program output')))
print()
print('Execution time:', round(execution_time*1000, ndigits=4), 'ms')