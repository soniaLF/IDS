#EDA 02-14-2018
import pandas as pd
import numpy as np
import matplotlib
from sklearn import metrics

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.expand_frame_repr', False) #Per non tagliare il print

#IMPORTO IL DATASET nel framework pandas#
# path1='../archive/02-14-2018.csv'
# ds1 = pd.read_csv(path1)
#
#---------------------------PULIZIA E SISTEMAZIONE DATASET----------------------------------------------------------------------------
#
# # Stampa il numero di righe prima di eliminare i duplicati
# print(f"Numero di righe prima di eliminare i duplicati: {ds1.shape[0]}")
#
# # Elimina i duplicati
# df_cleaned = ds1.drop_duplicates()
#
# # Stampa il numero di righe dopo aver eliminato i duplicati
# print(f"Numero di righe dopo aver eliminato i duplicati: {df_cleaned.shape[0]}")
#
#
# # Salva il dataset pulito in un nuovo file CSV
# output_path = '../archive/02-14-2018_cleaned.csv'
# df_cleaned.to_csv(output_path, index=False)
#
# print(f"Dataset pulito salvato in: {output_path}")


#------------------------------------------VISUALIZZAZIONE INFO DATASET------------------------------------------------------------------------------------

path1='../archive/02-14-2018_cleaned.csv'
ds1 = pd.read_csv(path1)

#elenco delle feature ottenuto mostrando tutte le colonne del dataset esclusa la label
features = list(set(ds1.columns) - {'Label'})

#per un visualizzazione migliore Stampa le feature su righe separate
print("Lista delle features:")
for feature in features:
    print(feature)

#visualizzazione "tipi" delle feature
print("\nTipi delle features:")
for column in ds1.columns:
    print(f"{column}: {ds1[column].dtype}")



# Quanti campioni e quante feature
print("\nNumero campioni e numero feature",ds1.shape,"\n")

#visualizzazione dei primi 20 sample del dataset
print("\nPrimi 20 campioni del dataset","\n", ds1.head(20))


# Calcola i conteggi per ogni etichetta
counts = ds1['Label'].value_counts()
print(counts)




# Crea un grafico a torta con etichette corrette per ciascuna categoria
plt.pie(counts, autopct="%.1f%%", labels=counts.index)
plt.title("Percentuale di flussi benigni e maligni nel dataset 02-14-2018")
plt.show()





