from flask import Blueprint, jsonify
import pandas as pd

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def index():
    return jsonify({"message": "Bienvenido a MotoGP Season 24 API"})

@main_routes.route('/progression')
def progression():
    # Aquí cargaremos los datos de season_data.csv y devolveremos la progresión
    df = pd.read_csv('data/season_data.csv')
    return df.to_json(orient='records')