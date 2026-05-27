from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.forms import RegistroForm
from app.models import Usuario
from app.extensions import db

# Criamos o Blueprint 'auth'
auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/cadastrar-usuario", methods=["GET", "POST"])
def cadastrar_usuario():
    form = RegistroForm()

    if form.validate_on_submit():
        query = db.select(Usuario).where(Usuario.email == form.email.data)
        usuario_existente = db.session.scalar(query)

        if usuario_existente:
            flash("Este e-mail já está cadastrado no sistema", "erro")
            return redirect(url_for("auth.cadastrar_usuario"))
        
        novo_usuario = Usuario(nome=form.nome.data, email=form.email.data, senha=form.senha.data)

        db.session.add(novo_usuario)
        db.session.commit()

        flash('Conta criada com sucesso! Faça seu login.', 'sucesso')
        return redirect(url_for('auth.login'))
    
    return render_template("cadastrar_usuario.html", form=form)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pass
    return render_template("login.html")