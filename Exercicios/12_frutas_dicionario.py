# %%
#Solicite ao usuário o nome de uma fruta e 
# exiba o preço correspondente.
fruta = input("Qual fruta você deseja? : ")

frutas = {
"Banana":"R$6,79",
"Uva":"R$12,99",
"Pera":"R$13,99",
"Laranja":"R$4,65",
"Limão":"R$2,89",
"Goiaba":"R$5,85",
"Abacaxi":"R$7,79",
"Jaca":"R$13,89",
"Maçã":"R$9,59",
}

if fruta in frutas:
	print("O preço da", fruta, "por quilo é de:", frutas[fruta])
else:
	print("Fruta não encontrada em nosso catálogo.")
# %%
