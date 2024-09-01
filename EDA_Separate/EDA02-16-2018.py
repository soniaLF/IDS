#EDA 02-16-2018


import pandas as pd
import numpy as np
import matplotlib
from sklearn import metrics

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns


def pausa():
    input("Premi Invio per continuare...")


pd.set_option('display.expand_frame_repr', False) #Per non tagliare il print


#---------------------------PULIZIA E SISTEMAZIONE DATASET----------------------------------------------------------------------------
# #
# # ################################### Risoluzione problema datatype########################
# #
# # #IMPORTO IL DATASET nel framework pandas#
# path3='../archive/02-16-2018.csv'
# ds3 = pd.read_csv(path3)
#
#
# #visualizzazione "tipi" delle feature
# print("\nTipi delle features:")
# for column in ds3.columns:
#     print(f"{column}: {ds3[column].dtype}")
#
#
# #array con tutte le feature che devono essere numeriche
# numeric_cols=[
#     'Active Mean', 'Bwd IAT Tot', 'PSH Flag Cnt', 'Pkt Len Std', 'RST Flag Cnt',
#     'Fwd Pkts/b Avg', 'Fwd Byts/b Avg', 'Tot Fwd Pkts', 'Fwd Pkts/s',
#     'Fwd Pkt Len Max', 'Dst Port', 'Fwd Pkt Len Min', 'URG Flag Cnt', 'SYN Flag Cnt',
#     'Flow Byts/s', 'Fwd URG Flags', 'Bwd Pkt Len Max', 'Bwd IAT Min', 'Bwd IAT Mean',
#     'Pkt Len Var', 'Pkt Size Avg', 'ECE Flag Cnt', 'Fwd Act Data Pkts', 'Flow IAT Mean',
#     'Bwd Byts/b Avg', 'Idle Max', 'Fwd PSH Flags', 'Active Std', 'Active Max',
#     'Fwd Seg Size Min', 'CWE Flag Count', 'Bwd IAT Std', 'Bwd Header Len', 'Init Fwd Win Byts',
#     'Bwd PSH Flags', 'Fwd Pkt Len Mean', 'Subflow Bwd Pkts', 'Subflow Fwd Pkts',
#     'TotLen Bwd Pkts', 'Pkt Len Min', 'Bwd Pkts/b Avg', 'Bwd Pkt Len Mean', 'Flow Duration',
#     'FIN Flag Cnt', 'Down/Up Ratio', 'ACK Flag Cnt', 'Fwd IAT Min', 'Idle Std',
#     'Bwd Pkt Len Std', 'Fwd Header Len', 'Fwd IAT Std', 'Fwd Blk Rate Avg',
#     'Active Min', 'Bwd Blk Rate Avg', 'Subflow Bwd Byts', 'Fwd Pkt Len Std',
#     'Fwd Seg Size Avg', 'TotLen Fwd Pkts', 'Bwd IAT Max', 'Flow Pkts/s', 'Bwd Seg Size Avg',
#     'Init Bwd Win Byts', 'Fwd IAT Max', 'Flow IAT Min', 'Fwd IAT Tot', 'Idle Mean',
#     'Tot Bwd Pkts', 'Flow IAT Max', 'Protocol', 'Idle Min', 'Pkt Len Max', 'Fwd IAT Mean',
#     'Bwd URG Flags', 'Subflow Fwd Byts', 'Bwd Pkt Len Min', 'Pkt Len Mean', 'Bwd Pkts/s',
#     'Flow IAT Std'
# ]
#
#
# #1-Trasformo usando pd.to_numeric il dataset in tutte featur numeriche ad eccezione di Timestamp e Label che devono rimanere object
# for col in numeric_cols:
#     ds3[col]=pd.to_numeric(ds3[col], errors='coerce')
#
# print('trasformate tutte le feature in float: \n')
# print(ds3.dtypes)
#
#
#
#
# #2-Controllo ed eventualmente elimino i sample con valori NaN
#
# # Conta i valori NaN per ogni colonna
# nan_count = ds3.isna().sum()
#
# # Mostra il conteggio dei NaN per ogni colonna
# print("Conteggio dei valori NaN per ogni colonna:")
# print(nan_count)
#
#
#
# # Rimuovi tutte le righe che contengono almeno un valore NaN
# ds4 = ds3.dropna()
#
# # Conta i valori NaN per ogni colonna
# nan_count2 = ds4.isna().sum()
# # Mostra il conteggio dei NaN per ogni colonna
# print("Conteggio dei valori NaN per ogni colonna una volta rimossi :")
# print(nan_count2)
#
#
#
#
# # Quanti campioni e quante feature
# print("\nNumero campioni e numero feature",ds4.shape,"\n")
#
#
# #visualizzazione "tipi" delle feature
# print("\nTipi delle features:")
# for column in ds4.columns:
#     print(f"{column}: {ds4[column].dtype}")
#
#
#
#
#
# ds4.to_csv('../archive/02-16-2018TuttiFloat.csv')
#
#
#
# #3-Le feature che devono essere degli int le trasformo usando la funzione asType()
#
# path5='../archive/02-16-2018TuttiFloat.csv'
# ds5=pd.read_csv(path5)
#
# #Rimuovi la colonna 'Unnamed: 0'
# ds5 = ds5.drop(columns=['Unnamed: 0'])
#
# int_features = [
#     'Dst Port',
#     'Protocol',
#     'Flow Duration',
#     'Tot Fwd Pkts',
#     'Tot Bwd Pkts',
#     'TotLen Fwd Pkts',
#     'TotLen Bwd Pkts',
#     'Fwd Pkt Len Max',
#     'Fwd Pkt Len Min',
#     'Bwd Pkt Len Max',
#     'Bwd Pkt Len Min',
#     'Flow IAT Max',
#     'Flow IAT Min',
#     'Fwd IAT Tot',
#     'Fwd IAT Max',
#     'Fwd IAT Min',
#     'Bwd IAT Tot',
#     'Bwd IAT Max',
#     'Bwd IAT Min',
#     'Fwd PSH Flags',
#     'Bwd PSH Flags',
#     'Fwd URG Flags',
#     'Bwd URG Flags',
#     'Fwd Header Len',
#     'Bwd Header Len',
#     'Pkt Len Min',
#     'Pkt Len Max',
#     'FIN Flag Cnt',
#     'SYN Flag Cnt',
#     'RST Flag Cnt',
#     'PSH Flag Cnt',
#     'ACK Flag Cnt',
#     'URG Flag Cnt',
#     'CWE Flag Count',
#     'ECE Flag Cnt',
#     'Down/Up Ratio',
#     'Fwd Byts/b Avg',
#     'Fwd Pkts/b Avg',
#     'Fwd Blk Rate Avg',
#     'Bwd Byts/b Avg',
#     'Bwd Pkts/b Avg',
#     'Bwd Blk Rate Avg',
#     'Subflow Fwd Pkts',
#     'Subflow Fwd Byts',
#     'Subflow Bwd Pkts',
#     'Subflow Bwd Byts',
#     'Init Fwd Win Byts',
#     'Init Bwd Win Byts',
#     'Fwd Act Data Pkts',
#     'Fwd Seg Size Min',
#     'Active Max',
#     'Active Min',
#     'Idle Max',
#     'Idle Min'
# ]
#
#
# for col in int_features:
#     ds5[col]=ds5[col].astype('int64')
#
#
#
# #visualizzazione "tipi" delle feature
# print("\nTipi delle features una volta eseguito il tutto :")
# for column in ds5.columns:
#     print(f"{column}: {ds5[column].dtype}")
#
#
#
#
#
# ####Elimina duplicati
#
# # path3='../archive/02-16-2018.csv'
# #
# # ds3 = pd.read_csv(path3)
# #
# # Stampa il numero di righe prima di eliminare i duplicati
# print(f"Numero di righe prima di eliminare i duplicati: {ds5.shape[0]}")
#
#
#
# # Elimina i duplicati
# df_cleaned = ds5.drop_duplicates()
#
# # Stampa il numero di righe dopo aver eliminato i duplicati
# print(f"Numero di righe dopo aver eliminato i duplicati: {df_cleaned.shape[0]}")
#
#
# # Salva il dataset pulito in un nuovo file CSV
# output_path = '../archive/02-16-2018_cleaned.csv'
# df_cleaned.to_csv(output_path, index=False)
#
# print(f"Dataset pulito salvato in: {output_path}")

