import streamlit as st
import pandas as pd

# Titel voor de app
st.title('Schoenenwinkel insights')

# Widget om een Excel-bestand te uploaden
uploaded_file = st.file_uploader("Kies een Excel-bestand", type=["xlsx"])

# Controleer of er een bestand is geüpload
if uploaded_file is not None:
    try:
        # Lees het Excel-bestand in een DataFrame
        df = pd.read_excel(uploaded_file)

        # Toon de DataFrame in de app
        st.write("Inhoud van het Excel-bestand:")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Fout bij het inlezen van het bestand: {e}")
