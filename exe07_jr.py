while True:
    try:
        nota1 = float(input('Digite a 1ª nota: '))
        nota2 = float (input('Digite a 2ª nota: '))
        media = (nota1 + nota2) / 2
        print(f'A nota do aluno foi {nota1+nota2:.2f} e sua media é {media} ')


        break
    except ValueError:
        print('Erro! Digite apenas o que foi pedido.')
