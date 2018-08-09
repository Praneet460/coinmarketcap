import requests
from prettytable import PrettyTable

key = input("Enter you CoinMarketCap API Key: ")


api = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY="

api = api + key

raw_data = requests.get(api).json()
data = raw_data['data']

table = PrettyTable()

for currency in data:
    name = currency["name"]
    price = currency["quote"]["USD"]["price"]
    volume = currency["quote"]["USD"]["volume_24h"]
    change_1hr = currency["quote"]["USD"]["percent_change_1h"]
    change_24h = currency["quote"]["USD"]["percent_change_24h"]
    change_7d = currency["quote"]["USD"]["percent_change_7d"]
    last_updated = currency["quote"]["USD"]["last_updated"]
    table.add_row([name, price, volume, change_1hr, change_24h, change_7d, last_updated])

table.field_names = ["Name", "Price", "Volume", "Change(1hr)", "Change(24hr)", "Change(7days)", "Last Updated"]

print(table)
