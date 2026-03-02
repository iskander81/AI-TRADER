# main.py
import ccxt
import os
from dotenv import load_dotenv

load_dotenv()

def test_connection():
    try:
        exchange = ccxt.bybit({
            "apiKey": os.getenv("BYBIT_API_KEY", ""),
            "secret": os.getenv("BYBIT_SECRET", ""),
            "enableRateLimit": True
        })
        balance = exchange.fetch_balance()
        print("Connected successfully!")
        print("Balance:", balance['total'])
    except Exception as e:
        print("Error connecting:", e)

if __name__ == "__main__":
    test_connection()
