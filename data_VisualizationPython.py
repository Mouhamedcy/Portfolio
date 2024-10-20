import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Charger les données
data = pd.read_csv('Africa_climate_change.csv')

# 2. Nettoyer les données
data['DATE'] = pd.to_datetime(data['DATE'], format='%Y%m%d')
data = data.dropna(subset=['TAVG', 'COUNTRY'])  # Supprimer les lignes sans température moyenne ou pays

# 3. Tracer les fluctuations de température moyenne en Tunisie et au Cameroun
filtered_data = data[(data['COUNTRY'].isin(['Tunisia', 'Cameroon'])) & (data['DATE'].dt.year <= 2005)]
plt.figure(figsize=(14, 7))
sns.lineplot(data=filtered_data, x='DATE', y='TAVG', hue='COUNTRY')
plt.title('Fluctuations de la température moyenne en Tunisie et au Cameroun (1980-2005)')
plt.xlabel('Année')
plt.ylabel('Température moyenne (°C)')
plt.xticks(rotation=45)
plt.legend(title='Pays')
plt.tight_layout()
plt.show()

# 4. Histogrammes pour la température au Sénégal
senegal_data = data[data['COUNTRY'] == 'Senegal']
data_1980_2000 = senegal_data[(senegal_data['DATE'].dt.year >= 1980) & (senegal_data['DATE'].dt.year <= 2000)]
data_2000_2023 = senegal_data[(senegal_data['DATE'].dt.year > 2000) & (senegal_data['DATE'].dt.year <= 2023)]

plt.figure(figsize=(14, 7))
sns.histplot(data_1980_2000['TAVG'], bins=20, color='blue', label='1980-2000', kde=True, stat='density')
sns.histplot(data_2000_2023['TAVG'], bins=20, color='orange', label='2000-2023', kde=True, stat='density')
plt.title('Distribution de la température moyenne au Sénégal')
plt.xlabel('Température moyenne (°C)')
plt.ylabel('Densité')
plt.legend()
plt.tight_layout()
plt.show()

# 5. Température moyenne par pays
mean_temp_per_country = data.groupby('COUNTRY')['TAVG'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=mean_temp_per_country, x='COUNTRY', y='TAVG', palette='viridis')
plt.title('Température moyenne par pays')
plt.xlabel('Pays')
plt.ylabel('Température moyenne (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()