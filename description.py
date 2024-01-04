"""

Modulul  description.py foloseste bibliotecile BeautifulSoup,configparser si requests pentru a prelua adresa URL din fisierul .ini
si a prelua titlul http si description meta-ul unui site pe baza URL-ului

"""

from bs4 import BeautifulSoup
import requests
import configparser

def get_config():
    """
    Functie care citeste configuratia dintr-un fisier .ini

    Returns:
        Un obiect de configuratie configparser
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def print_html_meta():
    """
     Functie care are scopul de a prelua titlul HTML si meta description-ul de la URL-ul din fisierul config.ini

     Returns :
        - nimic, doar printeaza informatiile dorite

    """
    #obiect referinta la functia get_config()
    config = get_config()

    #import url-ul din fisierul config.ini
    url = config['URL']['url']

    # cer request  la adresa URL
    back_url = requests.get(url)

    # verific daca raspunsul are codul 200
    if back_url.status_code == 200:
        # in obiectul soup stocam raspunsul html
        soup = BeautifulSoup(back_url.content, 'html.parser')
        # cu metoda .title.string stocam din raspunsul html titlul sub format string
        page_title = soup.title.string
        # in acest obiect, cautam tag-ul meta cu atributul 'name' egal cu 'description'
        meta = soup.find("meta", attrs={"name": "description"})
        # daca am gasit tag-ul meta si contine atributul content, afisam
        if meta and 'content' in meta.attrs:
            # afisam continutul din content
            meta_description = meta['content']
            print(f'Title: {page_title}')
            print(f'Meta description: {meta_description}')
        else:
            # daca nu gasim tag-ul meta sau atributul content, afisam un mesaj de eroare
            print('Nu s-a gasit meta description pe pagina')
    else:
        # in cazul in care response code-ul request-ului nostru este diferit de 200 ok, printam un mesaj de eroare
        print(f'Nu s-a putut realiza conexiunea, codul de eroare este : {back_url.status_code}')



