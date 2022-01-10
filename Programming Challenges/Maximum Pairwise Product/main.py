import random
import sys
import os

tests = int(sys.argv[1])
n = int(sys.argv[2])

for i in range(tests):
    print('Test #' + str(i))
    os.system('python3 gen.py ' + str(n) + ' ' + str(i) + ' > input.txt')
    os.system('python3 mpp_model.py < input.txt > main.txt')

    with open('input.txt') as g: input = g.read()
    print(input)
    with open('main.txt') as f: model = f.read()
    print(model)