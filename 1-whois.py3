#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2-whois.py3 CODIGOS

"""
  Esse arquivo executa o WHOIS

  Modificado em 19  de Outubro de 2021

"""

import sys
try:
    import whois
except:
    sys.exit("[!] Instale a biblioteca nmap com o comando: pip3 install python-whois")

dominio = "teste.com.br"
consultaWhois = whois.whois(dominio)

print(consultaWhois.email) #1
print(consultaWhois["email"]) #1
print(consultaWhois.text) #3