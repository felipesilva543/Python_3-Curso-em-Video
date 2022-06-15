def leia_dinheiro(txt = ''):
    valido = False
    while not valido:
        valor = input(txt).strip().replace(',','.')
        if valor == '':
            print(f'\"\" é invalido!')
        elif valor.isalpha():
            print(f'{valor} é invalido!')
        else:
            valido = True
            return float(valor)
            