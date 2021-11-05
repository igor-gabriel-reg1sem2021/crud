import sqlite3, os

nomeBD = '1'
try:
    conector = sqlite3.connect(nomeBD)
    id = 1
    cursor = conector.cursor()
    cursor.execute('select * from agenda')
    result = cursor.fetchall()
    for contato in result:
        id += 1
    nome = 'Pessoa'
    while nome != '':
        print('id: ', id)
        nome = input('Nome: ')
        if nome != '':
            fone = input('Fone: ')
            cursor.execute('insert into agenda (id, nome, fone) values(?, ?, ?)', (id, nome,fone))
            conector.commit()
            id = id + 1
    cursor.close()
    conector.close()
except sqlite3.Error as error:
    print('Erro: BD não encontrado')
    print('Erro: ', error)
    os.remove(nomeBD)