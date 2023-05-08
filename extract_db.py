import pandas as pd

# Installer puis importer le connecteur (ex : 'mysql.connector' ou 'sqlite3') :
import sqlite3

# Se connecter à la base de données en inscrivant la bonne configuration :
bank_db = sqlite3.connect('./Data/bank.db')

# Extraire des données à partir de la base :

# Méthode 1 : Utilisation du curseur et renvoi d'un tuple
cursor = bank_db.cursor()
cursor.execute("SELECT nom, prenom, ville FROM client WHERE idclient = ?", ("1", ))
client1 = cursor.fetchone()
print(client1)

# Méthode 2 : Utilisation de 'read_sql_query' et renvoi d'un dataframe
query = '''
SELECT nom, prenom, ville
    FROM client
    WHERE idclient = "1"
'''
client2 = pd.read_sql_query(query, bank_db)
client2

# Fermer la connexion (après avoir effectué toutes les requêtes):
# bank_db.close()

# 1. Donner le nom et le prénom de tous les clients.
query = '''
SELECT nom, prenom 
    FROM client
'''
q1 = pd.read_sql_query(query, bank_db)
q1

# 2. Donner le nom et le prénom des clients habitant à Paris.
query = '''
SELECT nom, prenom 
    FROM client 
    WHERE ville = "Paris"
'''
q2 = pd.read_sql_query(query, bank_db)
q2

# 3. Donner les identifiants des comptes de type Livret A.
cursor.execute("SELECT idcompte FROM compte WHERE type = 'Livret A'")
q3 = cursor.fetchall()
print(q3)

# 4. Donner les identifiants des opérations de débit sur le compte d’identifiant égal à 1.
cursor.execute("SELECT idop FROM operation WHERE idcompte = '1'")
q4 = cursor.fetchall()
print(q4)

# 5. Donner, sans doublon, les identifiants des propriétaires de livret A, classés par ordre croissant.
cursor.execute("SELECT DISTINCT idproprietaire FROM compte WHERE type = 'Livret A' ORDER BY idproprietaire")
q5 = cursor.fetchall()
print(q5)

# 6. Donner l’identifiant des clients n’ayant pas de livret A.
query = '''
SELECT idproprietaire, type
    FROM compte
    WHERE idproprietaire NOT IN
        (SELECT idproprietaire 
        FROM compte 
        WHERE type = 'Livret A')
'''
q6 = pd.read_sql_query(query, bank_db)
q6