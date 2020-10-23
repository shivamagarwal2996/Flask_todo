from flask_migrate import Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
#from flask_bcrypt import Bcrypt



app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
CORS(app, origins='*')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#print("running migrate")

#bcrypt = Bcrypt(app)

from flaskblog import routes