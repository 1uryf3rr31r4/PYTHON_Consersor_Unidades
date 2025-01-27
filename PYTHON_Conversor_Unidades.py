import time

def converterMassa(unidade_inicial, unidade_final, valor):
    medidas_massa = {'g':1,
                    'kg':1000,
                    'mg':0.001,
                    'lb':453.592,
                    'oz':28.3495}
    if unidade_inicial in medidas_massa and unidade_final in medidas_massa:
        resultado=(medidas_massa[unidade_inicial]/medidas_massa[unidade_final])*valor

        print('O resultado da conversão é: {:.2f}'.format(resultado)+f'{unidade_final}')
    else:
        print('Unidade não suportado')

def converterVolume(unidade_inicial, unidade_final, valor):
    medidas_volume = {
        'ml':1,
        'l':1000,
        'gal':3785.41
    }
    if unidade_inicial in medidas_volume and unidade_final in medidas_volume:
        resultado = (medidas_volume[unidade_inicial]/medidas_volume[unidade_final]*valor)
        print('O resultado da conversão é {:.2f}'.format(resultado)+f'{unidade_final}')
    else:
        print('Unidade não surportada')

def converterTempo(unidade_inicial, unidade_final, valor):
    medidas_tempo = {
        's':1,
        'min':60,
        'h':3600,
        'd':86400
    }
    if unidade_inicial in medidas_tempo and unidade_final in medidas_tempo:
        resultado = (medidas_tempo[unidade_inicial]/medidas_tempo[unidade_final]*valor)
        print('O resultado da conversão é {:.2f}'.format(resultado)+f'{unidade_final}')
    else:
        print('Unidade não suportada')

def converterUnidade(unidade_inicial, unidade_final, valor):
    if unidade_inicial[-1]=='g' or unidade_final[-1]=='g':
        converterMassa(unidade_inicial, unidade_final, valor)
    elif unidade_inicial[-1]=='l' or unidade_final[-1]=='l':
        converterVolume(unidade_inicial, unidade_final, valor)
    elif unidade_inicial[-1]=='s' or unidade_final[-1]=='s':
        converterTempo(unidade_inicial, unidade_final, valor)
    else:
        print('Unidade não suportada')

unidade_inicial = input('Digite a unidade inical (ex: kg, l, s): ')
unidade_final = input('Digite a unidade final (ex: g, ml, min): ')
valor = float(input(f'Digite o valor em {unidade_inicial} a ser convertido : '))

converterUnidade(unidade_inicial, unidade_final, valor)