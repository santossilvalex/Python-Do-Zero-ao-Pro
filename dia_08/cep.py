#%%

import requests  #para realizar requisicoes da web
import json     #para trabalhar lista/dicionarios com arquivos json
from tqdm import tqdm  #para mostrar barra de progresso

import pandas as pd


ceps = ["04831100", 
        "01001000",
        "01310-200",
        "20040-002",
        "69005-000",
        "88010-000",
        "05413-010",
        "30130-010",
        "70040-010",
        "60020-000"
        ]

url = "https://viacep.com.br/ws/{cep}/json"
dados = []
for i in tqdm(ceps):
    respostas = requests.get(url.format(cep=i))
    if respostas.status_code == 200:
        dados.append(respostas.json())


dados
#%%
dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", index=False, encoding="utf-8")

#%%

print(dados)

with open("ceps.json", "w", encoding = "utf-8") as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)


# %%
