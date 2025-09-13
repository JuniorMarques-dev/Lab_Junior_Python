while True:
    try:
        num1 = int(input('Digite um numero: '))
        num2 = int(input('Digite outro numero: '))
        soma = num1 + num2
    
        
        print(f'A soma do nº {num1} + {num2} = {soma}')

        break

    except ValueError:
        print('Erro de digitação, tente novamente.')