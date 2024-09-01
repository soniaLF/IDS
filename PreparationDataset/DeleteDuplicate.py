import pandas as pd

def pause():
    input("Premi invio per continuare")


path='../archive/dataset14-15-16-21-22-23-28-01-02-20.csv'
df=pd.read_csv(path)

print(f"Numero di righe prima di eliminare i duplicati: {df.shape[0]}")

pause()

df_cleaned=df.drop_duplicates(df)

print(f"Numero di righe dopo aver eliminato i duplicati: {df_cleaned.shape[0]}")

#non ci sono duplicati


