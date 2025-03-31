import streamlit as st
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

st.set_page_config(page_title="🎟️ Générateur de Billet DSP Avocats")

# Titre
st.title("🎟️ Génère ton billet DSP Avocats")
st.markdown("Un billet symbolique à activer pour un échange juridique confidentiel chez **DSP Avocats**.")

# Formulaire utilisateur
nom = st.text_input("Ton prénom / nom :")
envoyer = st.button("🎫 Générer et envoyer le billet")

if envoyer:
    if nom.strip() == "":
        st.warning("Merci de renseigner ton nom pour générer le billet.")
    else:
        date_gen = datetime.now().strftime("%d %B %Y - %Hh%M")
        billet_html = f"""
        <div style='border: 3px dashed #888; padding: 20px; border-radius: 10px; background-color: #f9f9f9; text-align: center;'>
            <h2>🎫 BILLET JURIDIQUE NUMÉRIQUE</h2>
            <h3><i>Délivré par DSP Avocats</i></h3>
            <p><b>Bénéficiaire :</b> {nom}</p>
            <p><b>Date :</b> {date_gen}</p>
            <p><b>Valeur :</b> 1 échange juridique (30 minutes)</p>
            <p><i>À activer auprès du cabinet pour un rendez-vous confidentiel</i></p>
            <p style='margin-top: 20px; font-size: 14px;'>© DSP Avocats – billet à usage unique</p>
        </div>
        """

        # Affichage à l'écran
        st.markdown("---")
        st.markdown(billet_html, unsafe_allow_html=True)
        st.markdown("---")

        # Envoi par email (simulation avec instructions)
        try:
            # Config à adapter : ici, exemple avec Gmail
            destinataire = "panicucci.avocat@gmx.fr"  # à remplacer par ton email
            expediteur = "ton.email@gmail.com"         # remplace avec ton adresse d’envoi
            mdp_app = "mot-de-passe-app-gmail"         # mot de passe d’appli Gmail (pas le mot de passe normal)
            
            msg = MIMEText(billet_html, "html")
            msg['Subject'] = f"🎫 Nouveau billet DSP Avocats de {nom}"
            msg['From'] = expediteur
            msg['To'] = destinataire

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(expediteur, mdp_app)
                server.sendmail(expediteur, destinataire, msg.as_string())

            st.success("✅ Billet envoyé à DSP Avocats ! Merci 🙏")
        except Exception as e:
            st.error("❌ L’envoi automatique a échoué. Copie le billet et envoie-le par mail.")
            st.code(str(e))
