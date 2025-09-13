from time import sleep
while True:
    try:
        lado1 = int(input('Digite um número inteiro: '))
        lado2 = int(input('Digite outro número inteiro: '))
        lado3 = int(input('Digite mais um número inteiro: '))
        lados = [lado1,lado2,lado3]#mudei do outro exercício pois agora quis tentar com uma lista
        print(f'Os nºs digitados foram {lado1}, {lado2}, {lado3}, e o maior dentre eles é {max(lados)} e o menor é {min(lados)}.')
        sleep(0.5)
        print('Pera ai...acho que da pra fazer um triângulo em...')
        
        if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
            sleep(1)
            print('Olha só e não é que deu mesmo?')
            
            if lado1 == lado2 == lado3:
                print('Parabéns você criou um Triângulo Equilátero.')

            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                print('Parabéns você criou um Triângulo Isósceles.')
            else:
                print('Parabéns você criou um Triângulo Escaleno.')
        else:
            sleep(0.5)
            print('Analisando...')
            sleep(1)
            print('Desculpe me enganei...')
            print('Os números digitados não formam um triângulo.')



        break

    except ValueError:
        print('Erro de digitação, apenas números Inteiros.')