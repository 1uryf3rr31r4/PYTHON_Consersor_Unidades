import time

medido_massa = {}

def converterMassa(unidade_inicial, unidade_final, valor):
    medida_massa = {'g':1,
                    'kg':1000,
                    'mg':0.001,
                    'lb':453.592,
                    'oz':28.3495}

    if unidade_inicial in medida_massa and unidade_final in medida_massa:
        resultado=(medida_massa[unidade_inicial]/medida_massa[unidade_final])*valor

        print('O resultado da conversão é: {:.2f}'.format(resultado))

    else:
        print('Unidade não suportado')

def converterUnidade(unidade_inicial, unidade_final, valor):
    if unidade_inicial[-1]=='g' or unidade_final[-1]=='g':
        converterMassa(unidade_inicial, unidade_final, valor)
    else:
        print('Unidade não suportada')

unidade_inicial = input('Digite a unidade inical (ex: kg, l, s): ')
unidade_final = input('Digite a unidade final (ex: g, ml, min): ')
valor = float(input('Digite o valor a ser convertido: '))

converterUnidade(unidade_inicial, unidade_final, valor)