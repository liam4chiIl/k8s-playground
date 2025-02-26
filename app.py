from flask import Flask, request, jsonify

# Création de l’application Flask
app = Flask(__name__)

# Fonction de calcul de la Flat Tax
def calcul_flat_tax(montant_investi, montant_sortie):
    if montant_sortie <= montant_investi:
        return {"message": "Aucune imposition, vous n'avez pas réalisé de gains."}
    else:
        montant_a_payer = montant_sortie * 0.3
        return {"montant_a_payer": round(montant_a_payer, 2)}

# Route API qui accepte les requêtes POST
@app.route('/flat-tax', methods=['POST'])
def api_flat_tax():
    # Récupération des données envoyées
    data = request.get_json()
    
    # Vérification des champs requis
    if "montant_investi" not in data or "montant_sortie" not in data:
        return jsonify({"error": "Les champs 'montant_investi' et 'montant_sortie' sont requis"}), 400

    # Calcul et retour de la réponse JSON
    resultat = calcul_flat_tax(data["montant_investi"], data["montant_sortie"])
    return jsonify(resultat)

# Démarrage du serveur Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
