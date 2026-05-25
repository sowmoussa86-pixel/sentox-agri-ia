import streamlit as st
from cultures import pesticides_db

st.set_page_config(
    page_title="SENTOX AGRI IA",
    layout="wide"
)

# ========= STYLE =========

st.markdown("""
<style>

.stApp{
    background-color:#07111f;
    color:white;
}

h1,h2,h3{
    color:white;
}

.big-title{
    text-align:center;
    color:#7CFC00;
    font-size:45px;
    font-weight:bold;
}

.card{
    background:#10243d;
    padding:20px;
    border-radius:20px;
    box-shadow:0px 0px 10px rgba(0,0,0,0.5);
}

</style>
""", unsafe_allow_html=True)

# ========= IMAGE =========

st.image(
    "images/sentox_agri_design.png",
    use_container_width=True
)

# ========= TITRE =========

st.markdown("""
<div class='big-title'>
SENTOX AGRI - VERSION IA
</div>
""", unsafe_allow_html=True)

st.write("")

# ========= MENU =========

menu = st.sidebar.radio(
    "MENU SENTOX",
    [
        "🏠 Accueil",
        "☣️ Analyse toxicologique",
        "🧪 Calcul doses pesticides",
        "🌿 Reconnaissance plantes IA",
        "🌍 Écotoxicologie",
        "📄 Export PDF",
        "🛰️ Cartes agricoles",
        "🌦️ Météo agricole",
        "⏳ Temps de récolte",
        "📊 Recommandations IA"
    ]
)

# =========================================================
# ACCUEIL
# =========================================================

if menu == "🏠 Accueil":

    culture = st.selectbox(
        "🌾 Choisir culture",
        list(pesticides_db.keys())
    )

    surface = st.number_input(
        "📏 Surface (ha)",
        min_value=0.1,
        value=1.0
    )

    if st.button("🔬 ANALYSER"):

        data = pesticides_db[culture]

        st.subheader(f"Culture : {culture}")

        for p in data:

            st.markdown(f"""
            <div class='card'>

            <h3>{p['nom']}</h3>

            <p>Dose : {p['dose']} L/ha</p>

            <p>Risque : {p['risque']}/3</p>

            <p>Efficacité : {p['efficacite']}/10</p>

            <p>Autorisé : {p['autorise']}</p>

            </div>
            """, unsafe_allow_html=True)

        eau = surface * 12000

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("💧 Eau", f"{eau} L")

        with col2:
            st.metric("☣️ Produits", len(data))

        with col3:
            st.metric("✅ Sécurité", "Conforme")

# =========================================================
# ANALYSE TOXICOLOGIQUE
# =========================================================

elif menu == "☣️ Analyse toxicologique":

    st.header("☣️ Analyse toxicologique")

    st.write("""
    Analyse :
    - DL50
    - Cancérogénicité
    - Neurotoxicité
    - Risques environnementaux
    - Sécurité alimentaire
    """)

# =========================================================
# CALCUL DOSES
# =========================================================

elif menu == "🧪 Calcul doses pesticides":

    st.header("🧪 Calcul intelligent des doses")

    dose = st.number_input("Dose recommandée (L/ha)", value=1.0)

    surface = st.number_input("Surface (ha)", value=1.0)

    total = dose * surface

    st.success(f"Quantité totale nécessaire : {total} L")

# =========================================================
# RECONNAISSANCE IA
# =========================================================

elif menu == "🌿 Reconnaissance plantes IA":

    st.header("🌿 Reconnaissance IA des plantes")

    image = st.file_uploader(
        "Télécharger image plante",
        type=["jpg","png","jpeg"]
    )

    if image:
        st.image(image)

        st.success("Analyse IA bientôt disponible")

# =========================================================
# ECOTOXICOLOGIE
# =========================================================

elif menu == "🌍 Écotoxicologie":

    st.header("🌍 Analyse écotoxicologique")

    st.write("""
    - Toxicité poissons
    - Toxicité abeilles
    - Pollution eau
    - Pollution sols
    - Risques biodiversité
    """)

# =========================================================
# EXPORT PDF
# =========================================================

elif menu == "📄 Export PDF":

    st.header("📄 Export rapport PDF")

    st.info("Fonction export PDF bientôt disponible")

# =========================================================
# CARTES
# =========================================================

elif menu == "🛰️ Cartes agricoles":

    st.header("🛰️ Cartographie agricole")

    st.info("Cartes satellitaires bientôt disponibles")

# =========================================================
# METEO
# =========================================================

elif menu == "🌦️ Météo agricole":

    st.header("🌦️ Météo agricole IA")

    st.write("""
    - Température
    - Humidité
    - Risques pluie
    - Vent
    - Prévision traitements
    """)

# =========================================================
# RECOLTE
# =========================================================

elif menu == "⏳ Temps de récolte":

    st.header("⏳ Temps avant récolte")

    jours = st.slider(
        "Nombre jours",
        1,
        120,
        30
    )

    st.success(f"Récolte estimée dans {jours} jours")

# =========================================================
# IA
# =========================================================

elif menu == "📊 Recommandations IA":

    st.header("📊 IA AGRICOLE")

    st.write("""
    - Recommandation pesticides
    - Optimisation traitements
    - Sécurité alimentaire
    - Réduction toxicité
    - Agriculture durable
    """)