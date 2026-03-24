# %%
dados = {}

while True:
    frase = input ("Digite uma frase:")
    if frase == "":
        break

    if frase not in dados:
        dados[frase] = 1
    else:
        dados[frase] += 1
        
for frase, quantidade in dados.items():
    print(f'A frase "{frase}" foi digitada {quantidade} vezes.')
