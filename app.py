from flask import Flask, jsonify, request
import pokebase as pb


app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Omarchy Pokedex!"


#Pokedex Route for url handling
@app.route('/Pokedex')
def Pokedex():
    response = "Welcome Trainer!<br>"
    response += "This is a placeholder route.<br>"
    response += "More features coming soon!"
    return response

# Get the Pokemon
def get_pokemon(pokemon_name):

    pokemon = pb.pokemon(pokemon_name)
    
    return 



if __name__ == '__main__':
    app.run(debug=True)
