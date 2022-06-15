#!/usr/bin/env python
# coding: utf-8

# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

# In[ ]:


def dobro(n):
    return n*2

def metade(n):
    return n/2

def diminuir(n, porc=0):
    return (n - (n*(porc/100)))

def aumentar(n, porc):
    return (n + (n*(porc/100)))

