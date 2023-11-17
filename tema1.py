
""" 

Modulul  tema1.py foloseste bibliotecile BeautifulSoup si requests pentru a trimite cereri si a prelua titlul http
si description meta-ul unui site pe baza URL-ului introdus de noi la tastatura

"""


from bs4 import BeautifulSoup
import requests



#dir(requests)
#dir(BeautifulSoup)

def print_html_meta(url):
 """
  Functie care are scopul de a prelua titlul HTML si meta description-ul de la site 

  Parametrii : 
    - url : obiect parametru care contine adresa URL de la site-ul de unde dorim informatiile 

  Returns :
     - nimic, doar printeaza informatiile dorite
  
 """




#cer request  la adresa URL
 back_url=requests.get(my_url)

# verific daca raspunsul are codul 200
 if back_url.status_code==200:
   #in obiectul soup stocam raspunsul html
   soup=BeautifulSoup(back_url.content, 'html.parser')
   #cu metoda .title.string stocam din raspunsul html titlul sub format string
   page_title=soup.title.string
   #in acest obiect, cautam tag-ul meta cu atributul 'name' egal cu 'description'
   meta=soup.find("meta", attrs={"name": "description"})
   #daca am gasit tag-ul meta si contine atributul content, afisam
   if meta and 'content' in meta.attrs:
        # afisam continutul din content 
        meta_description = meta['content']
        print(f'Title: {page_title}')
        print(f'Meta description: {meta_description}')
   else:
        #daca nu gasim tag-ul meta sau atributul content, afisam un mesaj de eroare
        print('Nu s-a gasit meta description pe pagina')
 else:
   #in cazul in care response code-ul request-ului nostru este diferit de 200 ok, printam un mesaj de eroare
   print(f'Nu s-a putut realiza conexiunea, codul de eroare este : {back_url.status_code}')




#luam input de la tastatura adresa URL dorita
my_url=input("Adresa URL este : ")
 #apelul functiei create
print_html_meta(my_url)

