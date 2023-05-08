import pandas as pd

patents = pd.read_csv('./Data/patents.csv', delimiter=";", header = 0)
patents.head()

# Supprimer les quatres dernières colonnes
patents.drop('de_libelle', inplace=True, axis=1)
patents.drop('de_sd1_libelle', inplace=True, axis=1)
patents.drop('de_sd2_libelle', inplace=True, axis=1)
patents.drop('fe_id', inplace=True, axis=1)
patents.head()