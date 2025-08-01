import streamlit as st
import paho.mqtt.publish as publish

# === CONFIG da secrets.toml ===
BROKER = st.secrets["MQTT_BROKER"]
PORT = int(st.secrets["MQTT_PORT"])
USERNAME = st.secrets["MQTT_USERNAME"]
PASSWORD = st.secrets["MQTT_PASSWORD"]
TOPIC = st.secrets["MQTT_TOPIC"]

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
