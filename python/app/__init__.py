from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate 
import secrets 


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rodomastwr@localhost:5433/projeto'
app.config['SECRET_KEY'] = secrets.token_hex(16)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
migrate = Migrate(app, db) 








from app import routes 
from app.models import Usuario, Foto 