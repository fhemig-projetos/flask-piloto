from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Criamos as instâncias vazias (sem passar o 'app' para elas ainda)
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()