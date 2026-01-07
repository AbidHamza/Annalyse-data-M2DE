# Datasets disponibles

Ce dossier contient les fichiers CSV utilisés dans les différentes rooms de la formation.

## ventes_commerces.csv

### Contexte

Dataset de ventes d'un commerce de détail. Chaque ligne représente une transaction de vente.

### Description des colonnes

- **date** : Date de la transaction (format YYYY-MM-DD)
- **produit_id** : Identifiant unique du produit vendu (1 à 20)
- **categorie** : Catégorie du produit (Electronique, Meuble, Vetement, Alimentation, Sport)
- **prix_unitaire** : Prix unitaire du produit en euros
- **quantite** : Quantité de produits vendus dans cette transaction
- **region** : Région de vente (Nord, Sud, Est, Ouest, Centre)
- **client_id** : Identifiant du client (100 à 499)
- **montant_total** : Montant total de la transaction (prix_unitaire × quantite)

### Objectif analytique

Ce dataset permet d'analyser :
- L'évolution des ventes dans le temps
- La performance par catégorie de produits
- Les variations géographiques des ventes
- Le comportement d'achat des clients
- La segmentation des transactions

### Taille

1000 lignes

---

## capteurs_iot.csv

### Contexte

Dataset de mesures de capteurs IoT installés dans plusieurs bâtiments. Les données sont collectées toutes les heures sur une année.

### Description des colonnes

- **timestamp** : Horodatage de la mesure (format YYYY-MM-DD HH:MM:SS)
- **capteur_id** : Identifiant du capteur (TEMP_001, TEMP_002, HUM_001, PRESSURE_001)
- **valeur** : Valeur mesurée par le capteur
- **unite** : Unité de mesure (°C pour température, % pour humidité, hPa pour pression)
- **batiment** : Bâtiment où est installé le capteur (BAT_A, BAT_B, BAT_C)

### Objectif analytique

Ce dataset permet d'analyser :
- Les séries temporelles de mesures
- Les patterns temporels (saisonnalité, cycles journaliers)
- Les anomalies dans les mesures
- Les corrélations entre différents types de capteurs
- Les différences entre bâtiments

### Taille

8760 lignes (1 an de données horaires)

---

## indicateurs_socio_economiques.csv

### Contexte

Dataset d'indicateurs socio-économiques par pays et année pour plusieurs pays européens.

### Description des colonnes

- **pays** : Nom du pays (France, Allemagne, Espagne, Italie, Pologne)
- **annee** : Année de l'indicateur (2020 à 2023)
- **pib_par_habitant** : Produit Intérieur Brut par habitant en euros
- **taux_chomage** : Taux de chômage en pourcentage
- **taux_scolarisation** : Taux de scolarisation en pourcentage
- **densite_population** : Densité de population (habitants/km²)
- **depenses_sante_pourcent** : Dépenses de santé en pourcentage du PIB
- **esperance_vie** : Espérance de vie à la naissance en années

### Objectif analytique

Ce dataset permet d'analyser :
- L'évolution des indicateurs dans le temps
- Les corrélations entre variables économiques et sociales
- Les différences entre pays
- Les modèles prédictifs de variables socio-économiques

### Taille

500 lignes

