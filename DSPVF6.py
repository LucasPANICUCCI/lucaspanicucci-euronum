import streamlit as st
from datetime import datetime
from io import BytesIO

# Configuration de la page
st.set_page_config(page_title="🎫 Billet DSP Avocats", layout="centered")

# Initialisation des variables de session
if "montant" not in st.session_state:
    st.session_state.montant = 0
if "nom" not in st.session_state:
    st.session_state.nom = ""
if "billet_genere" not in st.session_state:
    st.session_state.billet_genere = False
if "intro_vue" not in st.session_state:
    st.session_state.intro_vue = False

# Fenêtre d'introduction modale (simulée)
if not st.session_state.intro_vue:
    with st.container():
        st.markdown("""
        <div style='position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                     background-color: rgba(255, 255, 255, 0.95); z-index: 999;
                     padding: 50px; display: flex; justify-content: center; align-items: center;
                     font-family: Georgia, serif;'>
            <div style='max-width: 800px; padding: 30px; background: #ffffff; border: 1px solid #ccc;
                        border-radius: 12px; box-shadow: 0 0 20px rgba(0,0,0,0.2);'>
                <h2 style='text-align: center;'>💶 Générateur de billet juridique numérique DSP</h2>
                <p style='font-size:16px; line-height:1.6; text-align:justify; color:#333;'>
                    Inspirée du principe de l’euro numérique — une monnaie publique, numérique, simple et accessible — 
                    cette plateforme vous permet de créer progressivement un <strong>crédit symbolique d’accès au droit</strong>.
                </p>
                <p style='font-size:16px; line-height:1.6; text-align:justify; color:#333;'>
                    Chaque clic représente un <strong>acte de reconnaissance de la valeur du droit</strong>. 
                    Une fois le seuil symbolique de <strong>150 €</strong> atteint, vous pourrez générer un billet juridique numérique DSP, 
                    <strong>valable pour une consultation confidentielle avec un avocat du cabinet</strong>.
                </p>
                <p style='text-align:right; font-size:14px; color:#888;'>— Service Avocat – DSP Avocats</p>
                <form action="" method="post">
                    <button style='margin-top: 20px; width: 100%; background-color: #0077cc; color: white;
                                   padding: 12px; font-size: 16px; border: none; border-radius: 8px; cursor: pointer;'>
                        Compris, je commence →
                    </button>
                </form>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.session_state.intro_vue = True
    st.stop()

# Champ pour le nom
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

# Génération du billet
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
                        font-family: \"Georgia\", serif; text-align: center;'>
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

            # Capture d'écran ou téléchargement
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
