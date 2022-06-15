#!/usr/bin/env python
# coding: utf-8

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')

def dobro(n=0, format=False):
    res = n*2
    return res if format is False else moeda(res)

def metade(n=0, format=False):
    res = n/2
    return res if format is False else moeda(res)

def diminuir(n=0, porc=0, format=False):
    res = (n - (n*(porc/100)))
    return res if format is False else moeda(res)

def aumentar(n=0, porc=0, format=False):
    res = (n + (n*(porc/100)))
    return res if format is False else moeda(res)

def resumo(n=0, a=10, d=5):
    print('-'*33)
    print('RESUMO VALOR'.center(30))
    print('-'*33)
    print(f'Dobro: \t\t\t{dobro(n, True)}')
    print(f'Metade \t\t\t{metade(n, True)}')
    print(f'Aumento de {a}%: \t{aumentar(n, a, True)}')
    print(f'Diminuição de {d}%: \t{diminuir(n, d, True)}')
    print('-'*33)



