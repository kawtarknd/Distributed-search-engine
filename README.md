# Distributed-search-engine
Projet académique réalisé dans le cadre du module *Systèmes Répartis & Distribués* du master Analytique des données et intelligence artificielle – Faculté des Sciences d’Agadir.

## 📌 Objectif

Développer un *moteur de recherche distribué* permettant l’indexation, la recherche et la visualisation de données textuelles à grande échelle à l’aide des technologies *Elasticsearch, **Logstash, **Kibana*, et une API REST.

## 👥 Équipe projet

- Kawtar Kinad  
- Latifa Khair  
- Imane Moustike  
- Ayoub Kennouz  

Encadré par : *Pr. Idraiss Jaafar*

---

## 🧠 Fonctionnalités principales

- Indexation automatisée de fichiers textes à l’aide de Logstash.
- Recherche intelligente de documents via une API REST.
- Visualisation des statistiques de recherche dans Kibana.
- Architecture distribuée pour une meilleure performance et scalabilité.

---

## 🏗️ Architecture du système

L’architecture du moteur de recherche est composée de :

- *Logstash* : collecte, transformation et transfert des données vers Elasticsearch.
- *Elasticsearch* : moteur de recherche distribué.
- *Kibana* : visualisation des données indexées.
- *API REST (Flask)* : permet à l'utilisateur de faire des requêtes de recherche.
- (Optionnel) *Interface utilisateur web* : pour tester les recherches de manière plus intuitive.

---

## 📊 Diagrammes UML

### 1. Cas d’utilisation
<p align="center">
  <img src="https://github.com/user-attachments/assets/51f80836-26e0-4686-8cc0-a0cd440c582b" alt="Diagramme Cas d'Utilisation">
</p>

### 2. Classes
<p align="center">
  <img src="https://github.com/user-attachments/assets/78cedf81-229c-42d8-94d3-ea98d662f575" alt="Diagramme Classes">
</p>

### 3. Séquence
<p align="center">
  <img src="https://github.com/user-attachments/assets/6748333c-c255-410d-8f91-3e69011f6a9c" alt="Diagramme Séquence">
</p>

### 4. Déploiement
<p align="center">
  <img src="https://github.com/user-attachments/assets/2842b91e-8d54-47f8-b441-dbd9300ee52a" alt="Diagramme Déploiement">
</p>

### 5. Activité
<p align="center">
  <img src="https://github.com/user-attachments/assets/7077ac5d-f0d1-4718-92f9-8f99126c0002" alt="Diagramme Activité">
</p>

---

## 🧪 Technologies utilisées

- 🟦 *Elasticsearch* — stockage et moteur de recherche distribué
- 🟧 *Logstash* — pipeline d’ingestion de données
- 🟨 *Kibana* — visualisation
- 🟩 *Flask* — création d’une API web simple

---
