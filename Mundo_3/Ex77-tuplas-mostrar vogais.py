palavras=('estudar','programar','curso','ajuda','futuro','praticar')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in'aeiou':
            print(letra,end='')








#palavras=('estudar','programar','curso','ajuda','futuro','praticar')
#for p in palavras:
    #print(f'\nNa palavra {p.upper()} temos ', end='')
    #for letra in p:
        #if letra.lower() in 'aeiou':
           # print(letra,end=' ')