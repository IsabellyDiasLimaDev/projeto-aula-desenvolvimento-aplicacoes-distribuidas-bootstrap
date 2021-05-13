from app import app, db
from flask import Flask, url_for, redirect, render_template, request
from app.model.tables import Cliente


@app.route("/")
def index():
    # selecionar todos - select * from
    clientes = Cliente.query.all()
    return render_template("index.html", clientes=clientes)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # crio um objeto cliente com os dados do formulario
        cliente = Cliente(request.form['nome'], request.form['comentario'])
        # adiciono o cliente (insert into)
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("add.html")


@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    # select from
    cliente = Cliente.query.get(id)
    if request.method == 'POST':
        cliente.name = request.form['nome']
        cliente.comment = request.form['comentario']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("edit.html", cliente=cliente)


@app.route("/delete/<int:id>")
def delete(id):
    cliente = Cliente.query.get(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('index'))
