# 🛡️ Zero-Day Network Threat Detection System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scapy](https://img.shields.io/badge/Scapy-2.5.0-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25.0-red)

Un système de détection d'anomalies réseau utilisant l'Isolation Forest pour identifier des comportements malveillants inconnus (zero-day).

## Structure 
zero-day-detection/
├── data/               # Données générées
│   ├── detections.csv
│   └── normal_traffic.csv
├── models/             # Modèles entraînés
│   └── zero_day_model.pkl
├── src/                # Code source
│   ├── app.py
│   ├── capture.py
│   ├── detect.py
│   ├── features.py
│   ├── generate_detections.py
│   ├── generate_normal_data.py
│   └── train.py
└──  requirements.txt    # Dépendances

## 📦 Fonctionnalités clés
- **Capture temps réel** : Analyse des paquets réseau via Scapy
- **Détection avancée** : 
  - Extraction de caractéristiques (entropie, TTL, flags TCP)
  - Modèle Isolation Forest entraîné sur du trafic normal
- **Visualisation** : Dashboard interactif avec Streamlit
- **Génération de données** : Outils pour créer des datasets de test

## 🚀 Architecture Technique
```plaintext
data_flow = [
    "capture.py → Packet Sniffer",
    "features.py → Feature Extraction",
    "detect.py → Anomaly Prediction",
    "app.py → Visualization Dashboard"
]
