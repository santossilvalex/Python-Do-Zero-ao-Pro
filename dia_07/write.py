# %%

nome_arquivo = "historia_02.txt"


txt = "porém sinto que o teste deu certo, pois o arquivo foi criado e o texto foi adicionado a ele."

with open(nome_arquivo, mode ="a") as open_file:  
    open_file.write(txt)
# %%
