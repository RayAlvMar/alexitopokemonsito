from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

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
    
    resp = request.get(f"(API){pokemon_name}")
    
    if resp.status_code == 200:
        pokemon_data = resp.json()
        return render_template('pokemon.html', pokemon=pokemon_data)
    
    
if __name__ == '__main__':
    app.run(debug=True)