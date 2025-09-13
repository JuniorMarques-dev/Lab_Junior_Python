from time import sleep
while True:
    try:
        num = int(input('Digite um número: '))
        
        if num % 2 == 0:
            print(f'O número digitado foi {num}, e ele é par, e {num}² é {pow(num,2)}')#geralmente uso num**2, mas resolvi testar o pow pela 1ª vez
        else:
            print(f'O número digitado foi {num}, e ele é ímpar, e o triplo de {num} = {num*3}')    



        break
    except ValueError:
        print('Analizando possível erro...')
        sleep(1)
        print('Erro de digitação, digite um número válido.')