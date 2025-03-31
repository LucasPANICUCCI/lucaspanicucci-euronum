import streamlit as st
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# Configuration de la page
st.set_page_config(page_title="💶 Mon Billet DSP Avocats", layout="centered")

# Initialisation des variables de session
if "montant" not in st.session_state:
    st.session_state.montant = 0
if "nom" not in st.session_state:
    st.session_state.nom = ""

# Titre de la page
st.title("💼 Cumule ton crédit juridique")
st.markdown("Clique pour cumuler des crédits DSP, puis génère ton billet.")

# Champ pour le nom
nom = st.text_input("Ton prénom / nom :", value=st.session_state.nom)
st.session_state.nom = nom

# Trois boutons pour ajouter des montants
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

# Affichage du total cumulé
st.markdown(f"""
    <h2 style='text-align: center; color: green;'>
        Total actuel : {st.session_state.montant} €
    </h2>
""", unsafe_allow_html=True)

st.markdown("---")

# GROS bouton rouge pour générer le billet
generer = st.button("🚨 GÉNÉRER MON BILLET DSP 🚨")

if generer:
    if nom.strip() == "":
        st.warning("Merci de renseigner ton nom.")
    elif st.session_state.montant == 0:
        st.warning("Tu dois cumuler un montant avant de générer ton billet.")
    else:
        # Génération du billet HTML
        date_gen = datetime.now().strftime("%d %B %Y - %Hh%M")
        billet_html = f"""
        <div style='border: 3px dashed #d00; padding: 25px; border-radius: 10px; background-color: #fffbe6; text-align: center;'>
            <h2 style='color: #d00;'>🎫 BILLET DSP AVOCATS</h2>
            <h3>Bénéficiaire : {nom}</h3>
            <p><b>Montant cumulé :</b> {st.session_state.montant} €</p>
            <p><b>Date :</b> {date_gen}</p>
            <p style='margin-top: 20px;'>Ce billet donne droit à un échange juridique confidentiel au cabinet DSP Avocats.</p>
            <p style='margin-top: 10px; font-size: 14px;'>À présenter par mail ou en rendez-vous. Usage unique.</p>
        </div>
        """

        # Affichage à l’écran du billet
        st.markdown("### 🎉 Ton billet est prêt :")
        st.markdown(billet_html, unsafe_allow_html=True)

        # Envoi automatique par email
        try:
            destinataire = "contact@dsp-avocat.fr"
            expediteur = "ton.email@gmail.com"  # 👉 À remplacer par ton adresse Gmail d’envoi
            mdp_app = "mot-de-passe-app-gmail"  # 👉 À remplacer par ton mot de passe d'application Gmail

            msg = MIMEText(billet_html, "html")
            msg['Subject'] = f"🎫 Billet DSP Avocats – {nom}"
            msg['From'] = expediteur
            msg['To'] = destinataire

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(expediteur, mdp_app)
                server.sendmail(expediteur, destinataire, msg.as_string())

            st.success("✅ Ton billet a bien été envoyé à DSP Avocats !")
        except Exception as e:
            st.error("❌ L’envoi automatique a échoué. Merci de copier le billet et de l’envoyer manuellement.")
            st.code(str(e))
