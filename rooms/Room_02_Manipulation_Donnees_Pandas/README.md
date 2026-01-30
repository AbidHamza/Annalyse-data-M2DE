# Room 02 : Manipulation de données avec Pandas

## Objectif de la room

Cette room introduit pandas, la bibliothèque Python standard pour la manipulation et l'analyse de données tabulaires. Vous apprendrez à charger, explorer, filtrer et transformer des données avec pandas.

## Notions abordées

1. **Lecture de fichiers CSV**
   - Chargement de données avec `pd.read_csv()`
   - Compréhension de la structure d'un DataFrame
   - Exploration initiale des données

2. **Indexation et sélection**
   - Accès aux colonnes
   - Sélection de lignes
   - Filtrage conditionnel
   - Méthodes `.loc[]` et `.iloc[]`

3. **Filtrage de données**
   - Conditions simples et multiples
   - Opérateurs booléens
   - Indexation booléenne

4. **Agrégations**
   - Fonctions d'agrégation (sum, mean, count, etc.)
   - Groupement avec `groupby()`
   - Agrégations multiples

## Lien avec le métier

Dans un contexte professionnel, vous recevez souvent des données sous forme de fichiers CSV ou Excel. Pandas permet de :
- Charger rapidement ces données
- Explorer leur structure et leur contenu
- Filtrer pour isoler des sous-ensembles pertinents
- Agréger pour calculer des indicateurs métier (totaux, moyennes par catégorie, etc.)

Ces opérations sont la base de toute analyse de données.

## Consignes de travail

1. Suivez les notebooks dans l'ordre
2. Utilisez le dataset `ventes_commerces.csv` du dossier `/data`
3. Exécutez chaque cellule et observez les résultats
4. Complétez les exercices dans les notebooks
5. Consultez les exercices guidés puis autonomes du dossier `exercices/`

## 📝 Travail à Rendre

Pour valider cette room, vous devez rendre un **Dossier compressé (ZIP)** contenant :

1.  **Les 4 notebooks du cours complétés** : Assurez-vous d'avoir exécuté toutes les cellules.
2.  **L'exercice autonome** : Le notebook `exercices/exercice_autonome.ipynb` dûment rempli.
3.  **Une synthèse Markdown** (`synthese_pandas.md`) de 10 lignes expliquant ce que vous avez retenu sur :
    - La différence entre `loc` et `iloc`.
    - L'utilité du `groupby`.

**Format du nom de fichier** : `NOM_Prenom_Room02_Pandas.zip`
**Date limite** : Selon le calendrier de la formation.

