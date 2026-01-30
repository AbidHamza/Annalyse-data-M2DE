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

## Organisation de la Room (Durée estimée : 5-8h)

Cette room est dense. Prenez le temps de digérer chaque concept.

1. **Les Bases (1h)** : `notebooks/01_introduction_pyspark.ipynb`
   - Comprendre le Driver, les Workers et le DataFrame.
2. **Manipulation Réelle (1h30)** : `notebooks/02_manipulation_avancee_pyspark.ipynb`
   - Nettoyer, filtrer, et gérer les types complexes.
3. **Expertise SQL & Window (2h)** : `notebooks/03_spark_sql_deep_dive.ipynb` **(Crucial)**
   - Apprendre les Window Functions (`lead`, `lag`, `rank`) qui font la différence en entretien.
4. **Mini-Projet Final (3h)** : `notebooks/04_mini_projet_nyc_taxi.ipynb`
   - Un projet capstone complet : Ingestion -> Cleaning -> Feature Engineering -> Business Aggregats.

## Consignes de travail

Suivez l'ordre des notebooks. Le Mini-Projet finale (04) est un excellent entraînement pour valider vos acquis avant un entretien technique.

## Prérequis

- Bonne maîtrise de Python et Pandas (Rooms 01 & 02).
- Installation de Java 8+ et `pyspark`.
