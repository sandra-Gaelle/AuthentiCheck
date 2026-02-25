import tensorflow as tf
from models.predict import predict_article

# 1. Charger le modèle (essentiel avant l'inférence)
model = tf.keras.models.load_model('models/fake_news_model.keras')

text = "Remplacer par votre texte"
predict_article(text, model)

print(f"Résultat : {resultat['prediction']} (Score : {resultat['probability_real']:.2f})")
