def soma(a:float, b:float):
    return a + b

def media (a:float, b:float):
    return soma(a, b) / 2

a = float(input("Informe um numero:"))
b = float(input("Informe outro numero:"))

print("média:", media(a, b))