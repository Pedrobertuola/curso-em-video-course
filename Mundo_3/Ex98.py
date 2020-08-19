from time import sleep
def contador(a,b,c):
    print('-=-'*30)
    print(f'Contando de {a} até {b} de {c} em {c}.')
    print('-=-'*30)
    if a<b:
        for d in range(a,b+1,c):
            print(f'{d}',end=' ')
            sleep(0.2)
    elif a>b:
        for d in range(a,b-1,-c):
            print(d,end=' ')
            sleep(0.2)
    print('Fim')


contador(1,10,1)
print('-=-'*30)
contador(10,0,2)
print('-=-'*30)
print('Agora é a sua vez de personalizar a contagem!')
I=int(input('Inicio: '))
F=int(input('Fim: '))
P=int(input('Passo: '))
contador(I,F,P)