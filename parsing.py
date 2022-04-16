from bs4 import BeautifulSoup
import requests
import time

import sqlb


def dannie():
    timen = time.strftime("%D").replace("/", ".")
    soup = BeautifulSoup(
        requests.get(f"https://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To={timen}").text,
        "lxml")
    katalog = soup.find(class_="data").text.split("\n")
    while '' in katalog:
        katalog.remove('')
    x = ['Цифр. код', 'Букв. код', 'Единиц', 'Валюта', 'Курс']
    for i in x:
        katalog.remove(i)
    return katalog

def lang():
    katalog = dannie()
    name = []
    for i in range(3, len(katalog), 5):
        name.append(katalog[i])
    return name

def katirovka():
    katalog = dannie()
    kurs = []
    for i in range(4, len(katalog), 5):
        kurs.append(katalog[i])
    return kurs

def kurs():
    a=""
    kurs=katirovka()
    name=lang()
    for i in range(len(name)):
        a+=name[i]
        a+=": "
        a+=kurs[i]
        a+=" RUB"
        a+="\n"
    return a

def name_val():
    a = ""
    name = lang()
    for i in range(len(name)):
        a += name[i]
        a += ","
    return a

def sht():
    katalog = dannie()
    kol_vo=[]
    for i in range(2, len(katalog), 5):
        kol_vo.append(katalog[i])
    return kol_vo

def rub(message):
    name=lang()
    kol=sht()
    k=katirovka()
    summ=0
    for i in range(len(name)):
     react=sqlb.inf(message)
     if react == "NULL":
         pass
     if react!="NULL":
         print(k,'\n',kol[i])
         l=float(k[i].replace(",","."))/float(kol[i])
         print(react[0])
         summ+=react[0]*l
     return summ




