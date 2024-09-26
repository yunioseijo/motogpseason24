import pandas as pd

# Función para cargar el archivo CSV
def load_data():
    # Leer el archivo CSV
    df = pd.read_csv('data/season_data.csv')
    return df

# Función para obtener la progresión de puntos de un piloto específico
def get_pilot_progression(pilot_name):
    # Cargar los datos
    df = load_data()

    # Filtrar los datos del piloto en particular
    pilot_data = df[df['Piloto'] == pilot_name]

    if pilot_data.empty:
        return {"error": "Piloto no encontrado"}, 404

    # Obtener las columnas que contienen los puntos por carrera (columnas de carrera)
    race_columns = [col for col in df.columns if col.startswith("QAT") or col.startswith("POR") or col.startswith("AME")]

    # Filtrar las columnas de puntos de las carreras y devolverlas como una lista
    progression = pilot_data[race_columns].values.flatten().tolist()

    return {
        "piloto": pilot_name,
        "progression": progression
    }

# Función para obtener la progresión de todos los pilotos
def get_all_pilots_progression():
    # Cargar los datos
    df = load_data()

    # Obtener las columnas de las carreras
    race_columns = [col for col in df.columns if col.startswith("QAT") or col.startswith("POR") or col.startswith("AME")]

    # Crear una estructura para almacenar la progresión de puntos por piloto
    all_pilots_progression = []

    for index, row in df.iterrows():
        pilot_name = row['Piloto']
        progression = row[race_columns].values.flatten().tolist()
        all_pilots_progression.append({
            "piloto": pilot_name,
            "progression": progression
        })

    return all_pilots_progression
