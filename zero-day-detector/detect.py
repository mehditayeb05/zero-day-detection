import pickle
import pandas as pd
from features import extract_features
from scapy.all import sniff

model = pickle.load(open("models/zero_day_model.pkl", "rb"))

def detect_zero_day(pkt):
    features = extract_features(pkt)
    df = pd.DataFrame([features])
    prediction = model.predict(df[["length", "proto", "ttl", "entropy"]])

    if prediction[0] == -1:
        print(f"🚨 ALERTE ZERO-DAY: {features['src_ip']} → {features['dst_ip']}")
        print(f"   TTL={features['ttl']}, Entropie={features['entropy']:.2f}")

print("🛡️ Détection Zero-Day activée...")
sniff(prn=detect_zero_day, store=False)

