while True:
    nome = input('Digite seu nome: ')
    ano = int(input('Digite o ano que você nasceu: '))
    if ano >= 1922 and ano <= 2021 :
        print('Nome do usuário é {} e sua idade é {}'.format(nome, 2022 - ano))
        break
    print('Por avor, preencher o campo corretamente.')