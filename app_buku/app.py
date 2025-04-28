from flask import Flask
from flask_cors import CORS 
from app_buku.routes import bp 

app = Flask(__name__)
CORS(app)  

app.register_blueprint(bp) 

if __name__ == '__main__':
    app.run(port=5002, debug=True)  # Port untuk layanan buku perpustakaan
