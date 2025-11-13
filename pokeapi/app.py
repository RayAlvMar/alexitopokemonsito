from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import requests

API = "https://pokeapi.co/api/v2/pokemon/"
app = Flask(__name__)
app.secret_key = "secretishima"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_pokemon():
    pokemon_name = request.form.get('pokemon_name', '').strip().lower()
    
    if not pokemon_name:
        flash('Por favor, ingresa un nombre de Pokemon','error')
        return redirect(url_for('index'))
    
    try:
        
        resp = request.get(f"(API){pokemon_name}")
        if resp.status_code == 200:
            pokemon_data = resp.json()
            
            pokemon_info = {
                'name': pokemon_data['name'].title(),
                'id': pokemon_data['id'],
                'height': pokemon_data['height'] / 10,
                'weight': pokemon_data['weight'] / 10,
                'image': pokemon_data['sprites']['front_default'],
                'types': [t['type']['name'].title() for t in pokemon_data['types']]
                'abilities': [a['ability']['name'].title() for a in pokemon_data['abilities']]
            }
        return render_template('pokemon.html', pokemon=pokemon_data)
    else:
        flash(f'Pokémon '{pokemon}" no encontrado.", 'error')
        return redirect(url_for('index'))
    except request.exceptions.RequestException
    flash('Error al conectar con la API de Pokémon', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)