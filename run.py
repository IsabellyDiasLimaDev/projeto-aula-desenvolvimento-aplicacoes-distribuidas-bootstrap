from app import app, db

if __name__ == "__main__":
    # cria Banco
    db.create_all()
    # executa a aplicação
    app.run(debug=True)
