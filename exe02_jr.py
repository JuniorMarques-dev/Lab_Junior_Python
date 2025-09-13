while True:
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        soma = num1+num2


        
        if soma % 2 ==0:
            print(f'A soma dos nºs é {soma}, portanto é par')

        else:
            print(f'O a soma dos nºs é {soma}, portanto ímpar')

           








        break  
    except ValueError as e:
        print(f'Erro Aqui  {e}  ')