from scapy.all import sniff, IP, TCP
import time

def packet_handler(pkt):
    if pkt.haslayer(IP):
        print(f"[{time.strftime('%H:%M:%S')}] {pkt[IP].src} → {pkt[IP].dst}")

print("  Capture réseau démarrée (CTRL+C pour arrêter)...")
sniff(prn=packet_handler, store=False)