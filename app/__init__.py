import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configurações da aplicação
    app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'

    # Configuração básica: Onde o arquivo do SQLite será salvo
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models import Usuario
    
    # Rotas de exemplo
    @app.route('/')
    def home():
        return 'Tela inicial!'

    @app.route('/mostrar_dados')
    def mostrar_dados():
        return 'Nesta tela serão mostrados os dados do banco de dados'


    return app