# 🛡️ AuthentiCheck: Recommender System & Fake News Detection

[![MLflow](https://img.shields.io/badge/MLflow-Tracking-blue)](https://mlflow.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-orange)](https://tensorflow.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## 📌 Vision du Projet
Dans un écosystème numérique saturé, l'intégrité de l'information est un pilier de la confiance utilisateur. **AuthentiCheck** est un système de détection basé sur le NLP conçu pour attribuer un **score d'authenticité** aux contenus textuels. 

Ce projet dépasse la simple classification technique pour s'inscrire dans une démarche d'**IA Responsable**, visant à mitiger les risques liés à la désinformation automatisée (Deepfakes textuels et propagande).

## 🚀 Caractéristiques Techniques (V1)
- **Modèle Deep Learning** : Architecture Bi-LSTM (Bidirectional LSTM) développée avec **TensorFlow/Keras** pour capturer le contexte sémantique long-terme.
- **Pipeline MLOps** : Intégration complète de **MLflow** pour le tracking des expérimentations (Loss, Accuracy, AUC) et la gestion du **Model Registry**.
- **Prétraitement Intégré** : Utilisation de la couche `TextVectorization` native pour garantir la portabilité du modèle de l'entraînement vers l'inférence.
- **Infrastructure Cloud** : Déploiement d'un tunnel sécurisé via **Ngrok** pour exposer l'interface de monitoring MLflow depuis un environnement distant (Google Colab).

## 🛠️ Stack Technologique
- **Langage** : Python 3.10+
- **IA** : TensorFlow, Keras, Scikit-learn
- **MLOps** : MLflow, Ngrok
- **Données** : WELFake Dataset (via Kaggle)

## 📊 Monitoring & Performance
Grâce à MLflow, chaque itération est enregistrée. Le modèle actuel atteint une excellente convergence, monitorée via l'AUC (Area Under Curve) pour garantir une robustesse face aux classes potentiellement déséquilibrées.

> **Note Éthique** : Le score d'authenticité produit n'est pas une vérité absolue mais un indicateur de probabilité basé sur des patterns linguistiques, favorisant ainsi une approche d'aide à la décision humaine plutôt qu'une censure automatisée.

## 💻 Installation & Utilisation
1. **Cloner le projet** :
   ```bash
   git clone [https://github.com/TON_USER/fake-news-detection-mlops.git](https://github.com/TON_USER/fake-news-detection-mlops.git)
2. **Installer les dépendances** :
   pip install -r requirements.txt
3. **Lancer l'inférence** :
   from models.predict import predict_article
   result = predict_article("Votre texte ici...")
   print(f"Score d'authenticité : {result['probability_real']}")
