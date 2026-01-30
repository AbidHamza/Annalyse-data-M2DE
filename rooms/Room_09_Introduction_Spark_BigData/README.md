# Room 09 : Introduction au Big Data avec Apache Spark

## Objectif de la room

Cette room a pour objectif d'introduire les concepts fondamentaux du Big Data à travers le framework Apache Spark. Vous apprendrez à manipuler des volumes de données importants en utilisant PySpark, l'interface Python de Spark, et à comprendre la différence de paradigme par rapport à Pandas.

## Notions abordées

1. **Introduction au Big Data et Spark**
   - Différence entre Pandas (In-Memory, Single Node) et Spark (Distributed)
   - Architecture Driver/Worker
   - Concept de Lazy Evaluation

2. **Manipulation de DataFrames Spark**
   - Création de SparkSession
   - Lecteur et écriture de fichiers
   - Transformations vs Actions
   - Opérations classiques (select, filter, groupBy)

3. **Optimisation et Bonnes Pratiques**
   - Comprendre le plan d'exécution
   - Caching et Persistance

## Lien avec le métier

Dans un environnement de production traitant des téraoctets de données (logs serveurs, transactions bancaires, données IoT), les outils classiques comme Pandas atteignent leurs limites mémoire. Spark est le standard industriel pour le traitement de données à grande échelle. Savoir passer de Pandas à Spark est une compétence clé pour un Data Engineer ou un Data Scientist Senior.

## Consignes de travail

1. Ouvrez le notebook `notebooks/01_introduction_pyspark.ipynb`.
2. Lisez attentivement les explications théoriques avant d'exécuter le code.
3. Complétez les cellules de code marquées "A COMPLETER".
4. Réalisez l'exercice de synthèse dans le dossier `exercices/`.

## Prérequis

- Bonne maîtrise de Python et Pandas (Rooms 01 & 02).
- Installation de Java 8+ et `pyspark`.
