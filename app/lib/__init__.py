from .postgres import Database
from flask_jwt_extended import JWTManager

db=Database()
jwt=JWTManager()
