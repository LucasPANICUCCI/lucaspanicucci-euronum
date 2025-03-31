import streamlit as st
from datetime import datetime
from io import BytesIO
from email.mime.text import MIMEText
import smtplib

# Configuration de la page
st.set_page_config(page_title="🎫 Billet DSP Avocats", layout="centered")

# Initialisation des variables de session
if "montant" not in st.session_state:
    st.session_state.montant = 0
if "nom" not in st.session_state:
    st.session_state.nom = ""
if "billet_genere" not in st.session_state:
    st.session_state.billet_genere = False

# Texte introductif stylisé
st.markdown("""
<div style='background-color:#f5f5f5; padding: 25px; border-radius: 10px; border: 1px solid #ddd; font-family: Georgia, serif;'>
  <h2 style='text-align:center; color:#333;'>🎫 Billet juridique numérique</h2>
  <p style='font-size:16px; line-height:1.6; text-align:justify; color:#444;'>
    Cette interface expérimentale vous permet de générer un <strong>billet juridique numérique DSP</strong>, inspiré du principe de l’euro numérique. 
    Chaque clic que vous effectuez ici symbolise une <strong>création de valeur d’accès au droit</strong>.
    <br><br>
    Ce billet est à <strong>usage unique</strong>, valable pour un échange confidentiel d’une durée limitée avec un avocat du cabinet.
    Il vous invite à explorer une autre manière d’<strong>accéder à un service juridique</strong>, par la création progressive d’un crédit symbolique.
    <br><br>
    Le montant maximal pouvant être cumulé est de <strong>150 euros</strong>, au-delà duquel la génération du billet devient accessible.
  </p>
  <p style='text-align:right; margin-top:20px; font-size:14px; color:#888;'>
    — Service Avocat – DSP Avocats
  </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Champ nom
nom = st.text_input("Ton prénom / nom :", value=st.session_state.nom)
st.session_state.nom = nom

# Bouton +1 € jusqu'à 150 €
if st.session_state.montant < 150:
    if st.button("💶 +1 €"):
        st.session_state.montant += 1

# Affichage du montant
st.markdown(f"""
    <h2 style='text-align: center; color: green;'>
        Montant cumulé : {st.session_state.montant} €
    </h2>
""", unsafe_allow_html=True)

# Bouton de génération du billet (accessible dès 150 €)
if st.session_state.montant >= 150 and not st.session_state.billet_genere:
    if st.button("🚨 GÉNÉRER MON BILLET DSP 🚨"):
        if nom.strip() == "":
            st.warning("Merci de renseigner ton nom.")
        else:
            date_gen = datetime.now().strftime("%d %B %Y - %Hh%M")
            billet_html = f"""
            <div style='max-width: 600px; margin: 0 auto; padding: 30px;
                        border: 2px solid #333; border-radius: 15px;
                        background: #fffdf8; box-shadow: 0 0 10px rgba(0,0,0,0.1);
                        font-family: "Georgia", serif; text-align: center;'>
                <div style='border-bottom: 1px solid #aaa; margin-bottom: 20px; padding-bottom: 10px;'>
                    <h1 style='color: #222;'>🎫 BILLET DSP AVOCATS</h1>
                    <p style='font-size: 16px; color: #555;'><em>Émission numérique confidentielle</em></p>
                </div>
                <p style='font-size: 18px;'><strong>Bénéficiaire :</strong> {nom}</p>
                <p style='font-size: 18px;'><strong>Montant :</strong> {st.session_state.montant} €</p>
                <p style='font-size: 18px;'><strong>Date :</strong> {date_gen}</p>
                <div style='margin-top: 25px; font-size: 16px; color: #444;'>
                    Ce billet vous donne droit à un <strong>échange juridique confidentiel</strong> au sein du cabinet <strong>DSP Avocats</strong>, dans la limite d’un usage unique.
                </div>
                <div style='margin-top: 40px; font-size: 13px; color: #888; border-top: 1px solid #ccc; padding-top: 10px;'>
                    À présenter par mail ou en rendez-vous.<br>
                    Cabinet DSP Avocats – 8 bis rue Andrioli – 06000 NICE
                </div>
            </div>
            """

            st.markdown("### 🎉 Ton billet est prêt :")
            st.markdown(billet_html, unsafe_allow_html=True)

            # Capture d’écran ou téléchargement
            st.markdown("---")
            st.info("📸 Tu peux capturer ce billet à l'écran (`Impr. écran`, `Cmd + Shift + 4`) ou le télécharger ci-dessous :")

            html_content = billet_html.encode("utf-8")
            st.download_button(
                label="📥 Télécharger mon billet (HTML)",
                data=html_content,
                file_name=f"billet_dsp_{nom.replace(' ', '_')}.html",
                mime="text/html"
            )

            st.session_state.billet_genere = True
