E=str(input('Digite uma expressão'))
N=E.count('(')
N2=E.count(')')
if N==N2:
    print('A expressão é valida')
else:
    print('A expressão não é valida')
print(N)
print(N2)