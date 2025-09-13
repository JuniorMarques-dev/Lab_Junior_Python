'''max() = me mostre o maior numero entre eles
min() = me mostre o menor numero entre eles. '''

while True:
    try:
            num1 = int(input('Digite um número inteiro: '))
            num2 = int(input('Digite outro número inteiro: '))
            num3 = int(input('Digite outro número inteiro: '))

            print(f'Os números digitados foram: {num1}, {num2} e {num3}, o maior é {max(num1,num2,num3)} e o menor é {min(num1,num2,num3)}')
           



            break
    except ValueError:
        print('Erro')#dessa vez não fiz aquela validação mais elaborada para poupar tempo.