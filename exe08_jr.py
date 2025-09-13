from time import sleep
while True:
    try:
        num = int(input('Digite um número para ver sua tabuada: '))
        for c in range(1,11):
            print(f'{num} x {c:2} = {num*c}')

        break
    except ValueError:
        print('Analisando possível erro...')
        sleep(1)
        print('Você digitou algo inválido tente novamente.')
