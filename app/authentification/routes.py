
from flask import jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt
from werkzeug.security import check_password_hash
from flask import Flask, Blueprint, request, jsonify
from app.lib import db

auth_pb = Blueprint("auth", __name__)


# Supposez que vous avez déjà configuré un blueprint pour les utilisateurs
@auth_pb.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get('email')
    motdpass = data.get('motdpass')

    # Vérifier les informations d'identification de l'utilisateur
    db.cur.execute("SELECT * FROM utilisateur WHERE email = %s", (email,))
    user = db.cur.fetchone()
    if user:
        hashed_password =  user['motdpass']
        if check_password_hash(hashed_password, motdpass):
            
            # Authentification réussie, créer un token JWT
            # Inclure le rôle dans le token JWT
            additional_claims = {"role": user['role']}
            access_token = create_access_token(identity=user['email'], additional_claims=additional_claims)
            return jsonify(access_token=access_token), 200
        else :
            return jsonify({"msg": "Mot de passe incorrect"}), 401
    else:
        return jsonify({"error": "Email ou mot de passe incorrect"}), 400



def get_user_role():
    jwt_data = get_jwt()
    return jwt_data.get('role', None)






































# Blueprint pour les authentification
# auth_pb = Blueprint("authentification", __name__)

# @auth_pb.route("/login", methods = ["POST"] )
# def connexion():
#     data = request.get_json()
    
#     # Récupération des données
#     email = data.get["email"]
#     motdpass = data.get["motdpass"]
#     if not email or not motdpass:
#         return jsonify('remplir les champs vide')
#     return None
    
# # #     user=db.get_user(email)
# # #     if user :
        
        
# from flask import Blueprint, jsonify, request
# from flask_jwt_extended import (
#     create_access_token,
#     create_refresh_token,
#     jwt_required,
#     get_jwt,
#     current_user,
#     get_jwt_identity,
# )
# from .gestion import User, TokenBlocklist

# auth_bp = Blueprint("auth", __name__)


# @auth_bp.post("/register")
# def register_user():
#     data = request.get_json()

#     user = User.get_user_by_username(username=data.get("username"))

#     if user is not None:
#         return jsonify({"error": "User already exists"}), 409

#     new_user = User(username=data.get("username"), email=data.get("email"))

#     new_user.set_password(password=data.get("password"))

#     new_user.save()

#     return jsonify({"message": "User created"}), 201


# @auth_bp.post("/login")
# def login_user():
#     data = request.get_json()

#     user = User.get_user_by_username(username=data.get("username"))

#     if user and (user.check_password(password=data.get("password"))):
#         access_token = create_access_token(identity=user.username)
#         refresh_token = create_refresh_token(identity=user.username)

#         return (
#             jsonify(
#                 {
#                     "message": "Logged In ",
#                     "tokens": {"access": access_token, "refresh": refresh_token},
#                 }
#             ),
#             200,
#         )

#     return jsonify({"error": "Invalid username or password"}), 400


# @auth_bp.get("/whoami")
# @jwt_required()
# def whoami():
#     return jsonify(
#         {
#             "message": "message",
#             "user_details": {
#                 "username": current_user.username,
#                 "email": current_user.email,
#             },
#         }
#     )


# @auth_bp.get("/refresh")
# @jwt_required(refresh=True)
# def refresh_access():
#     identity = get_jwt_identity()

#     new_access_token = create_access_token(identity=identity)

#     return jsonify({"access_token": new_access_token})


# @auth_bp.get('/logout')
# @jwt_required(verify_type=False) 
# def logout_user():
#     jwt = get_jwt()

#     jti = jwt['jti']
#     token_type = jwt['type']

#     token_b = TokenBlocklist(jti=jti)

#     token_b.save()

#     return jsonify({"message": f"{token_type} token revoked successfully"}) , 200       
        
    
    
        

    