import sys
import os

tests = int(sys.argv[1])
n = int(sys.argv[2])

for i in range(tests):
    print('Test #' + str(i))
    # generating tests and storing in "input" file
    os.system('python3 gen.py ' + str(n) + ' ' + str(i) + ' > input.txt')

    # passing tests to main and model solutions
    os.system('python3 ml_sol.py < input.txt > model.txt')
    os.system('python3 maximum_loot.py < input.txt > main.txt')

    with open('input.txt') as g:
        input = g.read()
    print('Input: ', input)
    with open('main.txt') as f:
        main = f.read()
    print('Main_sol: ', main, end='')
    with open('model.txt') as m:
        model = m.read()
    print('Model_sol: ', model)
    if model != main: break
