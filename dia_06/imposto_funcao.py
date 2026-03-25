# %%
def calc_imposto(preco:float, tx_base:float, **kwargs):
    imposto =  preco + tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]

    return imposto
# %%
impostos_gerais ={
    "municipal": 0.21,
    "estadual": 0.15,       
    "federal": 0.18,
    "internacional": 0.25       
}

calc_imposto(1000, 0.05, **impostos_gerais) 
# %%
