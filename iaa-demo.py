import pandas as pd
from sklearn.metrics import cohen_kappa_score

data = pd.read_csv("pos-annotationen.csv")       # einlesen der Daten
data = data.fillna('None')      # Leere Felder mit dem String "None" füllen

iaa = cohen_kappa_score(data['anno1'], data['anno2'])       # Cohen's Kappa für anno1 und anno2 berechnen

print(round(iaa, 2))
