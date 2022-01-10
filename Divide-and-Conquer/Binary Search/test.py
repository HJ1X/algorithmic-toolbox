import sys
import os
import random

random.seed(5)
file = open('input.txt', 'w')
print(" ".join([str( 10 ** 8 + i) for i in range(1 + (3 * 10 ** 4))]), file=file)
print(" ".join([str(random.randint(0, 1000)) for i in range(2)]), file=file)
file.close()
