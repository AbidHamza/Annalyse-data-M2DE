# Exercice guidé : Analyse de transactions

## Contexte métier

Vous travaillez pour un service comptable et vous devez traiter une liste de transactions. Votre tâche est de calculer différents indicateurs à partir de ces données.

## Données

```python
transactions = [
    {'produit': 'Laptop', 'prix': 899.99, 'quantite': 2, 'client_id': 101},
    {'produit': 'Souris', 'prix': 25.50, 'quantite': 5, 'client_id': 102},
    {'produit': 'Clavier', 'prix': 79.99, 'quantite': 3, 'client_id': 101},
    {'produit': 'Écran', 'prix': 299.99, 'quantite': 1, 'client_id': 103},
    {'produit': 'USB', 'prix': 15.00, 'quantite': 10, 'client_id': 102}
]
```

## Questions guidées

### Étape 1 : Calculer les montants totaux

Pour chaque transaction, calculez le montant total (prix × quantite) et ajoutez-le comme nouvelle clé dans le dictionnaire.

**Indice** : Utilisez une boucle `for` pour parcourir la liste de transactions.

### Étape 2 : Trouver la transaction la plus importante

Identifiez la transaction avec le montant total le plus élevé.

**Indice** : Utilisez `max()` avec une fonction lambda ou une compréhension de liste.

### Étape 3 : Calculer le chiffre d'affaires total

Calculez la somme de tous les montants totaux.

**Indice** : Utilisez une compréhension de liste pour extraire les montants, puis `sum()`.

### Étape 4 : Filtrer les transactions importantes

Créez une nouvelle liste contenant uniquement les transactions dont le montant total est supérieur à 100 euros.

**Indice** : Utilisez une compréhension de liste avec une condition.

## Solution attendue

Votre code doit :
1. Afficher chaque transaction avec son montant total
2. Afficher la transaction la plus importante
3. Afficher le chiffre d'affaires total
4. Afficher la liste des transactions importantes

