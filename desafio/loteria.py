#%%
import random

def get_input():
    while True:
        try:
            numero_usuario = int(input("Entre com um número: "))
        
        except ValueError as err:
            print("Valor inválido!")
            continue
                
        if 1 <= numero_usuario <= 100:
            return numero_usuario

        print("Valor inválido! O valor deve ser entre 1 e 100")


def check_numbers(sorteio, usuario):
    if sorteio == usuario:
        print("Parabéns! Você se tornou um milionário imaginario!.")
        return True

    elif usuario > sorteio:
        print("Número muito alto. Tente um número menor!")
        return False

    else:
        print("Número muito baixo. Tente um número maior!")
        return False


numero_sorteio = random.randint(1,100)

for i in range(3):

    numero_usuario = get_input()
    if check_numbers(sorteio=numero_sorteio, usuario=numero_usuario):
        break

else:
    print("Suas tentativas acabaram!!")
# %%   
