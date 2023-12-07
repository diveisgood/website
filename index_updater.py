# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 13:36:33 2023

@author: mirdo
"""

import shutil
import sys
import re


try:
    title = "Dive into Diversity: A Journey Through the Different Types of Diving"
    title = title
except Exception as e:
    print(e)
    raise e
    
try:
    title_1 = title.split(":")[0]
    article_name = title_1.replace(" ", "")
    title_2 = title.split(":")[1]
except Exception as e:
    print(e)
    raise e
    
article_file_name = "index-ARTICLE-DiveintoDiversity.html"
    
# Nombre del archivo HTML original
archivo_original = "index.html"


# Nombre del nuevo archivo HTML duplicado
archivo_duplicado = "index-updated.html"


#Escribimos en el index
# Lee el contenido del archivo original
with open(archivo_original, 'r', encoding='utf-8') as file:
    contenido_original = file.read()
    

    #Inclusion parrafos
    patron_articulo = re.compile(fr'<!-- preview image start -->(.*?)<!-- preview image end -->', re.DOTALL)
    article = patron_articulo.findall(contenido_original)
    
    patron_new_article = re.compile(fr'<!-- new article -->(.*?)<!-- new article -->', re.DOTALL)
    
    new_article = article[0]
    
    patron_article_href = re.compile(fr'<a class="zoom-item" href="(.*?)" target="_top">Read</a>', re.DOTALL)
    href = article_file_name 
    new_article = patron_article_href.sub(f'<a class="zoom-item" href="{href}" target="_top">Read</a>', new_article)
    
    patron_article_img = re.compile(fr'<img alt="Image Preview" src="(.*?)">', re.DOTALL)
    url = "https://images.pexels.com/photos/37542/divers-scuba-reef-underwater-37542.jpeg"
    new_article = patron_article_img.sub(f'<img alt="Image Preview" src="{url}">', new_article)
    
    patron_article_title = re.compile(fr'<h2 class="article-title">(.*?)</h2>', re.DOTALL)
    new_article = patron_article_title.sub(f'<h2>{title}</h2>', new_article)
    
    new_article = "\n<!-- preview image start -->" + new_article + "<!-- preview image end -->\n" + "\n<!-- new article --><!-- new article -->"
    
    contenido_original = patron_new_article.sub(f'{new_article}', contenido_original)
    
    number_artics = len(article) + 1
    
    #Modificacion numero articulos
    patron_number = re.compile(fr'<h3 class="facts-counter-number">(.*?)<\/h3>', re.DOTALL)
    contenido_original = patron_number.sub(f'<h3 class="facts-counter-number">{str(number_artics)}</h3>', contenido_original)
    
# Escribe el nuevo contenido en el archivo duplicado
with open(archivo_duplicado, 'w', encoding='utf-8') as file:
    file.write(contenido_original)

print(f"Archivo duplicado y modificado: {archivo_duplicado}")
    