# Exercice guidé : Pipeline LLM complet

## Fil rouge

Vous avez suivi les 4 notebooks. Vous allez refaire le pipeline complet sur un corpus personnalisé pour valider vos acquis.

## Contexte

Vous disposez du fichier `../../data/sample_text.txt` et des notions des notebooks 01 à 04. L'objectif est de produire un notebook ou script complet qui charge, tokenise, entraîne et génère.

## Ce qu'on attend

- Un notebook ou script complet exécutable
- À l'étape 1 : données chargées et affichage de la taille du corpus
- À l'étape 2 : vocabulaire construit, exemple d'encodage/décodage
- À l'étape 3 : modèle entraîné, loss qui diminue au fil des epochs
- À l'étape 4 : texte généré à partir d'un prompt

Pas de résultat attendu affiché. Vous exécutez et vérifiez par vous-même.

## Étapes détaillées

### Étape 1 : Chargement des données

Chargez `../../data/sample_text.txt`. Affichez le nombre de caractères. Vérifiez que le fichier est bien lu.

### Étape 2 : Tokenisation

Créez le vocabulaire (char_to_id, id_to_char). Encodez une phrase du corpus. Décodez-la pour vérifier.

### Étape 3 : Entraînement

Utilisez le modèle SimpleLLM du notebook 03. Entraînez sur au moins 50 epochs. La loss doit diminuer. Sauvegardez le modèle.

### Étape 4 : Génération

Implémentez la fonction generate(). Testez avec un prompt du corpus et temperature=0.8. Le texte généré doit être cohérent avec le style du corpus.

## Livrables

- Code complet commenté
- Modèle sauvegardé
- Exemple de texte généré (sans valeur cible, vous jugez la qualité)
