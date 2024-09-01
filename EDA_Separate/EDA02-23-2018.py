#EDA 02-23-2018

import pandas as pd
import numpy as np
import matplotlib
from sklearn import metrics

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.expand_frame_repr', False) #Per non tagliare il print

#---------------------------PULIZIA E SISTEMAZIONE DATASET----------------------------------------------------------------------------

#IMPORTO IL DATASET nel framework pandas
#
# path5='../archive/02-23-2018.csv'
# ds5 = pd.read_csv(path5)

# # Stampa il numero di righe prima di eliminare i duplicati
# print(f"Numero di righe prima di eliminare i duplicati: {ds5.shape[0]}")
#
# # Elimina i duplicati
# df_cleaned = ds5.drop_duplicates()
#
# # Stampa il numero di righe dopo aver eliminato i duplicati
# print(f"Numero di righe dopo aver eliminato i duplicati: {df_cleaned.shape[0]}")
#
#
# # Salva il dataset pulito in un nuovo file CSV
# output_path = '../archive/02-23-2018_cleaned.csv'
# df_cleaned.to_csv(output_path, index=False)
#
# print(f"Dataset pulito salvato in: {output_path}")

#
# #------------------------------------------VISUALIZZAZIONE INFO DATASET------------------------------------------------------------------------------------

# path5='../archive/02-23-2018_cleaned.csv'
# ds5 = pd.read_csv(path5)
#
# #elenco delle feature ottenuto mostrando tutte le colonne del dataset esclusa la label
# features = list(set(ds5.columns) - {'Label'})
#
# #per un visualizzazione migliore Stampa le feature su righe separate
# print("Lista delle features:")
# for feature in features:
#     print(feature)
#
# #visualizzazione "tipi" delle feature
# print("\nTipi delle features:")
# for column in ds5.columns:
#     print(f"{column}: {ds5[column].dtype}")
#
#
#
# # Quanti campioni e quante feature
# print("\nNumero campioni e numero feature",ds5.shape,"\n")
#
# #visualizzazione dei primi 10 sample del dataset
# print("\nPrimi 20 campioni del dataset","\n", ds5.head(20))
#
#
# # Calcola i conteggi per ogni etichetta
# counts = ds5['Label'].value_counts()
# print(counts)
#
#
# # Crea un grafico a torta con etichette corrette per ciascuna categoria
# plt.pie(counts, autopct="%.1f%%", labels=counts.index)
# plt.title("Percentuale di flussi benigni e maligni nel dataset 02-23-2018")
# plt.show()
#
#
#
# Conta i valori nulli per colonna
# null_counts = ds.isnull().sum()
# print(f"valori null per colonna:  {null_counts}")