import streamlit as st
from cultures import pesticides_db

st.set_page_config(
    page_title="SENTOX AGRI IA",
    layout="centered"
)

# ===== STYLE CSS =====
st.markdown("""
<style>

body {
    background-color: #07111f;
}

.stApp {
    background: linear-gradient(to bottom, #07111f, #0b1d33);
    color: white;
}

h1, h2, h3 {
    color: white;
}

.big-title {
    font-size: 45px;
    font-weight: bold;
    color: #7CFC00;
    text-align: center;
}

.subtitle {
    text-align: center;
    color: white;
    font-size: 20px;
}

.card {
    background-color: #10243d;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.4);
}

.green {
    color: #7CFC00;
}

</style>
""", unsafe_allow_html=True)

# ===== IMAGE =====
st.image("images/sentox_agri_design.png", use_container_width=True)

# ===== TITRE =====
st.markdown(
    "<div class='big-title'>SENTOX AGRI - VERSION IA</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>L'intelligence au service de vos cultures</div>",
    unsafe_allow_html=True
)

st.write("")

# ===== CHOIX CULTURE =====
culture = st.selectbox(
    "🌾 Choisir une culture",
    list(pesticides_db.keys())
)

surface = st.number_input(
    "📏 Entrer surface (ha)",
    min_value=0.1,
    value=1.0
)

# ===== ANALYSE =====
if st.button("🔬 ANALYSER"):

    data = pesticides_db[culture]

    st.subheader(f"Culture sélectionnée : {culture}")

    for p in data:

        st.markdown("---")

        st.markdown(
            f"""
            <div class="card">

            <h3 class="green">{p['nom']}</h3>

            <p><b>Dose :</b> {p['dose']} L/ha</p>

            <p><b>Risque :</b> {p['risque']}/3</p>

            <p><b>Efficacité :</b> {p['efficacite']}/10</p>

            <p><b>Autorisé :</b> {p['autorise']}</p>

            </div>
            """,
            unsafe_allow_html=True
        )

    # ===== CALCULS =====

    eau = surface * 12000

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "💧 Eau nécessaire",
            f"{eau} L"
        )

    with col2:
        st.metric(
            "☣️ Pesticides",
            f"{len(data)} produit(s)"
        )

    with col3:
        st.metric(
            "✅ Sécurité",
            "Conforme"
        )