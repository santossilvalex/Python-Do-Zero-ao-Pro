#%%

nome_arquivo = "historia.txt"

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()
    print(conteudo)

# Aqui o arquivo é aberto, mas não é lido
open_file = open(nome_arquivo)
# %%
# O conteúdo do arquivo é lido e armazenado na variável "conteudo"
conteudo = open_file.read()
print(conteudo)
# %%
# O arquivo é fechado para liberar recursos do sistema
open_file.close()