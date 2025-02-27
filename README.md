**Execution du script avec l'exposition API Flask**

> python3 app.py


**Requête API** _(depuis un autre shell)_

> curl -X POST http://localhost:5000/flat-tax -H "Content-Type: application/json" -d '{"montant_investi": 1000, "montant_sortie": 2000}'


---

**Build de l'image Docker**

> docker build -t calcul_fiscal-api .

**Lancement du container**
> docker run -d -p 5000:5000 fiscal-api
