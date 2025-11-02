from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Omarchy Pokedex!"

@app.route('/Pokedex')
def Pokedex():
    response = "Welcome Trainer!<br>"
    response += "This is a placeholder route.<br>"
    response += "More features coming soon!"
    return response


if __name__ == '__main__':
    app.run(debug=True)
