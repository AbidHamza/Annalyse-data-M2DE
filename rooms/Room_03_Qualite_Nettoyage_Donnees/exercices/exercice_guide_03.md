# Exercice guidé : Nettoyage complet d'un dataset

## Contexte métier

Vous recevez un dataset de ventes qui nécessite un nettoyage avant analyse.

## Objectifs

1. Charger le dataset `ventes_commerces.csv`
2. Identifier et traiter les valeurs manquantes
3. Détecter et supprimer les doublons
4. Identifier les outliers sur les prix et montants

## Questions guidées

### Étape 1 : Exploration initiale

Chargez le dataset et affichez :
- Le nombre de lignes et colonnes
- Les types de données
- Un résumé des valeurs manquantes

### Étape 2 : Valeurs manquantes

Identifiez les colonnes avec valeurs manquantes. Pour chaque colonne :
- Calculez le pourcentage de valeurs manquantes
- Décidez d'une stratégie appropriée (suppression ou imputation)

### Étape 3 : Doublons

Vérifiez s'il existe des doublons exacts dans le dataset. Si oui, supprimez-les.

### Étape 4 : Outliers

Utilisez la méthode IQR pour identifier les outliers sur `prix_unitaire` et `montant_total`. Visualisez-les avec un boxplot (si vous connaissez matplotlib).

### Étape 5 : Dataset nettoyé

Créez un nouveau dataset nettoyé et comparez sa taille avec l'original.

## Livrables

- Code commenté pour chaque étape
- Justification des choix de nettoyage
- Résumé des transformations appliquées

