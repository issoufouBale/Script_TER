# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:26:20 2022

@author: maham
"""

import shutil
folder_path = 'C:/Users/maham/Documents/Master 2 SID/TER Projet/storage/storage'
import os
ext = ('html', 'pdf')
for path, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith(ext):
            id_ = os.path.split(path)[-1]
            extention = filename.split('.')[-1]
            print(id_+'.'+extention)

            src_path = os.path.join(path, filename)
            dst_path = os.path.join(r'C:/Users/maham/Documents/Master 2 SID/TER Projet/new_folder1', id_+'.'+extention)
            shutil.copy(src_path, dst_path)


from PyPDF2 import PdfReader
import pandas as pd


path = 'C:/Users/maham/Documents/Master 2 SID/TER Projet/new_folder/'
results = []
for file in os.listdir(path):
    if file.endswith('pdf'):
        reader = PdfReader(path + file)
        number_of_pages = len(reader.pages)
        results.append([file, number_of_pages])
print(results)

print(len(results))


df = pd.DataFrame(results, columns=["name",'page_number'])
df.to_csv('list.csv', index=False)

d =  pd.read_csv('C:/Users/maham/Documents/Master 2 SID/TER Projet/new_folder/list.csv')

print(d.head()) 


#html scraping
import os
import csv
import requests
from bs4 import BeautifulSoup

path = 'C:/Users/maham/Documents/Master 2 SID/TER Projet/new_folder/'
for file in os.listdir(path):
    if file.endswith('html'):
        
        #print(file)
        requete = requests.get('http://' + 'S3ZX6WZP.html')
        page = requete.content
        soup = BeautifulSoup(page, 'html.parser')

        # Extract all of the links in the HTML
        links = soup.find_all("a")

        # Print the links
        for link in links:
            print(link.get("href"))


import urllib 
from urllib.request import urlopen

path = 'C:/Users/maham/Documents/Master 2 SID/TER Projet/new_folder/'
for file in os.listdir(path):
    if file.endswith('html'):
        #requete = requests.get('http://' + file)
        #page = requete.content
        html = urlopen(file)
        contents = html.read()
        print(contents)


#abstract  extraction
import PyPDF2
import os

folder = 'C:/Users/maham/Documents/Master 2 SID/TER Projet/new_folder1/'
for filename in os.listdir(folder):
    if filename.endswith(".pdf"):
        pdf_file = os.path.join(folder, filename)
        with open(pdf_file, "rb") as f:
            pdf = PyPDF2.PdfFileReader(f)
            text = "".join([pdf.getPage(i).extractText() for i in range(pdf.numPages)])
            if "Abstract" in text:
                abstract_start = text.index("Abstract") + len("Abstract")
                abstract_end = text.index("\n", abstract_start)
                abstract = text[abstract_start:abstract_end].strip()
                print("Abstract for {}: {}".format(filename, abstract))
            else:
                print("No abstract found for {}".format(filename))

# Author extraction
import os
import PyPDF2

folder =  'C:/Users/maham/Documents/Master 2 SID/TER Projet/new_folder1/'

for filename in os.listdir(folder):
    if filename.endswith(".pdf"):
        pdf_file = open(os.path.join(folder, filename), "rb")
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        pdf_info = pdf_reader.getDocumentInfo()
        author = pdf_info.author

        print("Author of", filename, ":", author)
        pdf_file.close()


