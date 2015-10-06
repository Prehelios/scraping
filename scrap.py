# -*- coding: cp1252 -*-

# -*- coding: UTF-8 -*-


##### Modules import #####

from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import tldextract
import os

##### Mise en place des Fonctions #####

def Scraping():
    url = input ("Entrer a website à Parser (www.site.com): ")
    r  = requests.get("http://" +url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    for link in soup.find_all('a'):
        print(link.get('href'))

def Extract():
    Extract = input ("Entrer l'url d'un site à extraire : ")
    Ext = tldextract.extract(Extract)
    print (Ext, Ext.subdomain, Ext.domain, Ext.suffix, Ext.registered_domain, '.'.join(Ext[:2])) 


def ExtractHTML():
    url = input("Entrer l'URL du Website :")
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    print(respData)


def ExtractOnly():
    url = input("Entrer l'URL du Website :")
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    balise = input ("Entrer les balises à extraire (p,a,...): ")
    paragraphs = re.findall(r'<' + balise + '>(.*?)</' + balise + '>',str(respData))
    print (paragraphs)



def menu():
    os.system("clear")
    print ("###################################################")
    print ("#               Scraping Website                  #")
    print ("#                Scrap & Extract                  #")
    print ("#               -----------------                 #")
    print ("#                DreAmuS/HelioS                   #")
    print ("###################################################")
    print ("")
    print (" [+] 1 - Scraping les Liens d'un website")
    print (" [+] 2 - Extraire les Noms de Domaines")
    print (" [+] 3 - Extraire HTML")
    print (" [+] 4 - Extraire une partie de l'URL")
    print (" [+] 5 - Quitter")
    print ("-------------------------------------------------)
    choix = int(input("Tapez Votre Choix >>> "))

    if (choix == 1):
        Scraping()
        menu()
    elif (choix ==2):
        Extract()
        menu()
    elif (choix == 3):
        ExtractHTML()
        menu()
    elif (choix == 4):
        ExtractOnly()
        menu()
    elif (choix == 5):
        quit
    else:
        menu()


if __name__=="__main__":
    menu()
