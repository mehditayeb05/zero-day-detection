import pandas as pd
import numpy as np
import random

# Générer 1000 lignes de données
def generate_data(num_rows=1000):
    data = []
    for _ in range(num_rows):
        length = random.randint(40, 1500)              # Longueur en octets
        proto = random.choice([6, 17])                 # 6=TCP, 17=UDP
        ttl = random.choice(range(40, 130))            # TTL typique
        entropy = round(random.uniform(1.5, 6.0), 2)    # Entropie "normale"
        data.append([length, proto, ttl, entropy])
    return pd.DataFrame(data, columns=["length", "proto", "ttl", "entropy"])

# Génération et sauvegarde
df = generate_data()
df.to_csv("data/normal_traffic.csv", index=False)
print("✅ Fichier normal_traffic.csv généré avec succès.")

