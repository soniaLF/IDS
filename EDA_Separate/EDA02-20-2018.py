#EDA 02-20-2018

import pandas as pd
import numpy as np
import matplotlib
from sklearn import metrics

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.expand_frame_repr', False) #Per non tagliare il print


# realizzata solo per permettere di mettere il codice in pausa!
def pause():
    input("Premi <ENTER> per continuare ...\n")

#IMPORTO IL DATASET nel framework pandas

path4='../archive/02-20-2018.csv'

ds4 = pd.read_csv(path4)

#------------------------------------------VISUALIZZAZIONE INFO DATASET------------------------------------------------------------------------------------

#elenco delle feature ottenuto mostrando tutte le colonne del dataset esclusa la label
features = list(set(ds4.columns) - {'Label'})

#per un visualizzazione migliore Stampa le feature su righe separate
print("Lista delle features:")
for feature in features:
    print(feature)

#visualizzazione "tipi" delle feature
print("\nTipi delle features:")
for column in ds4.columns:
    print(f"{column}: {ds4[column].dtype}")



# Quanti campioni e quante feature
print("\nNumero campioni e numero feature",ds4.shape,"\n")

#visualizzazione dei primi 10 sample del dataset
print("\nPrimi 20 campioni del dataset","\n", ds4.head(20))


# Calcola i conteggi per ogni etichetta
counts = ds4['Label'].value_counts()
print(counts)


# Crea un grafico a torta con etichette corrette per ciascuna categoria
plt.pie(counts, autopct="%.1f%%", labels=counts.index)
plt.title("Percentuale di flussi benigni e maligni nel dataset 02-20-2018")
plt.show()


# Identifica le colonne extra da rimuovere
extra_features = ['Flow ID', 'Src IP', 'Src Port', 'Dst IP']

# Flow ID: object
# Src IP: object
# Src Port: int64
# Dst IP:

# Rimuovi le colonne extra
df_202_cleaned = ds4.drop(columns=extra_features)


# Salva il dataset pulito
df_202_cleaned.to_csv('../archive/02-20-2018_cleaned.csv', index=False)


# Verifica le colonne del dataset pulito
print(df_202_cleaned.columns)

# Opzionale: Verifica alcune righe per assicurarti che il dataset sia corretto
print(df_202_cleaned.head())

