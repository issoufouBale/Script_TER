# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 21:47:08 2023

@author: maham
"""

import os
import csv
import requests
from bs4 import BeautifulSoup
import urllib 
from urllib.request import urlopen

path = 'C:/Users/maham/Documents/Master 2 SID/TER Projet/new_folder/'
for file in os.listdir(path):
    if file.endswith('html'):
        print(file)
        #requete = requests.get('http://' + file)
        #page = requete.content
        html = urlopen(file)
        contents = html.read()
        print(contents)
        
import os
from bs4 import BeautifulSoup

lisT = []
# Set the directory you want to start from
rootDir = 'C:/Users/maham/Documents/Master 2 SID/TER Projet/new_folder/'

for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        # Check if the file is an HTML file
        if fname.endswith('.html'):
            #print(fname)
            # Open the file and read its contents
            with open(os.path.join(dirName, fname), 'r',encoding='Latin1') as f:
                html = f.read()
            # Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(html, 'html.parser')
            # Extract the data you want using the soup object
            data = soup.find_all('p')
            page_numbers = soup.find_all("span", class_="page-number")
            print(page_numbers)
            for abstract in data:
               # print(abstract.text)
                lisT.append([fname,abstract.text])
                print(lisT)
            # #d = soup.find_parents('p')
            # lang = soup.html['lang']
            # print(f'Language: {lang}')
            # lisT.append([fname,lang])
            # print(lisT)

import pandas as pd

df = pd.DataFrame(lisT, columns=["key",'Lang'])
df.to_csv('List_Lang.csv', index=False)

d =  pd.read_csv('C:/Users/maham/Documents/Master 2 SID/TER Projet/List_Lang.csv')

print(d.head(40))


#how to extract author html
from bs4 import BeautifulSoup
import os

folder =  'C:/Users/maham/Documents/Master 2 SID/TER Projet/new_folder1/'

for filename in os.listdir(folder):
    with open(os.path.join(folder, filename)) as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")
    author = soup.find("meta", attrs={"name": "author"})
    if author:
        print(f"Author for {filename}: {author['content']}")
    else:
        print(f"Author not found for {filename}")