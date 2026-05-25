import streamlit as st
from cultures import base_cultures
from pesticides import base_pesticides

st.set_page_config(page_title="SENTOX AGRI IA", layout="wide")

st.title("🌾 SENTOX AGRI - VERSION IA")
st.write("Plateforme intelligente de toxicologie agricole")

culture = st.selectbox(
    "Choisir une culture",
    list(base_cultures.keys())
)

if culture:

    st.subheader(f"Culture sélectionnée : {culture}")

    data = base_cultures[culture]

    st.write("### Informations générales")
    st.write(f"💧 Eau : {data['eau']}")
    st.write(f"☠ Toxicité : {data['toxicite']}")
    st.write(f"⏳ Délai : {data['delai']}")

    st.write("### Pesticides recommandés")

    for pesticide in data["pesticides"]:

        nom = pesticide.lower()

        if nom in base_pesticides:

            p = base_pesticides[nom]

            st.success(f"Pesticide : {nom}")

            st.write(f"Dose : {p['dose']}")
            st.write(f"DL50 : {p['DL50']}")
            st.write(f"Cancérogène : {p['cancerogene']}")
            st.write(f"Écotoxique : {p['ecotoxique']}")
            st.write(f"Abeilles : {p['abeilles']}")
            st.write(f"Poissons : {p['poissons']}")
            st.write(f"Risques : {p['risques']}")

        else:
            st.error(f"{nom} non trouvé dans la base pesticides")