# %%
alex = ["Alexsander", 27, 
        1.73, "Namorando",
        ["Desempregado", "Estudante"],
        ["RPG", "Games", "Musicas"],
        ["SP", "PB", "SC"]
    ]
print(len(alex))


alex[6][2]
# %%
tamanho_lista = len(alex)
pos = tamanho_lista - 1

atividades = alex[pos]

alex[pos][len(atividades) - 1]
# %%
