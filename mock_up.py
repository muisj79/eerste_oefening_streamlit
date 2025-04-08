import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Titel voor de app
st.title('Dashboard met Streamlit')
'''
# Widget om een CSV-bestand te uploaden
uploaded_file = st.file_uploader("Kies een CSV-bestand", type=["csv"])

# Controleer of er een bestand is geüpload
if uploaded_file is not None:
    try:
        # Lees het CSV-bestand in een DataFrame
        df = pd.read_csv(uploaded_file)

        # Toon de eerste paar rijen van de DataFrame
        st.write("Eerste paar rijen van het CSV-bestand:")
        st.dataframe(df.head())

        # Maak tabbladen
        tab1, tab2 = st.tabs(["Staafdiagram", "Lijndiagram"])

        with tab1:
            st.header("Staafdiagram")
            # Kies de kolommen voor de staafdiagram
            x_column = st.selectbox("Kies de x-as kolom", df.columns)
            y_column = st.selectbox("Kies de y-as kolom", df.columns)

            # Teken de staafdiagram
            plt.figure(figsize=(10, 6))
            sns.barplot(x=df[x_column], y=df[y_column])
            plt.xticks(rotation=45)
            st.pyplot(plt)

        with tab2:
            st.header("Lijndiagram")
            # Kies de kolommen voor de lijndiagram
            x_column = st.selectbox("Kies de x-as kolom", df.columns, key="line_x")
            y_column = st.selectbox("Kies de y-as kolom", df.columns, key="line_y")

            # Teken de lijndiagram
            plt.figure(figsize=(10, 6))
            sns.lineplot(x=df[x_column], y=df[y_column])
            plt.xticks(rotation=45)
            st.pyplot(plt)

    except Exception as e:
        st.error(f"Fout bij het inlezen van het bestand: {e}")
'''
