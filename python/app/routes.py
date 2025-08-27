from flask import render_template, url_for, request, redirect, flash
from app.models import Usuario
from app import app, db
from flask_login import login_required, current_user


@app.route("/")  
def homepage(): 
    return render_template("homepage.html", current_user=current_user)

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



