# %%

def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    '''juros_compostos serve para calcular o retorno financeiro de um investimento a parir de um aporte.
    Deve-se considerar o valor, a taxa atual do juros e o tempo(em anos) para o cálculo do valor final a ser retornado.

    aporte: 
        valor inicial investido 
    taxa: 
        taxa de juros em decimal (ex: 10% = 0.1) 
    anos: 
        tempo em anos que o dinheiro ficará investido 
    '''
    return aporte * (1 + taxa) ** anos
# %%
juros_compostos(aporte=2000, taxa=1, anos=5)
# %%
