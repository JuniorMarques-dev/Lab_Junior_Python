from time import sleep

while True:
    try:
        print('=-='*10)

        num = int(input('Digite um número inteiro: '))

        if num > 0: #corrigido eu havia posto >=1: não estava errado, mas assim é mais legível( positivo = maior que zero) leitura mental.
            print(f'O número digitado é {num} positivo e seu dobro é {num*2}')

        elif num == 0:
            print(f'O número digitado foi {num}, e ele não tem valor multiplicativo!.')

        else:
            print(f'O número digitado foi {num}, o seu valor absoluto é {abs(num)}')
        

        print('=-='*10)






        break
    except ValueError:
        print('Analisando possível erro...')
        sleep(1)
        print('Erro de digitação, por favor apenas números INTEIROS.')