from flask import Blueprint, render_template
from flask_login import login_required

# Criamos o Blueprint 'main'
main_bp = Blueprint('main', __name__)

@main_bp.route('/home')
@login_required
def home():
    return render_template("home.html")

@main_bp.route('/mostrar-dados')
@login_required
def mostrar_dados():
    return 'Nesta tela serão mostrados os dados do banco de dados'