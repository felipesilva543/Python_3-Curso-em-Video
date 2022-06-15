#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')
    


# In[ ]:




