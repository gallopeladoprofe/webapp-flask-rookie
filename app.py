from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    return "Este es el sitio donde inicia tu página"

if __name__ == "__main__":
    app.run()