from flask import Flask, render_template, request, url_for,redirect
from flask_sqlalchemy import SQLAlchemy

# instncia do Flask
app = Flask(__name__)
# caminho do DB
app.config.from_object('config')
# instancia do sqlalchemy
db = SQLAlchemy(app)
          
from app.controller import default


