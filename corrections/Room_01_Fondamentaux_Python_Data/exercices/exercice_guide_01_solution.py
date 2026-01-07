# Solution de l'exercice guidé 01 : Analyse de transactions

transactions = [
    {'produit': 'Laptop', 'prix': 899.99, 'quantite': 2, 'client_id': 101},
    {'produit': 'Souris', 'prix': 25.50, 'quantite': 5, 'client_id': 102},
    {'produit': 'Clavier', 'prix': 79.99, 'quantite': 3, 'client_id': 101},
    {'produit': 'Écran', 'prix': 299.99, 'quantite': 1, 'client_id': 103},
    {'produit': 'USB', 'prix': 15.00, 'quantite': 10, 'client_id': 102}
]

# Étape 1 : Calculer les montants totaux
for transaction in transactions:
    transaction['montant_total'] = transaction['prix'] * transaction['quantite']

print("=== Étape 1 : Transactions avec montant total ===")
for trans in transactions:
    print(f"{trans['produit']}: {trans['montant_total']:.2f}€")

# Étape 2 : Trouver la transaction la plus importante
transaction_max = max(transactions, key=lambda t: t['montant_total'])
print(f"\n=== Étape 2 : Transaction la plus importante ===")
print(f"Produit: {transaction_max['produit']}, Montant: {transaction_max['montant_total']:.2f}€")

# Étape 3 : Calculer le chiffre d'affaires total
ca_total = sum(t['montant_total'] for t in transactions)
print(f"\n=== Étape 3 : Chiffre d'affaires total ===")
print(f"CA total: {ca_total:.2f}€")

# Étape 4 : Filtrer les transactions importantes (> 100€)
transactions_importantes = [t for t in transactions if t['montant_total'] > 100]
print(f"\n=== Étape 4 : Transactions importantes (> 100€) ===")
for trans in transactions_importantes:
    print(f"{trans['produit']}: {trans['montant_total']:.2f}€")

