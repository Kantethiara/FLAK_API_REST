from flask import Flask, Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.lib import db

# Blueprint pour les utilisateurs
users_pb = Blueprint("users", __name__)

@users_pb.route("/list", methods=["GET"])
def list_users():
    conn = db.cur.execute('SELECT * FROM utilisateur')
    list = db.cur.fetchall()
    return jsonify(list)


@users_pb.route("/new", methods=["POST"])
def add_user():
    data = request.json
    nom_utilisateur = data.get('nom_utilisateur')
    email = data.get('email')
    motdpass = data.get('motdpass')
    role = data.get('role')
    id_groupe = data.get("id_groupe")

    # Vérifier que tous les champs sont remplis
    if not nom_utilisateur or not email or not motdpass or not role:
        return jsonify({"error": "Remplir tous les champs"}), 400

    # Hachage du mot de passe
    hashed_password = generate_password_hash(motdpass)

    try:
        # Exemple d'ajout d'un utilisateur à la base de données PostgreSQL
        db.cur.execute(
            "INSERT INTO utilisateur (nom_utilisateur, email, motdpass,role, id_groupe) VALUES (%s, %s, %s, %s, %s)",
            (nom_utilisateur, email, hashed_password, role, id_groupe)
        )
        db.conn.commit()

        return jsonify({
            "message": "Utilisateur ajouté avec succès",
            "user": {
                "nom_utilisateur": nom_utilisateur,
                "email": email,
                "role": role,
                "id_groupe": id_groupe
                
            }
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
