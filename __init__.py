"""
Acest pachet contine modulele necesare proiectului de la cursul de Python in colaborare cu Pentalog
acest pachet afiseaza meta description+title page ale site-ului olx, cauta anunturile pe baza keyword-ului
iphone 15 pro, preia titlul anuntului si pretul acestuia, ordoneaza crescator preturile, iar daca
pretul este sub pretul din fisierul de configurare, se trimite un email la adresa din acelasi fisier
"""
import description
import emailSender

#apelul functiei create in modulul anterior care va citi din config.ini adresa URL si afisa titlul HTML si description meta-ul
description.print_html_meta()
emailSender.check_price()
