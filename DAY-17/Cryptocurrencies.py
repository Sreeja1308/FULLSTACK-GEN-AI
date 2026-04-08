#top 10 Cryptocurrencies by market Cap 
import requests
import pandas as pd

url="https://api.coingecko.com/api/v3/coins/markets"

params={
    "vs_currency":"usd",
    "order":"market_cap_desc",
    "per_page":10,
    "page":1,
    "sparkline":False
}

response=requests.get(url,params=params)
crypto_data=response.json()

df=pd.DataFrame(crypto_data)

df=df[["name","symbol","current_price","market_cap","price_change_percentage_24h"]]
df.columns=["Name","Symbol","Current Price","Market Cap","price_change_percentage_24h"]
df=df.sort_values(by="Market Cap",ascending=False)
print("Top 10 Cryptocurrencies by Market Cap")
print(df)
