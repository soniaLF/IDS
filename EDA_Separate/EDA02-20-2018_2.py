import pandas as pd
import numpy as np
import matplotlib
from sklearn import metrics

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns



#IMPORTO IL DATASET nel framework pandas

path4='../archive/02-20-2018_cleaned.csv'

ds5 = pd.read_csv(path4)



# Stampa il numero di righe prima di eliminare i duplicati
print(f"Numero di righe prima di eliminare i duplicati: {ds5.shape[0]}")

# Elimina i duplicati
df_cleaned = ds5.drop_duplicates()

# Stampa il numero di righe dopo aver eliminato i duplicati
print(f"Numero di righe dopo aver eliminato i duplicati: {df_cleaned.shape[0]}")


# Salva il dataset pulito in un nuovo file CSV
output_path = '../archive/02-20-2018_cleaned2.csv'
df_cleaned.to_csv(output_path, index=False)

print(f"Dataset pulito salvato in: {output_path}")