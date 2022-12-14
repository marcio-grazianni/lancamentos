from datetime import date
import platform
import os
from time import sleep
import psycopg2
import psycopg2.extras

ls = "-" * 60

def retorna_os():
    return platform.system().upper()


def limpa_tela():
    if retorna_os() == "WINDOWS":
        os.system("cls")
    else:
        os.system("clear")


def converte_data_sql(data: date):
    retorno = None
    if data:
        retorno = data.strftime("%Y-%m-%d")
        retorno = retorno[0:4] + "-" + retorno[8:10] + "-" + retorno[5:7]

    return retorno


def retorna_plano_conta(texto: str):
    # A = 55 = ALIMENTACAO
    # F = 49 = FILHAS
    # T = 51 = TRANSPORTE
    # R = 54 = REMEDIOS
    # N = 50 = ANA
    # O = 52 = OUTRAS
    # C = 48 = CASA
    # U = 43 = CASA MATERIAL DE CONSTRUÇÃO

    retorno = None
    if (texto.upper() == "A"):
        retorno = 55
    elif (texto.upper() == "F"):
        retorno = 49
    elif (texto.upper() == "T"):
        retorno = 51
    elif (texto.upper() == "R"):
        retorno = 54
    elif (texto.upper() == "N"):
        retorno = 50
    elif (texto.upper() == "O"):
        retorno = 52
    elif (texto.upper() == "C"):
        retorno = 48
    elif (texto.upper() == "U"):
        retorno = 43

    return retorno


def converte_float(*args):
    return args[0].replace(",", ".")

def mensagem(texto: str, tempo: int):
    print(ls)
    print(texto)
    print(ls)
    sleep(tempo)
