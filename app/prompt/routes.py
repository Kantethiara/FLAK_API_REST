from app.lib import db
from flask import Flask, Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.authentification.routes import get_user_role



# Blueprint pour les utilisateurs
prompt_pb = Blueprint("prompt", __name__)

 #si role='user' , c'est seulment les utilisateur qui cree des prompts
@prompt_pb.route('/create', methods = ['POST'])
@jwt_required()
def add_prompt():
    role = get_user_role()
      # Récupération des données
    data = request.get_json()
    if role == 'user':   
        # Récupération des données
        titre = data.get('titre')
        contenu = data.get('contenu')
        statut = data.get('statut')
        prix = data.get('prix')
        id_utilisateur = data.get('id_utilisateur')
        # Vérification que tous les champs sont remplis
        if not all([titre, contenu, statut, prix, id_utilisateur]):
            return jsonify({'error': 'Veuillez remplir tous les champs'}), 400
        try:
            # Insertion dans la base de données
            db.cur.execute(
                "INSERT INTO prompt (titre, contenu, statut, prix, id_utilisateur) VALUES (%s, %s, %s, %s, %s)",
                (titre, contenu, statut, prix, id_utilisateur)
            )
            db.conn.commit()

            return jsonify({'message': 'Prompt créé avec succès'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Vous n\'avez pas les droits pour créer un prompt'}), 403


@prompt_pb.route('/D_edit', methods = ['POST'])
@jwt_required()
def D_edit_prompt():

         # Récupération des données
    role = get_user_role()
    data = request.get_json()
    id_prompt = data.get('id_prompt')
    
    
    
        

     

@prompt_pb.route('/edit', methods = ['POST'])
@jwt_required()
def edit_prompt():
         # Récupération des données
    role = get_user_role()
    data = request.get_json()

    if role == 'user': 
          # Récupération des données
        id_prompt = data.get('id_prompt')
        titre = data.get('titre')
        contenu = data.get('contenu')
        statut = data.get('statut')
        prix = data.get('prix')
        id_utilisateur = data.get('id_utilisateur')
        # Vérification que tous les champs1000 sont remplis
        if not all([id_prompt, titre, contenu, statut, prix, id_utilisateur]):
            return jsonify({'error': 'Veuillez remplir tous les champs'}), 400

        try:
            # Insertion dans la base de données
            db.cur.execute(
                "INSERT INTO prompt_modifications (id_prompt, titre, contenu, statut, prix, id_utilisateur) VALUES (%s, %s, %s, %s, %s, %s)",
                (id_prompt, titre, contenu, statut, prix, id_utilisateur)
            )
            db.conn.commit()

            return jsonify({'message': 'votre Prompt a été modifier avec succès'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Vous n\'avez pas les droits pour créer un prompt'}), 403


@prompt_pb.route('/del', methods = ['POST'])
@jwt_required()
def delette_prompt():
         # Récupération des données
    role = get_user_role()
    data = request.get_json()
    if role == 'admin': 
        id_prompt = data.get('id_prompt')
         # Vérification que tous les champs sont remplis
        if not id_prompt:
            return jsonify({'error': 'Veuillez entrer l id du prompt'}), 400
        try:
            db.cur.execute("DELETE FROM prompt WHERE id_prompt = %s", (id_prompt,))
            db.conn.commit()

            return jsonify({'message': 'votre Prompt a été supprimer avec succès'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Vous n\'avez pas les droits pour créer un prompt'}), 403



@prompt_pb.route('/search', methods=['GET'])
def search_prompt():
    # Récupération du terme de recherche depuis les paramètres de la requête
    term = request.args.get('term')
    if not term:
        return jsonify({'error': 'Veuillez fournir un terme de recherche'}), 400

    try:
        # Exécution de la requête SQL avec LIKE
        search_term = f"%{term}%"
        db.cur.execute("SELECT * FROM prompt WHERE contenu LIKE %s", (search_term,))
        results = db.cur.fetchall()
        return jsonify(results), 200

        if not results:
            return jsonify({'message': 'Aucun prompt trouvé'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
        
        

    
    
        
        
    
