# Exercice : Analyse de Logs Serveur (Simulés)

## Contexte

Vous travaillez pour une entreprise web qui génère des logs de connexion. Votre mission est d'analyser ces logs pour identifier les heures de pointe et les codes d'erreur fréquents.

## Données

Créez manuellement un DataFrame avec les colonnes suivantes : `ip_address`, `timestamp`, `method` (GET/POST), `status_code` (200, 404, 500), `response_time_ms`.

Exemple de données :
```python
log_data = [
    ("192.168.1.1", "2023-10-01 10:00:00", "GET", 200, 120),
    ("192.168.1.2", "2023-10-01 10:05:00", "POST", 500, 500),
    ("192.168.1.1", "2023-10-01 10:10:00", "GET", 404, 80),
    # ... ajoutez d'autres lignes
]
```

## Questions

1. Initialisez une `SparkSession`.
2. Créez le DataFrame `df_logs`.
3. Filtrez les requêtes qui ont un code d'erreur (différent de 200).
4. Calculez le temps de réponse moyen par type de méthode (GET vs POST).
5. (Bonus) Triez les résultats par temps de réponse décroissant.

## Livrable

Un notebook nommé `exercice_logs_server.ipynb` contenant votre code et vos analyses.
