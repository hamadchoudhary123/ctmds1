import random
import sys

def generate_price_curve(n: int) -> list[float] :
    prices = []
    for i in range(n):
        price = random.random() * 100
        prices.append(price)
    return prices

if __name__ == '__main__':
    n = int(sys.argv[1])
    prices = generate_price_curve(n)
    for i, price in enumerate(prices):
        print(f"{i}: {price:.2f} USD")



