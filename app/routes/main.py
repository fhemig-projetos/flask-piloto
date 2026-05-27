from flask import Blueprint, render_template

# Criamos o Blueprint 'main'
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template("base.html")

@main_bp.route('/mostrar-dados')
def mostrar_dados():
    return 'Nesta tela serão mostrados os dados do banco de dados'