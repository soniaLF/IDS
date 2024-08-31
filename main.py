
import pandas as pd
import numpy as np
import matplotlib
from sklearn import metrics

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.expand_frame_repr', False) #Per non tagliare il print


path3='archive/03-01-2018.csv'

ds3 = pd.read_csv(path3)


# print(ds3.head())
# print(ds3.info())

#
# #visualizzazione "tipi" delle feature
# print("\nTipi delle features:")
# for column in ds3.columns:
#     print(f"{column}: {ds3[column].dtype}")

#per un visualizzazione migliore Stampa le feature su righe separate
#
# features = list(set(ds3.columns))
# print("Lista delle features:")
# for feature in features:
#     print(feature)

#############################Converte tutte le feature escluse datatime e label in float gestendo gli errori di conversione mettendo il valore a NaN
#
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
# for col in numeric_cols:
#     ds3[col]=pd.to_numeric(ds3[col], errors='coerce')

#
# print(ds3.dtypes)
#
#
# ds3.to_csv('03-01-2018TipiConvertiti.csv')


path4='03-01-2018TipiConvertiti.csv'

ds4 = pd.read_csv(path4)


print(ds4.head())
print(ds4.info())

# Conta i valori NaN per ogni colonna
nan_count = ds4.isna().sum()

# Mostra il conteggio dei NaN per ogni colonna
print("Conteggio dei valori NaN per ogni colonna:")
print(nan_count)
