import pandas as pd

def pause():
    input("premi invio per continuare \n")

path='../archive/dataset14-15-16-21-22-23-28-01-02-20.csv'
df=pd.read_csv(path)

print("Numero di sample a null=")
print(df.isnull().sum())

#nessun valore a null



