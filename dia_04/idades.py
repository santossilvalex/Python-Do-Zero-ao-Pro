# %%
idades = [12, 43, 23, 56, 78, 18]
print(idades)

# %%
idades.append(10)
print(idades)

# %%
idades.remove(43)
print(idades)   
# %%

idades =[]

while True:
    idade = input("Entre com a idade: ")

    if idade == "":
        break

    idades.append(int(idade))

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)

print("MEDIA: ", media)
print("MINIMO: ", minimo)
print("MAXIMO: ", maximo)
print("QUANTIDADE: ", qtde)