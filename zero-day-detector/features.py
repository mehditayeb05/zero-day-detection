from scapy.all import IP, TCP, Raw
import numpy as np

def calculate_entropy(payload):
    if not payload:
        return 0
    freq = np.array([float(payload.count(c)) for c in set(payload)])
    prob = freq / len(payload)
    return -np.sum(prob * np.log2(prob))

def extract_features(pkt):
    return {
        "src_ip": pkt[IP].src,
        "dst_ip": pkt[IP].dst,
        "proto": pkt[IP].proto,
        "length": len(pkt),
        "ttl": pkt[IP].ttl,
        "tcp_flags": pkt[TCP].flags if pkt.haslayer(TCP) else 0,
        "entropy": calculate_entropy(pkt[Raw].load) if pkt.haslayer(Raw) else 0,
        "is_anomaly": 0
    }