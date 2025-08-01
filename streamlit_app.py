import streamlit as st
import paho.mqtt.publish as publish
import time
import os

st.set_page_config(layout="wide")
st.title("Controllo Mobilenet SSD")

# Bottone accensione/spegnimento
if st.button("📷 Avvia Webcam"):
    publish.single("mobilenet/control", "start", hostname="localhost")  # o IP broker
    st.success("Webcam avviata!")

if st.button("🛑 Ferma Webcam"):
    publish.single("mobilenet/control", "stop", hostname="localhost")
    st.warning("Webcam fermata.")

st.markdown("---")
st.subheader("📺 Video in diretta")

# Mostra frame aggiornato
image_location = "static/frame.jpg"

frame_placeholder = st.empty()
while True:
    if os.path.exists(image_location):
        frame_placeholder.image(image_location, channels="BGR", use_column_width=True)
    time.sleep(0.1)
