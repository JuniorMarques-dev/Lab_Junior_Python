from math import sqrt
while True:
    try:
        num = int(input('Digite um nº: '))
        if num < 0:
            print('A proposta é básica e não chegou na contagem de conjunto de números complexos, por enquanto sem negativos.')
        print(f'O nº digitado foi {num}\nSeu dobro é {num*2}\nSeu triplo é {num*3}\nE sua raiz é {sqrt(num):.2f}')

        break
    except ValueError as e:
        print(f'Erro, pois tentou ver raiz negativa de {num}, vai com calma')


        '''from math import sqrt

while True:
    try:
        # Pede o número
        num = int(input('Digite um nº: '))

        # Verifica número negativo
        if num < 0:
            print('A proposta é básica e não trabalhamos com números negativos por enquanto. Tente outro número!')
            continue  # volta pro início do loop

        # Calcula e mostra os resultados
        print(f'O nº digitado foi {num}')
        print(f'Seu dobro é {num*2}')
        print(f'Seu triplo é {num*3}')
        print(f'Sua raiz quadrada é {sqrt(num):.2f}')

        break  # sai do loop quando tudo estiver correto

    except ValueError:
        # Captura erros de digitação (não inteiro)
        print('Erro de digitação! Digite apenas números inteiros.')
'''