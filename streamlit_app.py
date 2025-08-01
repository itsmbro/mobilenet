import streamlit as st
import paho.mqtt.publish as publish
import os
from dotenv import load_dotenv

# === CONFIG ===
load_dotenv()
BROKER = os.getenv("MQTT_BROKER")
PORT = int(os.getenv("MQTT_PORT"))
USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")
TOPIC = os.getenv("MQTT_TOPIC")

st.set_page_config(layout="wide")
st.title("🎥 Controllo Rilevamento Oggetti - MobileNet + MQTT + Streamlit")

try:
    if st.button("📷 Avvia Webcam"):
        publish.single(TOPIC, "start", hostname=BROKER, port=PORT,
                       auth={'username': USERNAME, 'password': PASSWORD}, tls={})
        st.success("Comando inviato: START")

    if st.button("🛑 Ferma Webcam"):
        publish.single(TOPIC, "stop", hostname=BROKER, port=PORT,
                       auth={'username': USERNAME, 'password': PASSWORD}, tls={})
        st.warning("Comando inviato: STOP")

except Exception as e:
    st.error(f"❌ Errore di connessione MQTT:\n{e}")

st.subheader("📺 Video Live")
st.image("static/frame.jpg", channels="BGR", use_column_width=True)
