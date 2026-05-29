from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required

from app.forms import RegistroForm, LoginForm
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
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    
    form = LoginForm()

    if form.validate_on_submit():
        query = db.select(Usuario).where(Usuario.email == form.email.data)
        usuario : Usuario = db.session.scalar(query)

        if usuario and usuario.check_senha(form.senha.data):
            login_user(usuario)
            flash("Login realizado com sucesso!", "sucesso")

            proxima_pagina = request.args.get("next")

            if proxima_pagina:
                return redirect(proxima_pagina)
            else:
                return redirect(url_for("main.home"))

        else: 
            flash('E-mail ou senha incorretos. Tente novamente.', 'erro')

    return render_template("login.html", form=form)
    
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Você saiu do sistema", "sucesso")
    return redirect(url_for("auth.login"))