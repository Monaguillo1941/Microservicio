from flask import Flask
app = Flask(__name__)

@app.route('/getPrueba')
def getPruebaOnLine():
    return 'Mi primer Microservicio utilizando Docker - Git'