import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

def get_nomen():
    nomen = pd.read_csv("mit_artikeln.csv")
    nomen = nomen.rename(columns={"ihm": "Nomen", "none": "Artikel"})
    nomen = nomen[nomen['Artikel'] != "none"]
    nomen['Nomen'] = nomen['Nomen'].str.capitalize()
    nomen.dropna(inplace=True)
    return nomen


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