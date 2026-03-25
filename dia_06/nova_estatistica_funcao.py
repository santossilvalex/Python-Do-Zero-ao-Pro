#%%
def soma(a:float, b:float, *args:float):
    valores = [a,b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args:float):
    return soma(a, b, *args) / (len(args) + 2)

a = float(input("Informe o valor A:"))
b = float(input("Informe o valor B:"))
c = float(input("Informe o valor C:"))

print("média:", media(a, b, c))


# %%