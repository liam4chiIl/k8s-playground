**Execution** /n
python3 app.py

**Requête API** _(depuis un autre shell)_ /n
curl -X POST http://localhost:5000/flat-tax -H "Content-Type: application/json" -d '{"montant_investi": 1000, "montant_sortie": 2000}'
