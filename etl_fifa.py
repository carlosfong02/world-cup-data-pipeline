import pandas as pd
import sqlite3

# Visualizar TODAS las columnas sin límite en terminal
pd.set_option('display.max_columns', None)

try:
    # 'latin1' para evitar errores de caracteres especiales
    df = pd.read_csv('FIFA-World-Cup-1930-2022.csv', encoding='latin1')
except FileNotFoundError:
    exit("No se encuentra el archivo CSV")

# Muestra tipos de datos (Dtype) y nulos (Non-Null)
df.info() 

# Muestra las primeras 3 filas
print(df.head(3))

# Recorre todas las columnas, quita espacios, convierte a minúsculas y reemplaza espacios por guiones bajos.
df.columns = [col.strip().lower().replace(' ', '_').replace('-', '_') for col in df.columns]

# Convierte la fecha de texto (Object) a formato Fecha real (Datetime)
df['match_date'] = pd.to_datetime(df['match_date'], format='%m/%d/%Y')

# Selección de columnas, mediante un diccionario (Filtering)
cols_utiles = [
    'match_id', 'tournament_name', 'match_date', 'stage_name', 
    'home_team_name', 'away_team_name', 
    'home_team_score', 'away_team_score', 
    'home_team_win', 'away_team_win', 'draw'
]
df_final = df[cols_utiles].copy()

# Renombrado de Columnas mediante un diccionario
nombres_espanol = {
    'match_id': 'id_partido',
    'tournament_name': 'torneo',
    'match_date': 'fecha',
    'stage_name': 'fase',
    'home_team_name': 'equipo_local',
    'away_team_name': 'equipo_visitante',
    'home_team_score': 'goles_local',
    'away_team_score': 'goles_visitante',
    'home_team_win': 'gana_local',
    'away_team_win': 'gana_visitante',
    'draw': 'empate'
}
# Cambio de nombres al DataFrame final
df_final = df_final.rename(columns=nombres_espanol)

# Elimina espacios vacíos del inicio y final
df_final['equipo_local'] = df_final['equipo_local'].str.strip()
df_final['equipo_visitante'] = df_final['equipo_visitante'].str.strip()

# Conexión a SQLite
conn = sqlite3.connect('fifa_world_cup.db')

# if_exists='replace': Borra y recrea la tabla en cada ejecución Full Load)
# index=False: Evita guardar el índice numérico como una columna extra
df_final.to_sql('fact_partidos', conn, if_exists='replace', index=False)

conn.close()
print("\n Pipeline finalizado")