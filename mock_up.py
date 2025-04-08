import pandas as pd
import matplotlib.pyplot as plt

# CSV inlezen
df = pd.read_csv("exclusieve_schoenen_verkoop_met_locatie.csv")

# Zorg dat de datumkolom echt als datum wordt gezien
df['datum'] = pd.to_datetime(df['datum'])

# Groeperen op datum en totalen optellen
df_grouped = df.groupby('datum')['totaal_bedrag'].sum().reset_index()

# Lijngrafiek maken
plt.figure(figsize=(10, 6))
plt.plot(df_grouped['datum'], df_grouped['totaal_bedrag'], marker='o')
plt.title('Totale verkoop per dag')
plt.xlabel('Datum')
plt.ylabel('Totaal bedrag (€)')
plt.grid(True)
plt.tight_layout()
plt.show()
