import pandas as pd
import numpy as np

# Définir le nombre de lignes à générer
num_rows = 100  # Par exemple 100 lignes

# Générer des données aléatoires pour chaque colonne
length = np.random.randint(50, 150, size=num_rows)  # Longueur des paquets (50 à 150 octets)
proto = np.random.choice([6, 17, 1], size=num_rows)  # Protocole (TCP=6, UDP=17, ICMP=1)
ttl = np.random.randint(30, 255, size=num_rows)  # Valeur TTL (30 à 255)
entropy = np.random.uniform(1, 8, size=num_rows)  # Entropie (valeur flottante entre 1 et 8)

# Anomalie (0 = normal, -1 = anomalie, généré aléatoirement avec une probabilité de 10% pour les anomal>
is_anomaly = np.random.choice([0, -1], size=num_rows, p=[0.9, 0.1])

# Créer un DataFrame
df = pd.DataFrame({
    'length': length,
    'proto': proto,
    'ttl': ttl,
    'entropy': entropy,
    'is_anomaly': is_anomaly
})

# Sauvegarder le DataFrame dans un fichier CSV
df.to_csv('data/detections.csv', index=False)

print("Fichier detections.csv généré avec succès !")
