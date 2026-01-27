# Zero-Day Network Threat Detection System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scapy](https://img.shields.io/badge/Scapy-2.5.0-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25.0-red)

A network anomaly detection system using Isolation Forest to identify unknown (zero-day) malicious behaviors.

## File Structure
```text
zero-day-detection/
├── data/                   
│   ├── detections.csv
│   └── normal_traffic.csv
├── models/                
│   └── zero_day_model.pkl
│   app.py
│   capture.py
│   detect.py
│   features.py
│   generate_detections.py
│   generate_normal_data.py
│   train.py
└── requirements.txt      
```
## Key Features
- Real-time capture: Network packet analysis using Scapy
- Advanced detection:
- - Feature extraction (entropy, TTL, TCP flags)
- - Isolation Forest model trained on normal traffic
- Visualization: Interactive dashboard using Streamlit
- - Data generation: Tools to create test datasets

## Technical Architecture
```text
data_flow = [
    "capture.py → Packet Sniffer",
    "features.py → Feature Extraction",
    "detect.py → Anomaly Prediction",
    "app.py → Visualization Dashboard"
]
```
