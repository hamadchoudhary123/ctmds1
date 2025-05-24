import random

from datetime import datetime, timedelta
import pytz

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

@app.command()
def generate_price_curve(for_date_str: str, interval_minutes: int = 60):
    for_date = datetime.strptime(for_date_str, "%Y-%m-%d")
    tz = pytz.timezone("Europe/London")

    start = tz.localize(datetime(for_date.year, for_date.month, for_date.day, 0, 0))
    end = start + timedelta(days=1)

    current = start
    curve =[]
    while current <= end:
        time = current.strftime("%H:%M")
        price = random.random() * 100
        element = {
            "time": time,
            "price": price,
            "currency": "USD",
        }
        curve.append(element)
        current += timedelta(minutes=interval_minutes)
        current = tz.normalize(current)
    print(curve)

if __name__ == "__main__":
    app()
