import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import re
import numpy as np
import torch 
from torch.nn.utils.rnn import pad_sequence

def get_nomen():
    nomen = pd.read_csv("mit_artikeln.csv")
    nomen = nomen.rename(columns={"ihm": "Nomen", "none": "Artikel"})
    nomen = nomen[nomen['Artikel'] != "none"]
    nomen['Nomen'] = nomen['Nomen'].str.capitalize()
    nomen.dropna(inplace=True)
    return nomen

def line_read(data, verbose=False): #any word that has number in it is not included
    article = {}
    types = ('m', 'f', 'n')
    with open(data, "r", encoding="utf-8") as file: 
        content = file.read()
        ct = 0
        for line in re.split(r"[\n;]", content):
            line = line.strip()
            words = line.split()
            if(len(words)>1 and len(words[1]) > 2):
                if(words[1][0] == '{' and words[1][2] == '}'):
                    if verbose:
                        print(words[0])
                    has_number = any(char.isdigit() for char in words[0])
                    if not has_number and words[1][1] in types:
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

letters = ['a',  'b'	,'c',	'd',	'e',	'f',	'g',	'h'	,   'i',	'j',	'k',	'l',	'm',
              	'n',	'o',	'p',	'q',	'r',	's',	't',	'u',	'v',	'w',
                    	'x',	'y',	'z'	,'ä'	,'ö'	,'ü',	'ß', '0', '-']

def word_prep_rnn(w):
    w = w.lower()
    r = list(w)
    for i in range(len(r)):
        if r[i] not in letters:
            r[i] = '0'
    return r

def onehot(cat):
    n = len(cat)
    oh = []
    for i in range(n):
        vec = [0] * n
        vec[i] = 1
        oh.append(vec)
    oh.append([0]*n)
    return oh

OneHot = onehot(letters)
hot_mapping = dict(zip(letters, OneHot))

def hotX(w):
    r = word_prep_rnn(w)
    HX = [hot_mapping[letter] for letter in r]
    #flatHX = [item for sublist in HX for item in sublist] #flatten the list of lists into a vector
    return np.array(HX, dtype='int8')

def hotX_torch(w):
    r = word_prep_rnn(w)
    HX = [hot_mapping[letter] for letter in r]
    #flatHX = [item for sublist in HX for item in sublist] #flatten the list of lists into a vector
    return torch.tensor(HX)

article_to_idx = {"m": 0, "f": 1, "n": 2}

def makeXy(df):
    X = df['word'].values
    X = pad_sequence([hotX_torch(w) for w in X], batch_first=True)
    y = df['article'].values
    y = [article_to_idx[q] for q in y]
    return X, y

