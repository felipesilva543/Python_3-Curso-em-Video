#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fatorial(n):
    """
    -> Retorna o fatorial de um número
    param n: Número para fazer o fatorial
    return: Fatorial do numero n
    """
    valor = 1
    for c in range(1, n+1):
        valor *= c
    return valor

def dobro(n):
    return n*2

def triplo(n):
    return n*3

