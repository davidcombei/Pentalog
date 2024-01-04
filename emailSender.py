"""
modul care compara pretul fiecarui anunt gasit cu pretul din .ini si in cazul in care exista un anunt 
cu pretul mai mic se trimite un email automat la adresa de email din acelasi fisier .ini
"""

import products
import smtplib
import description





#password app : oqcf wzcn xpqx qkkw
def send_email(pret):
    """

    :param pret: parametru pt pretul de prag din fisierul .ini
    :return: nimic, aceasta functie trimite e-mail-ul si este apelata in functia check_price in cazul
    in care s-a gasit un anunt sub pretul dorit
    """
    #datele fisierului config.ini
    config = description.get_config()
    #valoarea de prag pt pret
    prag=config['X']['X']
    #sender + receiver email
    sender_email = 'daviddbd22@gmail.com'
    receiver_email = config['e-mail']['e-mail']
    #mesajul trimis
    subject = 'Pretul produsului a scazut!'
    message = f'Pretul produsului dorit a scazut sub pragul de {prag}'
    text = f'Subiect : {subject}\n\n {message}'
    #conectare la SMTP pe portul 587
    server=smtplib.SMTP("smtp.gmail.com", 587)
    #pornire server
    server.starttls()
    #logare cu email-ul meu + app password-ul google
    server.login(sender_email,'oqcfwzcnxpqxqkkw')
    #trimitere email
    server.sendmail(sender_email, receiver_email, text)


def check_price():
    """
    functie care compara preturile cu pretul de prag si apeleaza functia send_email in cazul in care
    conditia este indeplinita
    :return:  nimic
    """

    config = description.get_config()
    prag_price = int(config['X']['X'])

    #preiau data frame-ul din modulul products.py
    items = products.read_products()
    print(items)

    #iterez prin data frame,
    for index, item in items.iterrows():
        #transform toate string-urile de pe coloana pret in valori numerice
        item_price = int(''.join(filter(str.isdigit, item['Pret'])))
        #compar preturile
        if item_price < int(prag_price):
            #daca conditia este indeplinita, se trimite un e-mail
            send_email(prag_price)
            print('Un email a fost trimis')
            break

#check_price()

