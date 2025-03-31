import streamlit as st
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

st.set_page_config(page_title="💶 Mon Billet DSP Avocats", layout="centered")

# Initialisation
if "montant" not in st.session_state:
    st.session_state.montant = 0
if "nom" not in st.session_state:
    st.session_state.nom = ""

st.title("💼 Cumule ton crédit juridique")

# Nom
nom = st.text_input("Ton prénom / nom :", value=st.session_state.nom)
st.session_state.nom = nom

# Boutons d'ajout
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("+1 €"):
        st.session_state.montant += 1
with col2:
    if st.button("+10 €"):
        st.session_state.montant += 10
with col3:
    if st.button("+50 €"):
        st.session_state.montant += 50

# Affichage du montant
st.markdown(f"""
    <h2 style='text-align: center; color: green;'>
        Total actuel : {st.session_state.montant} €
    </h2>
""", unsafe_allow_html=True)

st.markdown("---")

# GROS bouton rouge
generer = st.button("🚨 GÉNÉRER MON BILLET DSP 🚨")

if generer:
    if nom.strip() == "":
        st.warning("Merci de renseigner ton nom.")
    elif st.session_state.montant == 0:
        st.warning("Tu dois cumuler un montant avant de générer ton billet.")
    else:
        date_gen = datetime.now().strftime("%d %B %Y - %Hh%M")
        billet_html = f"""
        <div style='border:
