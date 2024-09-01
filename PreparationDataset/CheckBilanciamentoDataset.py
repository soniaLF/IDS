import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path='../archive/dataset14-15-16-21-22-23-28-01-02-20.csv'
df=pd.read_csv(path)

target_column='Label'

class_counts=df[target_column].value_counts()

# print("\n Distribuzione delle classi nel dataset:")
# print(class_counts)

plt.figure(figsize=(10, 6))
sns.barplot(x=class_counts.index, y=class_counts.values)

plt.title('Distribuzione delle classi nel dataset')
plt.xlabel('Classi')
plt.ylabel('Conteggio')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

#Mostra il grafico
plt.tight_layout()
plt.show()

