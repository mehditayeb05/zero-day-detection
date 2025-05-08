import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Zero-Day Threat Dashboard")

data = pd.read_csv("data/detections.csv")

col1, col2 = st.columns(2)
col1.metric("Paquets analysés", len(data))
col2.metric("Alertes Zero-Day", len(data[data["is_anomaly"] == -1]))

fig, ax = plt.subplots()
ax.scatter(data["length"], data["entropy"], c=data["is_anomaly"])
ax.set_xlabel("Taille")
ax.set_ylabel("Entropie")
st.pyplot(fig)





