from requests.api import head
import csv
import pandas as pd

url = 'http://api.coincap.io/v2/assets'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data={})
json_file = response.json()
cryptos = []
csvheader = ['SYMBOL', 'NAME', 'PRICE (USD)']

for x in json_file['data']:
    listing = [x['symbol'],x['name'],x['priceUsd']]
    cryptos.append(listing)

with open('./Data/crypto.csv','w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(csvheader)
    writer.writerows(cryptos)

print('Data saved to file "crypto.csv"')

read_cryptos = pd.read_csv('./Data/crypto.csv')
read_cryptos.head()