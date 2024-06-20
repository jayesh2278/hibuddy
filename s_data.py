import requests
import pandas as pd 

df = pd.read_csv('store.csv')

for i in df['url'].to_list():
    response = requests.get(i)
    if response.status_code==int(200):
        print(i)

