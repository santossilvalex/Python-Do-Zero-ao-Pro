#%%
import requests
import pandas as pd

url = "https://api.opendota.com/api/heroStats"
resposta = requests.get(url)

df = pd.DataFrame(resposta.json())
df.to_csv("dota2.csv", sep=";",index=False, encoding="utf-8")

# %%
