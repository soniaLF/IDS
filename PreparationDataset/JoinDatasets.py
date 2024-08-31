
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

import pandas as pd

# # Carica i dataset
# df_202 = pd.read_csv('../archive/02-20-2018.csv')  # Dataset del 20-02-2018
# df_other = pd.read_csv('../archive/02-16-2018.csv')  # Uno degli altri dataset con 80 feature
#
# # Identifica le colonne extra nel dataset del 20-02-2018
# extra_columns = set(df_202.columns) - set(df_other.columns)
#
# # Visualizza le feature extra
# print("Extra features nel dataset 20-02-2018:")
# print(extra_columns)



# Elenco dei file CSV per ogni giorno
file_paths = [
    '../archive/02-14-2018.csv',
    '../archive/02-15-2018.csv',
    '../archive/02-16-2018.csv',
    '../archive/02-20-2018_cleaned.csv',
    '../archive/02-21-2018.csv',
    '../archive/02-22-2018.csv',
    '../archive/02-23-2018.csv',
    '../archive/02-28-2018.csv',
    '../archive/03-01-2018.csv',
    '../archive/03-02-2018.csv'
]

# Lettura e concatenazione di tutti i file CSV in un unico DataFrame
dfs = [pd.read_csv(file_path, low_memory=False) for file_path in file_paths]
df_combined = pd.concat(dfs, ignore_index=True)

# Salvare il DataFrame combinato in un file CSV
df_combined.to_csv('../archive/datasetUnito.csv', index=False)

