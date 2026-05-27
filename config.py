import os
from dotenv import load_dotenv

# Carrega as senhas ocultas do arquivo .env
load_dotenv()

# Pega o caminho absoluto da pasta raiz do seu projeto
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Em vez de escrever a senha aqui, ele puxa do .env!
    # Se o .env não existir (ex: no computador de outro dev), ele usa 'dev-key' como fallback de segurança
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-provisoria'    
    
    # O caminho do banco de dados (salvando dentro da pasta app)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app', 'app.db')
    
    # Desativa os avisos de modificação do SQLAlchemy para economizar memória
    SQLALCHEMY_TRACK_MODIFICATIONS = False