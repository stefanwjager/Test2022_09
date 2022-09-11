from flask import Flask

from password import generate_password

app = Flask (__name__)

@app.route('/')
def index():
    pword= generate_password(12)
    return f'<h1> {pword}</h1>'
