from app.lib import db
from flask import Flask, Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.authentification.routes import get_user_role



# Blueprint pour les utilisateurs
group_pb = Blueprint("group", __name__)


@group_pb.route("/listgroup", methods=["get"])
def list_group():
    conn = db.cur.execute('SELECT * FROM groupe')
    list = db.cur.fetchall()
    return jsonify(list)



@group_pb.route("/newgroup", methods=["POST"])
@jwt_required()
def add_group():
    data = request.json
    role = get_user_role()
    nom_groupe = data.get('nom_groupe')
    
 
    if role == 'admin':
        
        # Vérifier que tous les champs sont remplis
        if not nom_groupe:
            return jsonify({"error": "Donner le nom du groupe"}), 400

        try:
            # Exemple d'ajout d'un groupe à la base de données PostgreSQL
            db.cur.execute(
                "INSERT INTO groupe (nom_groupe) VALUES (%s)",(nom_groupe,)
            )
            db.conn.commit()

            return {
                "message": "groupe crée avec succès"}
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({'error': 'Vous n\'avez pas les droits pour créer un prompt'}), 403

