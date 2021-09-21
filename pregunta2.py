# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 22:04:04 2021

@author: Usuario
"""

from pyswip import Prolog

prolog = Prolog()
prolog.consult("base_conocimiento.pl")


##
## Consultas
##


# ¿Juan es hermano de Marcela?
lista = bool(list(prolog.query("hermanode(juan, marcela)")))
print("¿Juan es hermano de Marcela?")
print(lista)

# ¿Carlos es hermano de juan?
lista1 = bool(list(prolog.query("hermanode(carlos, juan)")))
print("¿Carlos es hermano de juan?")
print(lista1)

# ¿Pablo es abuelo de maria?
lista2 = bool(list(prolog.query("abuelode(pablo, maria)")))
print("¿Pablo es abuelo de maria?")
print(lista2)

# ¿María es abuela de pablo?
lista3 = bool(list(prolog.query("abuelode(maria, pablo)")))
print("¿María es abuela de pablo?")
print(lista3)







