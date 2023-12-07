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
    
    
    
# Nombre del archivo HTML original
archivo_original = "index.html"


# Nombre del nuevo archivo HTML duplicado
archivo_duplicado = "index-updated.html"