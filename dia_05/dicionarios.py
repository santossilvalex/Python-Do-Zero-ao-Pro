
# %%

# pares de chave e valor

dados_alex = {
    "nome": "Alexsander",
    "sobrenome": "Santos",
    "idade": 27,
    "data de aniversário": "12/12/1998",
    "filhos": False,
    "formacao" : "ciencias de dados",
    "cidade": "Florianópolis",
        "aonde morou": ["São Paulo", "João Pessoa", "Florianópolis"],
        "cargos": [
            {"função": "gestor de vendas", "empresa": "veneto"},
            {"função": "analista administrativo", "empresa": "interage risk"},
            {"função": "auxiliar administrativo", "empresa": "g. muller"},
            {"função" :"auxiliar administrativo", "empresa": "rede milionaria"},
        ]
    }
print(dados_alex)
# %%
dados_alex["cargos"][3]["empresa"]
# %%
dados_alex["ocupação atual"] = "estudante"
dados_alex["cargo atual"] = "desempregado"
print(dados_alex)
# %%
print("Chaves",(dados_alex.keys()))
print("Valores", (dados_alex.values()))
print("Itens", (dados_alex.items()))
# %%

for i in dados_alex:
    print(i,":",dados_alex[i])
# %%

for item in dados_alex.items():
    print(item) 
# %%
for chave, valor in dados_alex.items():
    print(chave, "->", valor)
# %%
