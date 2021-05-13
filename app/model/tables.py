from app import app, db

# crio a tabela cliente
class Cliente(db.Model):
    __tablename__ = "tbcliente"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
    comment = db.Column(db.String(120))
    
    def __init__(self, name, comment):
        self.name = name
        self.comment = comment