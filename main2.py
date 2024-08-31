import pandas as pd

path3='03-01-2018TipiConvertiti.csv'

ds3 = pd.read_csv(path3)

int_features = [
    'Dst Port',
    'Protocol',
    'Flow Duration',
    'Tot Fwd Pkts',
    'Tot Bwd Pkts',
    'TotLen Fwd Pkts',
    'TotLen Bwd Pkts',
    'Fwd Pkt Len Max',
    'Fwd Pkt Len Min',
    'Bwd Pkt Len Max',
    'Bwd Pkt Len Min',
    'Flow IAT Max',
    'Flow IAT Min',
    'Fwd IAT Tot',
    'Fwd IAT Max',
    'Fwd IAT Min',
    'Bwd IAT Tot',
    'Bwd IAT Max',
    'Bwd IAT Min',
    'Fwd PSH Flags',
    'Bwd PSH Flags',
    'Fwd URG Flags',
    'Bwd URG Flags',
    'Fwd Header Len',
    'Bwd Header Len',
    'Pkt Len Min',
    'Pkt Len Max',
    'FIN Flag Cnt',
    'SYN Flag Cnt',
    'RST Flag Cnt',
    'PSH Flag Cnt',
    'ACK Flag Cnt',
    'URG Flag Cnt',
    'CWE Flag Count',
    'ECE Flag Cnt',
    'Down/Up Ratio',
    'Fwd Byts/b Avg',
    'Fwd Pkts/b Avg',
    'Fwd Blk Rate Avg',
    'Bwd Byts/b Avg',
    'Bwd Pkts/b Avg',
    'Bwd Blk Rate Avg',
    'Subflow Fwd Pkts',
    'Subflow Fwd Byts',
    'Subflow Bwd Pkts',
    'Subflow Bwd Byts',
    'Init Fwd Win Byts',
    'Init Bwd Win Byts',
    'Fwd Act Data Pkts',
    'Fwd Seg Size Min',
    'Active Max',
    'Active Min',
    'Idle Max',
    'Idle Min'
]


float_features = [
    'Fwd Pkt Len Mean',
    'Fwd Pkt Len Std',
    'Bwd Pkt Len Mean',
    'Bwd Pkt Len Std',
    'Flow Byts/s',
    'Flow Pkts/s',
    'Flow IAT Mean',
    'Flow IAT Std',
    'Fwd IAT Mean',
    'Fwd IAT Std',
    'Bwd IAT Mean',
    'Bwd IAT Std',
    'Pkt Len Mean',
    'Pkt Len Std',
    'Pkt Len Var',
    'Pkt Size Avg',
    'Fwd Seg Size Avg',
    'Bwd Seg Size Avg',
    'Active Mean',
    'Active Std',
    'Idle Mean',
    'Idle Std'
]

# ds3['Fwd Pkt Len Mean']=ds3['Fwd Pkt Len Mean'].astype('float')

# for col in int_features:
#     ds3[col]=ds3[col].astype('int')
#
# for col in float_features:
#     ds3[col]=ds3[col].astype('float')

print(ds3.dtypes)

# Conta i valori NaN per ogni colonna
nan_count = ds3.isna().sum()

# Mostra il conteggio dei NaN per ogni colonna
print("Conteggio dei valori NaN per ogni colonna:")
print(nan_count)


# Rimuovi tutte le righe che contengono almeno un valore NaN
ds4 = ds3.dropna()

# Conta i valori NaN per ogni colonna
nan_count2 = ds4.isna().sum()
# Mostra il conteggio dei NaN per ogni colonna
print("Conteggio dei valori NaN per ogni colonna:")
print(nan_count2)



# Quanti campioni e quante feature
print("\nNumero campioni e numero feature",ds4.shape,"\n")


#visualizzazione "tipi" delle feature
print("\nTipi delle features:")
for column in ds4.columns:
    print(f"{column}: {ds4[column].dtype}")



# Rimuovi la colonna 'Unnamed: 0'
ds4 = ds4.drop(columns=['Unnamed: 0'])



#visualizzazione "tipi" delle feature
print("\nTipi delle features:")
for column in ds4.columns:
    print(f"{column}: {ds4[column].dtype}")



#ora devo convertire le colonne che devono essere int invece di float

for col in int_features:
    ds4[col]=ds4[col].astype('int64')



#visualizzazione "tipi" delle feature
print("\nTipi delle features:")
for column in ds4.columns:
    print(f"{column}: {ds4[column].dtype}")


    
ds4.to_csv('archive/03-01-2018NoWarning.csv')
