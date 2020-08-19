def aumentar(preço,taxa,format=False):
    res=preço+(preço*taxa/100)
    return res if format==False else moeda(res)

def diminuir(preço,taxa,format=False):
    res=preço-(preço*taxa/100)
    return res if format==False else moeda(res)

def dobro(preço,format=False):
    res=preço*2
    return res if format==False else moeda(res)
def metade(preço,format=False):
    res=preço/2
    return res if format==False else moeda(res)

def moeda(preço=0,moeda='R$'):
    return f'{moeda} {preço:.2f}'.replace('.',',')






