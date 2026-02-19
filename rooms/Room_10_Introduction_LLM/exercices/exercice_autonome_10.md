# Exercice autonome : Adapter le pipeline à un nouveau corpus

## Fil rouge

Vous maîtrisez le pipeline LLM. Adaptez-le à un nouveau cas d'usage pour démontrer votre autonomie.

## Contexte

Choisissez un corpus différent : citations, poèmes, articles de presse, ou tout autre texte cohérent. Le corpus doit être suffisant (au moins 10 000 caractères) pour que le modèle puisse apprendre des patterns.

## Ce qu'on attend

- Un corpus différent de sample_text.txt
- Un modèle entraîné sur ce corpus
- Des exemples de génération (au moins 3 avec des températures différentes)
- Une analyse courte : le texte généré est-il cohérent avec le style du corpus ?

## Critères de réussite

- Le code charge, tokenise, entraîne et génère sans erreur
- Le texte généré reflète le style ou le vocabulaire du corpus (même de manière approximative pour un petit modèle)
- Vous savez expliquer l'effet de la température sur les exemples produits

## Livrables

- Notebook ou script complet
- Fichier du corpus utilisé (ou lien vers la source)
- Modèle sauvegardé
- Court paragraphe d'analyse des résultats
