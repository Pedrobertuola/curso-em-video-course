def notas(*n,sit=False):
    """"Funçao para analisar notas e situação de vários alunos
    param n: uma ou mais notas dos alunos
    param sit: valor opcional, indicando se deve ou não adicionar a situaçao
    returm: dicionario com varias informações sobre a situaçao da turm
    """



    r=dict()
    r['Total']=len(n)
    r['Maior']=max(n)
    r['Menor']=min(n)
    r['Media']=sum(n)/len(n)
    if sit:
        if r['Media']>=7:
            r['Situacao']='Boa'
        elif r['Media']>=5:
            r['Situacao']='Razoavel'
        else:
            r['Situacao']='Ruim'
    return r

#programaprincipal
resp=notas(5,6,1,sit=True)
print(resp)
help(notas)
