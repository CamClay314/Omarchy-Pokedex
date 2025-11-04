from flask import Flask, jsonify, request, render_template, redirect, url_for
import pokebase as pb
import threading
import re

app = Flask(__name__)


#thread = threading.Thread()

#def gemini_read():
#    if pokemon_name    


import re

def is_pokemon_real(name):
    cleaned_name = sanitize_pokemon_name(name)
    try:
        partner = pb.pokemon(cleaned_name)
        return partner  # Return the actual Pokémon object
    except Exception:
        # If pokebase throws an error (invalid name)
        return None

def sanitize_pokemon_name(name):
    # Clean and normalize
    cleaned = re.sub(r"[~`!@#$%^&*()_+{}\[\]|\\:;\"'<,>.?/]", "", name).lower().strip()
    return cleaned

# --- Data Formatter ---
def link_pokemon(pokemon):
    """Build a response string from a pokebase Pokémon object"""
    response = (
        f"Name: {pokemon.name}\n"
        f"Height: {pokemon.height}\n"
        f"Weight: {pokemon.weight}\n"
        f"Types: {[t.type.name for t in pokemon.types]}\n"
    )
    return response




@app.route('/')
def home():
    return "Welcome to Omarchy Pokedex!"


@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['username']
    return f"Hello, {name}! Welcome to Omarchy Pokedex."


@app.route('/pokemon', methods=['POST', 'GET'])
def pokemon_redirect():

    if request.method == 'POST':
        pokemon_name = request.form.get['pokemon_name']

    else:
        pokemon_name = request.args.get('pokemon_name')

    if not pokemon_name:
        return redirect(url_for('Pokedex')) # Redirect back if no name provided

    return redirect(url_for('pokemon_name_func', name=pokemon_name))

@app.route('/pokemon/<name>')
def pokemon_name_func(name):
    partner = is_pokemon_real(name)
    if partner:
        return render_template('pokemon.html', pokemon=partner)
    else:
        return f"<h3>‘{name}’ is not a real Pokémon. Try again.</h3>"


#@app.route('/hello/<name>')
#def hello(name):
#    return render_template('hello.html', person=name)


#--------------------------------------


#Pokedex Route for url handling
@app.route('/Pokedex')
def Pokedex():
    return render_template('index.html')


# PLACEHOLDER
#@app.route('/pokemon/<name>')


if __name__ == '__main__':
    app.run(debug=True)
