"""
modul care citeste anunturile cu keyword 'iphone 15 pro' de pe olx, afiseaza titlurile  + pretul acestora
si le ordoneaza crescator dupa pret
acest modul adauga si parametrul pentru terminal -log pt a putea vedea timpul fiecarui request catre olx
"""

import description
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import functools
import argparse


def decorator(func):
    @functools.wraps(func)
    def wrapper(*argss, **kwargs):
        start_time = time.time()
        value = func(*argss,**kwargs)
        stop_time = time.time()
        if args.log:
            print(f'Durata : {stop_time-start_time:.2f} secunde')
        return value
    return wrapper


@decorator
def read_products():
    """
    functie care va accesa olx.ro pe categoria telefone mobile iphone si va cauta strict anunturile cu
    iphone 15 pro + pretul acestora
    :return: un data frame care contine anunturile dorite
    """

    config = description.get_config()
    #am adaugat extensia pt categorie pt a fi adaugata la link si a cauta strict iphone


    #link complet catre categoria dorita de pe olx
    url = config['URL']['url']

    #requestul
    request = requests.get(url)



    #in acest obiect stochez valoarea din fisierul .ini a produsului dorit
    product = config['product']['product']

    #vector care stocheaza titluri anunt+ preturi
    vec=[]
    if(request.status_code == 200):
        soup = BeautifulSoup(request.text,'html.parser')
        #caut anunturile din pagina html, acea clasa este clasa pt anunturi verificata
        #in inspect element pe olx
        listings = soup.find_all('div',class_ = 'css-1sw7q4x')
        for listing in listings:
            #h6 este tag-ul care contine titlurile anunturilor
            title_element = listing.find('h6')
            #extrag strict anunturile care contin keyword-ul din fisierul .ini
            if title_element and product in title_element.text.lower():
                title = title_element.text
                #p este tagul care contine preturile
                price=listing.find('p').text
                #adaug titlul + pretul in vector
                vec.append({'Produs': title, 'Pret': price})

    #creez un dataframe cu datele colectate
    df = pd.DataFrame(vec, columns=['Produs','Pret'])
    #ordonez dataframe-ul dupa pret in ordine crescatoare
    df = df.sort_values(by='Pret', ascending=True)
    return df




#referinta perser pt argument la terminal
parser = argparse.ArgumentParser()
#specific care este argumentul + actiunea + un help informativ
parser.add_argument("-log", action="store_true",help='Afiseaza timpul pt fiecare request')

args = parser.parse_args()

args.log = True if getattr(args, 'log', False) else False


