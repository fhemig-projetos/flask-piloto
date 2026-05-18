from flask import app, render_template, request
from flask_login import login_required


def init_routes(app):
    @login_required
    @app.route('/')
    def home():
        return 'Tela inicial!'

    @login_required
    @app.route('/mostrar-dados')
    def mostrar_dados():
        return 'Nesta tela serão mostrados os dados do banco de dados'
    
    @app.route("/cadastrar-usuario", methods=["GET", "POST"])
    def cadastrar_usuario():
        if request.method == "POST":
            pass
        return render_template("cadastrar-usuario.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            pass
        return render_template("login.html")

    

