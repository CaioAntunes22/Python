from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route('/decorator') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def ola_mundo():
    return 'Welcome to Flask’s documentation. Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.' # Isso é o que será retornado quando a rota '/' for acessada

if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento