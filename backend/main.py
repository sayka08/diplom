from binance.client import Client

API_KEY = "H41KUAh7MBiCmOAB9Ek06BHrOlHFmzg8yudmF2kHDZKgQkiTkPdf6L4X6WKxsHPs"
API_SECRET = "yl08bT6WojwAi2pJtjyy1TW2HLpykQPI7jvVhtxbqH0aNpBqkCrptjX6uA9Dw4az"

client = Client(API_KEY, API_SECRET)

price = client.get_symbol_ticker(symbol="BTCUSDT")
print(f"Текущая цена BTC: {price['price']}")
