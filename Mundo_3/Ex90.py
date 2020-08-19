aluno={}
aluno['nome']=str(input('nome: '))
aluno['media']=float(input(f'Média de {aluno["nome"]}: '))
if aluno['media']>=7:
    aluno['situacao']='Aprovado'
elif 5<=aluno['media']<7:
    aluno['situacao']='Recuperacao'
else:
    aluno['situacao']='Reprovado'
print('-='*30)
for k,v in aluno.items():
    print(f'-{k} é igual a {v}')