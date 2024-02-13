import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Leer el archivo CSV
file_path = '2019.csv'  # Asegúrate de que la ruta del archivo sea correcta
data = pd.read_csv(file_path)

# Crear una figura y un arreglo de ejes para los subplots
fig, axes = plt.subplots(1, 3, figsize=(20, 6))

# Gráfico de regresión para la relación entre el nivel de felicidad y el PIB per cápita
sns.regplot(ax=axes[0], x='GDP per capita', y='Score', data=data, line_kws={'color': 'red'})
axes[0].set_title('Happiness Score vs. GDP per Capita')

# Gráfico de regresión para la relación entre el nivel de felicidad y el apoyo social
sns.regplot(ax=axes[1], x='Social support', y='Score', data=data, line_kws={'color': 'red'})
axes[1].set_title('Happiness Score vs. Social Support')

# Gráfico de regresión para la relación entre el nivel de felicidad y la percepción de corrupción
sns.regplot(ax=axes[2], x='Perceptions of corruption', y='Score', data=data, line_kws={'color': 'red'})
axes[2].set_title('Happiness Score vs. Perceptions of Corruption')

plt.tight_layout()
plt.show()
