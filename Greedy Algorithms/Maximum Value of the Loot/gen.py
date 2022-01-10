import random
import sys

n = int(sys.argv[1])
myseed = int(sys.argv[2])
random.seed(myseed)

print(n, end=' ')
print(str(random.randint(1, 10 ** 3)), end=' ')
print(" ".join([str(random.randint(1, 2 * 10 ** 6)) for i in range((2 * n))]))