from flask import render_template, url_for, request, redirect, flash, jsonify
from app.models import Usuario
from app import app, db
from flask_login import login_required, current_user
from app import bcrypt  

@app.route("/")  
@login_required
def homepage(): 
    return render_template("login.html", current_user=current_user)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, senha):
            login_user(usuario)
            return redirect(url_for("homepage"))
        else:
            flash("Email ou senha incorretos")
            return redirect(url_for("login"))
    return render_template("homepage.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nome_usuario = request.form.get("nome_usuario")
        email = request.form.get("email")
        senha = request.form.get("senha")
        confirmacao_senha = request.form.get("confirmacao_senha")

        if senha != confirmacao_senha:
            flash("As senhas não coincidem")
            return redirect(url_for("cadastro"))

        senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')
        usuario = Usuario(nome_usuario=nome_usuario, email=email, senha=senha_hash)
        db.session.add(usuario)
        db.session.commit()
        flash("Cadastro realizado com sucesso! Faça login.")
        return redirect(url_for("login"))
    return render_template("cadastro.html")

@app.route("/perfil/<id_usuario>")
@login_required
def perfil(id_usuario): 
    if int(id_usuario) == int(current_user.id): 
        return render_template("perfil.html", usuario=current_user)
    else: 
        usuario  = Usuario.query.get(int(id_usuario))
        return render_template("perfil.html", usuario=usuario)


@app.route("/configuracoes", methods=["POST", "GET"])
@login_required
def configuracoes():
    if request.method == "POST":  
        current_user.nome_de_usuario = request.form.get("nome_de_usuario")
        current_user.email = request.form.get("email")
        current_user.bio = request.form.get("bio")
        current_user.privacidade = request.form.get("privacidade")
        current_user.idioma = request.form.get("idioma") 
        current_user.genero = request.form.get("genero")


        db.session.commit()
        flash("Alterações atualizadas com sucesso!")
        return redirect(url_for("configuracoes"))
    
    return render_template("configuracoes.html", current_user=current_user)

@app.route("/index")
def index():
    return render_template("index.html")

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user
from app.models import Usuario



