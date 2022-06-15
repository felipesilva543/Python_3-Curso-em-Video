#!/usr/bin/env python
# coding: utf-8

# In[1]:


def dobro(n=0):
    return n*2

def metade(n=0):
    return n/2

def diminuir(n=0, porc=0):
    return (n - (n*(porc/100)))

def aumentar(n=0, porc=0):
    return (n + (n*(porc/100)))

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')
    

