import requests
from openpyxl import Workbook
import datetime

key = input("Enter you CoinMarketCap API Key: ")

today = datetime.date.today()

file = Workbook()
sheet = file.create_sheet(str(today), 0)

api = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY="

api = api + key

raw_data = requests.get(api).json()
data = raw_data['data']
sheet.append(["Name", "Price", "Volume", "Change(1hr)", "Change(24hr)", "Change(7days)", "Last Updated"])
for currency in data:
    name = currency["name"]
    price = currency["quote"]["USD"]["price"]
    volume = currency["quote"]["USD"]["volume_24h"]
    change_1hr = currency["quote"]["USD"]["percent_change_1h"]
    change_24h = currency["quote"]["USD"]["percent_change_24h"]
    change_7d = currency["quote"]["USD"]["percent_change_7d"]
    last_updated = currency["quote"]["USD"]["last_updated"]
    sheet.append([name, price, volume, change_1hr, change_24h, change_7d, last_updated])
file.save("CryptoCurrencyStats.xlsx")
