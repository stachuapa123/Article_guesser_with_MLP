import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import re
def get_nomen():
    nomen = pd.read_csv("mit_artikeln.csv")
    nomen = nomen.rename(columns={"ihm": "Nomen", "none": "Artikel"})
    nomen = nomen[nomen['Artikel'] != "none"]
    nomen['Nomen'] = nomen['Nomen'].str.capitalize()
    nomen.dropna(inplace=True)
    return nomen

def line_read(data): #any word that has number in it is not included
    article = {}
    with open(data, "r", encoding="utf-8") as file: 
        content = file.read()
        ct = 0
        for line in re.split(r"[\n;]", content):
            line = line.strip()
            words = line.split()
            if(len(words)>1 and len(words[1]) > 2):
                if(words[1][0] == '{' and words[1][2] == '}'):
                    print(words[0])
                    has_number = any(char.isdigit() for char in words[0])
                    if not has_number:
                        article[words[0]] = words[1][1]
                    
                    ct+=1
                    
    return article 
def build_dataframe(article_dict):
    df = pd.DataFrame(
        list(article_dict.items()),
        columns=["word", "article"]
    )
    return df
reverse_mapping = {0 : 'Neutrum', 1 : 'Maskulinum', 2 : 'Femininum'}
dmapping = {0 : 'das', 1 : 'der', 2 : 'die'}
dmapping2 = {'n' : 'das', 'm' : 'der', 'f' : 'die'}

def true_artikel(wort, nomen, mapping=dmapping2):
    art = nomen.loc[nomen['Nomen'] == wort]['Artikel'].iloc[0]
    d = mapping[art]
    print(d + " " + wort)

def true_artikel_return(wort, nomen, mapping=dmapping2):
    art = nomen.loc[nomen['Nomen'] == wort]['Artikel'].iloc[0]
    d = mapping[art]
    return d