from random import choice

while True:
    try:
         Ola = str(input('Olá sou o primeiro programa do Junior, qual seu nome?: ')).strip().upper()
         cumprimento = 'Que prazer!', 'Muito bom te conhecer', 'É isso ai tamo junto !'
         lista = choice(cumprimento)
         msg_errado = 'Eita! não foi isso que eu perguntei', 'Está tudo bem? Você não parece ter lido nada do que eu disse','Fala comigo direito por favor!!'
         lista_errado = choice(msg_errado)
        

         if Ola == 'FILHO DA PUTA':
             'FILHA DA PUTA' in Ola.upper()
             print('Que coisa feia...ta achando que ta falando com quem?')

         elif Ola.replace(' ','').isalpha():  
             print(f'{Ola.title()} {lista}')

         else:
             print(lista_errado)

         break
    except ValueError as e:
        print(f'Erro {e}: Arruma aqui.')