def maior(*n):
    if len(n)>0:
        print(f'O maior valor é {max(n)}')
    else:
        print('Não foram informados valores')

maior(3,4,5,9,4,3,2)
maior()

