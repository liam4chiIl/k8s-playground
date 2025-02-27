# **🚀 TP : Déploiement d’une API Flask sur Docker & Kubernetes**  

Ce projet transforme un **script Python CLI** en une **API web** avec Flask, puis la conteneurise avec **Docker** avant de la déployer sur **Minikube (Kubernetes)**.  

## **🛠️ Objectifs**  
✅ Convertir un script de calcul fiscal en API REST.  
✅ Conteneuriser l’application avec **Docker**.  
✅ Tester l’API localement via **cURL**.  
✅ Déployer l’API sur **Minikube (Kubernetes)**.  

## **📦 Technologies utilisées**  
- **Python 3.9** + Flask  
- **Docker** (build & run de l’image)  
- **Minikube & Kubernetes** (déploiement)  

## **📜 Fonctionnement**  
1️⃣ L’API expose une route `POST /flat-tax` qui calcule une taxe sur un investissement.  
2️⃣ Docker est utilisé pour conteneuriser et exécuter l’API.  
3️⃣ Minikube est utilisé pour simuler un cluster Kubernetes et orchestrer l’application.  


**Execution du script avec l'exposition API Flask**

> python3 app.py


**Requête API** _(depuis un autre shell)_

> curl -X POST http://localhost:5000/flat-tax -H "Content-Type: application/json" -d '{"montant_investi": 1000, "montant_sortie": 2000}'


---

**Build de l'image Docker**

> docker build -t calcul_fiscal-api .

**Lancement du container**
> docker run -d -p 5000:5000 fiscal-api
