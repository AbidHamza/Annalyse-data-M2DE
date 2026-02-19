# Room 10 : Introduction aux LLM (Large Language Models)

## Fil rouge

Vous travaillez pour une entreprise qui souhaite comprendre comment fonctionnent les modèles de langage utilisés aujourd'hui (assistants conversationnels, génération de texte). Plutôt que d'utiliser des API sans comprendre, vous allez construire un petit LLM from scratch pour en maîtriser les principes.

**Progression en 4 étapes :**
1. Comprendre le principe (Qu'est-ce qu'un LLM ?)
2. Préparer le texte (Tokenisation)
3. Construire et entraîner le modèle (Architecture et entraînement)
4. Utiliser le modèle pour générer du texte (Génération)

## Objectif de la room

Cette room introduit les concepts fondamentaux des LLM en construisant un petit modèle from scratch. Vous apprendrez ce qu'est un LLM, comment préparer les données (tokenisation), comment entraîner un modèle et comment générer du texte.

## Notions abordées

1. **Qu'est-ce qu'un LLM ?**
   - Prédiction du token suivant
   - Différence avec un moteur de recherche
   - Boucle autoregressive

2. **Tokenisation**
   - Texte vers tokens
   - Vocabulaire et encodage/décodage
   - Préparation des données pour le modèle

3. **Architecture et entraînement**
   - Embeddings
   - Couches et head de prédiction
   - Boucle d'entraînement (loss, backward, optimizer)

4. **Génération**
   - Sampling et température
   - Génération autoregressive
   - Utilisation du modèle entraîné

## Lien avec le métier

Les LLM sont au cœur des assistants conversationnels, de la génération de texte et de nombreuses applications IA. Comprendre leur fonctionnement permet de mieux les utiliser, les adapter (fine-tuning) et en évaluer les limites.

## Consignes de travail

1. Suivez les notebooks dans l'ordre : `01_qu_est_ce_qu_un_llm.ipynb`, `02_tokenisation.ipynb`, `03_architecture_et_entrainement.ipynb`, `04_generation.ipynb`
2. Lisez attentivement les explications dans les cellules Markdown
3. Complétez les cellules de code marquées "A COMPLETER"
4. Exécutez chaque cellule pour vérifier votre compréhension
5. Consultez les exercices dans le dossier `exercices/` après avoir terminé les notebooks

## Prérequis

- Python de base (variables, boucles, fonctions)
- Bases numpy (Room 01)
- PyTorch pour les notebooks 03 et 04 (installation optionnelle : `pip install torch`)

## Dépendances

```
pip install torch
```

Optionnel pour la tokenisation avancée :
```
pip install tiktoken
```
