print('Menu dos arquivos: \nDigite 0 para sair do meunu \nDigite 1 para cirar um bancoi\nDigite 2 para ler um banco \nDigite 3 para inserir um'
          'dado no banco \nDigite 4 para deletar um dado no banco')
i = input('Digite sua entrada: ')
while i != '0':
    if i == '1':
        import create
        i = input('Digite sua entrada: ')
    elif i == '2':
        import read
        i = input('Digite sua entrada: ')
    elif i == '3':
        import update
        i = input('Digite sua entrada: ')
    elif i == '4':
        import delete
        i = input('Digite sua entrada: ')
    elif i == '0':
        print('Você saiu')
    else:i = input('A entrada que você digitou não é valida, digite uma entrada valida: ')