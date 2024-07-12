from .user.routes import users_pb
from .prompt.routes import prompt_pb
from .group.routes import group_pb
from .authentification.routes import auth_pb
from flask_jwt_extended import JWTManager
from flask import Flask, jsonify


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thiara19671998'  # Clé secrète pour signer le token JWT
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600*24  # Le token expire après 1 heure (3600 secondes)
jwt = JWTManager(app)


app.register_blueprint(users_pb, url_prefix='/user')
app.register_blueprint(auth_pb, url_prefix='/auth')
app.register_blueprint(prompt_pb, url_prefix='/prompt')
app.register_blueprint(group_pb, url_prefix='/group')




