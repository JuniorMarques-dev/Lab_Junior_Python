while True:
    try:
        num1 = int(input('Digite um nº: '))

        print(f'O nº digitado foi {num1} e seu antecessor é {num1-1} e seu sucessor é {num1+1}')


        break



    except ValueError:
        print('Erro de digitação, apenas numeros.')
