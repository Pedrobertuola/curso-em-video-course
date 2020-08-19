from datetime import datetime
cadastro={}
cadastro['Nome']=str(input('Nome: '))
nasc=int(input('data de nascimento: '))
cadastro['idade']=datetime.now().year-nasc
cadastro['ctps']=int(input('Carteira de trabalho (0 não tem): '))
if cadastro['ctps']!=0:
    cadastro['contratacao']=int(input('Digite o ano de contratação: '))
    cadastro['salario']=float(input('Salário R$'))
    cadastro['aposentadoria']=cadastro['idade']+((cadastro['contratacao']+35)-datetime.now().year)
print('-='*30)
print(cadastro)
for k,v in cadastro.items():
    print(f'{k} é igual a {v}')