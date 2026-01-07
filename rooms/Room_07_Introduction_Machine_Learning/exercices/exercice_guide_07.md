# Exercice guidé : Premier modèle ML

## Contexte métier

Prédire l'espérance de vie à partir d'indicateurs socio-économiques.

## Objectifs

1. Charger `indicateurs_socio_economiques.csv`
2. Préparer les données (features et target)
3. Séparer train/test
4. Entraîner une régression linéaire
5. Évaluer la performance

## Étapes détaillées

### Étape 1 : Chargement et préparation

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('../../data/indicateurs_socio_economiques.csv')
```

### Étape 2 : Définir features et target

Features (X) : toutes les colonnes sauf `esperance_vie` et `pays`/`annee`
Target (y) : `esperance_vie`

### Étape 3 : Split train/test

Utilisez `train_test_split` avec `test_size=0.2`

### Étape 4 : Entraînement

Créez et entraînez un modèle `LinearRegression`

### Étape 5 : Évaluation

Calculez RMSE et R² sur le test set

## Livrables

- Code complet commenté
- Métriques de performance
- Interprétation des résultats

