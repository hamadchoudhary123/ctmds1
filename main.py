import random
import sys

if __name__ == '__main__':
    n = int(sys.argv[1])
    for i in range(n):
        price = random.random() * 100
        print(f"{i}: {price:.2f} USD")



