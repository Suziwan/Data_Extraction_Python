import pandas as pd

json_file = pd.read_json('./Data/festivals.json')
festivals = pd.DataFrame(json_file['fields'].tolist())
festivals.head()

# Combien y-a-t-il de festivals en PACA ?
total_festivals = len(festivals)
print(f"Il y a {total_festivals} festivals en Provence-Alpes-Côte d'Azur.")

# Quelles sont les 3 villes qui accueillent la majorité des festivals ?
city_counts = festivals.groupby('commune_principale').size().reset_index(name='count')
city_counts = city_counts.sort_values(by='count', ascending=False)
most_festivals_city1 = city_counts.iloc[0]['commune_principale']
most_festivals_city2 = city_counts.iloc[1]['commune_principale']
most_festivals_city3 = city_counts.iloc[2]['commune_principale']
print(f"Les 3 villes avec le plus de festivals sont {most_festivals_city1}, {most_festivals_city2} et {most_festivals_city3}.")

# Quel est le mois de l'année le plus chargé en festivals ?
month_counts = festivals.groupby('mois_habituel_de_debut').size().reset_index(name='count')
month_counts = month_counts.sort_values(by='count', ascending=False)
most_festivals_month = month_counts.iloc[0]['mois_habituel_de_debut']
print(f"Le mois avec le plus de festivals est {most_festivals_month}.")