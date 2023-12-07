# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:11:10 2023

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

article_body_file = "article_body_file.txt"

# Nombre del archivo HTML original
archivo_original = "index-ARTICLE.html"


# Nombre del nuevo archivo HTML duplicado
archivo_duplicado = "index-ARTICLE-" + article_name + ".html"

#Separamos los parrafos del article_body

# Contenido HTML de ejemplo
with open(article_body_file, 'r', encoding='utf-8') as file:
    article_body = file.read()
    
    
parrafos = article_body.split("<h2>")

article_struct = []

first_parraf = True

for parrafo in parrafos:
    #Nos saltamos el primero por estar vacio
    if first_parraf:
        first_parraf = False
        continue
    
    parrafo = "<h2>" + parrafo
    
    # Expresión regular para encontrar el contenido entre <p> y <br>
    patron_h2 = re.compile(r'<h2>(.*?)<\/h2>', re.DOTALL)

    # Busca coincidencias en el texto
    heading = patron_h2.findall(parrafo)[0].replace("\"", "")
    
    heading_texts = []
    
    # Expresión regular para encontrar el contenido entre <p> y <br>
    patron_p_br = re.compile(r'<p>(.*?)<br\s*\/?>', re.DOTALL)

    # Busca coincidencias en el texto
    texto = patron_p_br.findall(parrafo)
    
    heading_texts.append(texto[0].replace("<br>", "").replace("</p>", "").replace("<p>", "").replace("\t", "").replace("\n", ""))
    
    # Expresión regular para encontrar el contenido entre <br> y </p>
    patron_p_br = re.compile(r'<br>(.*?)<\/p>', re.DOTALL)

    # Busca coincidencias en el texto
    texto = parrafo.split("<br>")
    
    first_text = True
    
    for text in texto:
        
        if first_text:
            first_text = False
            continue
        
        if len(text) > 10:
            heading_texts.append(text.replace("<br>", "").replace("</p>", "").replace("<p>", "").replace("\t", "").replace("\n", ""))
    

    article_struct.append((heading, heading_texts))
    
    heading_texts = []

# Número de párrafos en el archivo
num_parrafos = len(article_struct)

#Escribimos en el articulo
# Lee el contenido del archivo original
with open(archivo_original, 'r', encoding='utf-8') as file:
    contenido_original = file.read()
    
    #Inclusion titulos
    patron_title_1 = re.compile(fr'<h2 id="title_1" class="home-page-main-title fadeIn-element">(.*?)<\/h2>', re.DOTALL)
    contenido_original = patron_title_1.sub(f'<h2 id="title_1" class="home-page-main-title fadeIn-element">{title_1}</h2>', contenido_original)

    patron_title_2 = re.compile(fr'<h1 id="title_2" class="home-page-main-title fadeIn-element">(.*?)<\/h1>', re.DOTALL)
    contenido_original = patron_title_2.sub(f'<h1 id="title_2" class="home-page-main-title fadeIn-element">{title_2}</h1>', contenido_original)

    #Inclusion parrafos
    patron_section = re.compile(fr'<!-- about start -->(.*?)<!-- about end -->', re.DOTALL)
    section = patron_section.findall(contenido_original)
    final_section = ''
    
    section_counter = 0
    for article in article_struct:
        section_counter += 1
        
        new_section = section
        
        heading = str(article[0])
        
        patron_heading = re.compile(fr'<h3 class="section-heading article-heading">(.*?)<\/h3>', re.DOTALL)
        new_section = patron_heading.sub(f'<h3 class="section-heading article-heading">{heading}</h3>', new_section[0])
        
        #Inclusion de parrafos
        patron_parrafo = re.compile(fr'<p>(.*?)<\/p>', re.DOTALL)
        parrafo_final = ''
        
        for parrafo_text in article[1]:
            #parrafo_new = patron_parrafo.sub(f'<p ="parrafo">(.*?)<\/p>{str(parrafo_text)}</p>', parrafo_base)
            parrafo_final = parrafo_final + "<p>" + parrafo_text + "</p>\n"
            
        
        new_section = patron_parrafo.sub(f'{parrafo_final}', new_section)
        
        final_section = final_section + new_section
    contenido_original = patron_section.sub(f'<!-- about start -->{final_section}<!-- about end -->', contenido_original)

# Escribe el nuevo contenido en el archivo duplicado
with open(archivo_duplicado, 'w', encoding='utf-8') as file:
    file.write(contenido_original)

print(f"Archivo duplicado y modificado: {archivo_duplicado}")
