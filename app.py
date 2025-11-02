from flask import Flask, jsonify, request, render_template
import pokebase as pb


app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Omarchy Pokedex!"


@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['username']
    return f"Hello, {name}! Welcome to Omarchy Pokedex."


@app.route('/pd', methods=['POST'])
def pd():



@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', person=name)

#Pokedex Route for url handling
@app.route('/Pokedex')
def Pokedex():
    return render_template('index.html')


# PLACEHOLDER
@app.route(/'pokemon/<name>')




#Get the Pokemon
def get_pokemon(pokemon_name):

    pokemon = pb.pokemon(pokemon_name)
    
    return 



if __name__ == '__main__':
    app.run(debug=True)
