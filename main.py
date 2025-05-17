import random

import typer

app = typer.Typer()

def generate_price_curve(n: int) -> list[float]:
    prices = []
    for i in range(n):
        price = random.random() * 100
        prices.append(price)
    return prices

@app.command()
def pricecurve(granularity: str = typer.Option("h", "--granularity", "-g", help="Granularity: h (hourly) or hh (half-hourly)")):
    n = 48 if granularity == 'hh' else 24
    prices = generate_price_curve(n)
    for i, price in enumerate(prices):
        print(f"{i}: {price:.2f} USD")

if __name__ == '__main__':
    app()