#------------------------------------------VISUALIZZAZIONE INFO DATASET-------------------------------------------------------------------------------------------------------------------------------

path3='../archive/02-16-2018_cleaned.csv'

ds3 = pd.read_csv(path3)

#elenco delle feature ottenuto mostrando tutte le colonne del dataset esclusa la label
features = list(set(ds3.columns) - {'Label'})

#per un visualizzazione migliore Stampa le feature su righe separate
print("Lista delle features:")
for feature in features:
    print(feature)

#visualizzazione "tipi" delle feature
print("\nTipi delle features:")
for column in ds3.columns:
    print(f"{column}: {ds3[column].dtype}")



# Quanti campioni e quante feature
print("\nNumero campioni e numero feature",ds3.shape,"\n")

#visualizzazione dei primi 10 sample del dataset
print("\nPrimi 20 campioni del dataset","\n", ds3.head(20))


# Calcola i conteggi per ogni etichetta
counts = ds3['Label'].value_counts()
print(counts)


# Crea un grafico a torta con etichette corrette per ciascuna categoria
plt.pie(counts, autopct="%.1f%%", labels=counts.index)
plt.title("Percentuale di flussi benigni e maligni nel dataset 02-16-2018")
plt.show()




# Conta i valori nulli per colonna
null_counts = ds3.isnull().sum()
print(f"valori null per colonna:  {null_counts}")

