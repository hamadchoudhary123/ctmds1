import random

import typer

app = typer.Typer()

def generate_price_curve(n: int) -> list[float]:
    return [random.random() * 100 for i in range(n)]

@app.command()
def pricecurve(
        granularity: str = typer.Option("h", "--granularity", "-g", help="Granularity: h (hourly) or hh (half-hourly)"),
        currency: str = typer.Option("USD", "--currency", "-c", help="Currency code e.g: USD or EUR"),
):

    n = 48 if granularity == 'hh' else 24
    prices = generate_price_curve(n)
    for i, price in enumerate(prices):
        if granularity == 'hh':
            total_minutes = i * 30
        else:
            total_minutes = i * 60

        hours = total_minutes // 60
        minutes = total_minutes % 60
        time_label = f"{hours:02}{minutes:02}"

        print(f"{time_label}: {price:.2f} {currency}")

if __name__ == '__main__':
    app()

