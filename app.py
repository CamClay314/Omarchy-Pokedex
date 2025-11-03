from flask import Flask, jsonify, request, render_template, redirect, url_for
import pokebase as pb
import threading


app = Flask(__name__)


#thread = threading.Thread()

@app.route('/')
def home():
    return "Welcome to Omarchy Pokedex!"


@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['username']
    return f"Hello, {name}! Welcome to Omarchy Pokedex."


@app.route('/pokemon', methods=['POST'])
def pokemon_p():
    pokemon_name = request.form['pokemon_name']
    return redirect(url_for('pokemon_name', name=pokemon_name))

@app.route('/pokemon/<name>')
def pokemon_name(name):
    return f"This is your pokemon: {name.capitalize()}!"


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




#Get the Pokemon
def get_pokemon(pokemon_name):

    pokemon = pb.pokemon(pokemon_name)
    
    return 



if __name__ == '__main__':
    app.run(debug=True)
