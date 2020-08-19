from datetime import date
def voto(x):
    if 18<=x<70:
        print('Voto obrigatório!')
    elif 16<=x<18 or x>=70:
        print('Voto opcional')
    else:
        print('Voto negado')





H=date.today().year
N=int(input('Digite o ano de nascimento: '))
idade=H-N
print(f'Você está com {idade} anos')
voto(idade)