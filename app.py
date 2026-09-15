import requests
import streamlit as st

# Replace IP_DE_VOTRE_VPS with your VPS public IP address
API_URL = "http://IP_DE_VOTRE_VPS:8000"

st.set_page_config(
    page_title="Bot Trader Scalper", page_icon="📈", layout="centered"
)

st.title("📈 Bot Trader Scalper (XAUUSD)")
st.caption("Panneau de contrôle à distance")

with st.form("broker_config"):
  st.subheader("Configuration du Compte Broker")
  login = st.text_input("Numéro de compte MT5 (Login)")
  password = st.text_input("Mot de passe MT5", type="password")
  server = st.text_input("Serveur du Broker (ex: Exness-Real)")
  symbol = st.text_input("Symbole", value="XAUUSD")
  lot = st.number_input("Taille du Lot", value=0.01, step=0.01, format="%.2f")

  col1, col2 = st.columns(2)
  start_btn = col1.form_submit_button("🚀 DÉMARRER LE BOT")
  stop_btn = col2.form_submit_button("🛑 ARRÊTER LE BOT")

if start_btn:
  if not login or not password or not server:
    st.error("Veuillez remplir tous les champs d'identifiants !")
  else:
    try:
      payload = {
          "login": login,
          "password": password,
          "server": server,
          "symbol": symbol,
          "lot": lot,
      }
      res = requests.post(f"{API_URL}/start", json=payload, timeout=10)
      if res.status_code == 200:
        st.success("✅ Ordre de démarrage envoyé avec succès au VPS.")
      else:
        st.error(f"❌ Erreur du serveur VPS : {res.text}")
    except Exception as e:
      st.error(f"❌ Impossible de contacter le VPS : {e}")

if stop_btn:
  try:
    res = requests.post(f"{API_URL}/stop", timeout=10)
    if res.status_code == 200:
      st.warning("🛑 Ordre d'arrêt envoyé au VPS.")
    else:
      st.error(f"❌ Erreur du serveur VPS : {res.text}")
  except Exception as e:
    st.error(f"❌ Impossible de contacter le VPS : {e}")
