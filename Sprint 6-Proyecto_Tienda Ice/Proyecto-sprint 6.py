#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# %%
df = pd.read_csv("games.csv")
df.head()
df.info()


# %%
# Convertir nombres de columnas a minúsculas
df.columns = df.columns.str.lower()
# Manejar 'tbd' en user_score y convertir a float
df['user_score'] = df['user_score'].replace('tbd', np.nan)
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')

# Convertir year_of_release a int (ignorando NaNs por ahora)
df['year_of_release'] = df['year_of_release'].astype('Int64')  # Usa Int64 para manejar NaNs
# Agregar columna de ventas totales
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales'] + df['other_sales']
# Manejar missing values básicos: Por ejemplo, dropear filas sin nombre o género (pocos), y para scores/rating, dejar NaNs por ahora (los manejaremos en análisis)
df = df.dropna(subset=['name', 'genre'])
# Verificar cambios
df.info()
df.head()



# %%
# Análisis exploratorio básico
# Ventas totales por año
sales_by_year = df.groupby('year_of_release')['total_sales'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(sales_by_year['year_of_release'], sales_by_year['total_sales'])
plt.title('Ventas Totales por Año de Lanzamiento')
plt.xlabel('Año')
plt.ylabel('Ventas Totales (millones)')
plt.show()

# Top 10 juegos por ventas
top_games = df.sort_values('total_sales', ascending=False).head(10)
print(top_games[['name', 'platform', 'year_of_release', 'total_sales']])



# %%
# Filtrar para lapso de 7 años (5)
start_year = 2010
end_year = 2016
df_filtered = df[(df['year_of_release'] >= start_year) & (df['year_of_release'] <= end_year)]

# Top 5 consolas por ventas totales en el período
top_platforms = df_filtered.groupby('platform')['total_sales'].sum().nlargest(5).index.tolist()

# Filtrar solo top
df_top = df_filtered[df_filtered['platform'].isin(top_platforms)]

# Pivot para grouped bar chart
sales_pivot = df_top.pivot_table(index='year_of_release', columns='platform', values='total_sales', aggfunc='sum', fill_value=0)

# Graficar
fig, ax = plt.subplots(figsize=(12, 6))
sales_pivot.plot(kind='bar', ax=ax, width=0.8)

# Labels numéricos
for container in ax.containers:
    for bar in container:
        height = bar.get_height()
        if height > 0:
            ax.text(bar.get_x() + bar.get_width()/2, height, f'{height:.2f}', ha='center', va='bottom', fontsize=10)

plt.title(f'Ventas por Año y Top Consolas ({start_year}-{end_year})')
plt.xlabel('Año de Lanzamiento')
plt.ylabel('Ventas Totales (millones)')
plt.legend(title='Plataforma')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

 #Top juegos por año para inferir impactos
for year in range(start_year, end_year + 1):
    top_games_year = df[df['year_of_release'] == year].sort_values('total_sales', ascending=False).head(10)
    print(f'Top juegos en {year}:\n', top_games_year[['name', 'platform', 'total_sales']])


# %%

# Definir lapsos de 10 años 
lapsos = [
    (1980, 1989),
    (1990, 1999),
    (2000, 2009),
    (2010, 2016)
]

# Diccionarios para almacenar resultados
conteo_juegos = {}
plataformas_destacadas = {}

for start, end in lapsos:
    # Filtrar df para el lapso
    df_lapso = df[(df['year_of_release'] >= start) & (df['year_of_release'] <= end)]
    
    # Conteo de juegos lanzados (filas únicas)
    num_juegos = len(df_lapso)
    conteo_juegos[f'{start}-{end}'] = num_juegos
    
    # Top 5 plataformas por ventas totales
    top_plataformas = df_lapso.groupby('platform')['total_sales'].sum().nlargest(5).reset_index()
    plataformas_destacadas[f'{start}-{end}'] = top_plataformas


print("Conteo de Juegos por Lapso:")
for lapso, count in conteo_juegos.items():
    print(f"{lapso}: {count} juegos")

print("\nPlataformas Destacadas por Lapso (Top 5 por ventas totales en millones):")
for lapso, df_top in plataformas_destacadas.items():
    print(f"\nLapso {lapso}:")
    print(df_top)


# %%
# Boxplot de ventas globales por plataforma (2011–2016)
plt.figure(figsize=(12,6))
df_relevant = df[(df['year_of_release'] >= 2011) & (df['year_of_release'] <= 2016)]

top_platforms = (
    df_relevant.groupby('platform')['total_sales']
    .sum()
    .nlargest(5)
    .index
)

df_box = df_relevant[df_relevant['platform'].isin(top_platforms)]

df_box.boxplot(column='total_sales', by='platform')
plt.title('Distribución de ventas globales por plataforma (2011–2016)')
plt.suptitle('')
plt.xlabel('Plataforma')
plt.ylabel('Ventas globales (millones)')
plt.show()


# %%
ps4 = df_relevant[df_relevant['platform'] == 'PS4']

plt.scatter(ps4['critic_score'], ps4['total_sales'], alpha=0.5)
plt.xlabel('Critic Score')
plt.ylabel('Ventas Globales')
plt.title('Relación entre reseñas de críticos y ventas (PS4)')
plt.show()

corr = ps4[['critic_score', 'total_sales']].corr().iloc[0,1]
print(f"Correlación Critic Score vs Ventas: {corr:.2f}")

# %%
genre_sales = (
    df_relevant.groupby('genre')['total_sales']
    .sum()
    .sort_values(ascending=False)
)

genre_sales.plot(kind='bar', figsize=(10,6))
plt.title('Ventas totales por género (2011–2016)')
plt.xlabel('Género')
plt.ylabel('Ventas globales (millones)')
plt.show()


# %%
# Filtrar para período relevante: 2012-2016
df_filtered = df[(df['year_of_release'] >= 2012) & (df['year_of_release'] <= 2016)]

# Función para obtener top 5 plataformas y cuotas por región
def get_top_platforms_by_region(region_sales_col):
    # Ventas totales por plataforma en la región
    sales_by_platform = df_filtered.groupby('platform')[region_sales_col].sum().reset_index()
    sales_by_platform = sales_by_platform.sort_values(region_sales_col, ascending=False).head(5)
    
    # Ventas totales en la región
    total_region_sales = df_filtered[region_sales_col].sum()
    
    # Cuota de mercado (%)
    sales_by_platform['market_share'] = (sales_by_platform[region_sales_col] / total_region_sales) * 100
    
    return sales_by_platform

# Obtener para NA (North America)
na_top = get_top_platforms_by_region('na_sales')
print('Top 5 NA:')
print(na_top)

# Obtener para EU (Europe)
eu_top = get_top_platforms_by_region('eu_sales')
print('Top 5 EU:')
print(eu_top)

# Obtener para JP (Japan)
jp_top = get_top_platforms_by_region('jp_sales')
print('Top 5 JP:')
print(jp_top)


# %%
# Filtrar para período relevante: 2012-2016 
df_filtered = df[(df['year_of_release'] >= 2012) & (df['year_of_release'] <= 2016)]

# Función para obtener top 5 géneros y cuotas por región
def get_top_genres_by_region(region_sales_col):
    # Ventas totales por género en la región
    sales_by_genre = df_filtered.groupby('genre')[region_sales_col].sum().reset_index()
    sales_by_genre = sales_by_genre.sort_values(region_sales_col, ascending=False).head(5)
    
    # Ventas totales en la región
    total_region_sales = df_filtered[region_sales_col].sum()
    
    # Cuota de mercado (%)
    sales_by_genre['market_share'] = (sales_by_genre[region_sales_col] / total_region_sales) * 100
    
    return sales_by_genre

# Obtener para NA
na_genres = get_top_genres_by_region('na_sales')
print('Top 5 Géneros NA:')
print(na_genres)

# Obtener para EU
eu_genres = get_top_genres_by_region('eu_sales')
print('Top 5 Géneros EU:')
print(eu_genres)

# Obtener para JP
jp_genres = get_top_genres_by_region('jp_sales')
print('Top 5 Géneros JP:')
print(jp_genres)


# %%
# Análisis de ventas promedio por rating ESRB por región
# Llenar NaN en rating con 'Unknown' para incluir todos
df_filtered.loc[:, 'rating'] = df_filtered['rating'].fillna('Unknown')

# Ventas promedio por rating y región
sales_by_rating = df_filtered.groupby('rating')[['na_sales', 'eu_sales', 'jp_sales']].mean().reset_index()
sales_by_rating = sales_by_rating.sort_values('na_sales', ascending=False)  # Ordenar por NA como ejemplo

print('Ventas Promedio por Rating ESRB:')
print(sales_by_rating)


# %%
df_filtered = df[(df['year_of_release'] >= 2012) & (df['year_of_release'] <= 2016)]

# Preparar datos: Eliminar NaNs en user_score para las pruebas
df_filtered = df_filtered.dropna(subset=['user_score'])

# Hipótesis 1: Calificaciones promedio de usuarios para Xbox One y PC son las mismas
# Filtrar scores por plataforma
xone_scores = df_filtered[df_filtered['platform'] == 'XOne']['user_score']
pc_scores = df_filtered[df_filtered['platform'] == 'PC']['user_score']

# Calcular medias
mean_xone = xone_scores.mean()
mean_pc = pc_scores.mean()

# Prueba t de Welch (no asume varianzas iguales)
t_stat1, p_value1 = stats.ttest_ind(xone_scores, pc_scores, equal_var=False)

print('Hipótesis 1: Xbox One vs PC')
print(f'Media Xbox One: {mean_xone:.2f}')
print(f'Media PC: {mean_pc:.2f}')
print(f'Estadístico t: {t_stat1:.2f}')
print(f'P-value: {p_value1:.4f}')

# Hipótesis 2: Calificaciones promedio de usuarios para Acción y Deportes son diferentes
# Filtrar scores por género
action_scores = df_filtered[df_filtered['genre'] == 'Action']['user_score']
sports_scores = df_filtered[df_filtered['genre'] == 'Sports']['user_score']

# Calcular medias
mean_action = action_scores.mean()
mean_sports = sports_scores.mean()

# Prueba t de Welch
t_stat2, p_value2 = stats.ttest_ind(action_scores, sports_scores, equal_var=False)

print('\nHipótesis 2: Acción vs Deportes')
print(f'Media Acción: {mean_action:.2f}')
print(f'Media Deportes: {mean_sports:.2f}')
print(f'Estadístico t: {t_stat2:.2f}')
print(f'P-value: {p_value2:.4f}')
# %%
