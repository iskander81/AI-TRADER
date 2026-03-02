import ccxt
import os
from dotenv import load_dotenv

load_dotenv()

def get_bybit_client():
    """
    Создаём подключение к Bybit через ccxt
    """
    return ccxt.bybit({
        "apiKey": os.getenv("BYBIT_API_KEY", ""),
        "secret": os.getenv("BYBIT_SECRET", ""),
        "enableRateLimit": True
    })

def fetch_balance():
    """
    Получение баланса
    """
    client = get_bybit_client()
    return client.fetch_balance()

def fetch_ticker(symbol="BTC/USDT"):
    """
    Получение текущей цены
    """
    client = get_bybit_client()
    return client.fetch_ticker(symbol)
