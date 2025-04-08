import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# CSV inlezen
df = pd.read_csv("exclusieve_schoenen_verkoop_met_locatie.csv")

# Kolomnamen netjes maken (voor de zekerheid)
df.columns = df.columns.str.strip()

# Datumkolom omzetten naar datetime
df['aankoopdatum'] = pd.to_datetime(df['aankoopdatum'])

# Groeperen op datum en totalen optellen
df_grouped = df.groupby('aankoopdatum')['totaal_bedrag'].sum().reset_index()

# Lijngrafiek maken
plt.figure(figsize=(10, 6))
plt.plot(df_grouped['aankoopdatum'], df_grouped['totaal_bedrag'], marker='o')
plt.title('Totale verkoop per dag')
plt.xlabel('aankoopdatum')
plt.ylabel('Totaal bedrag (€)')
plt.grid(True)
plt.tight_layout()
plt.show()

