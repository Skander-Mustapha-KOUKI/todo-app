# Gestionnaire de tâches (console)

Petit programme Python en ligne de commande pour gérer une liste de tâches.

## Fonctionnalités

- Ajouter une tâche
- Afficher toutes les tâches
- Changer le statut d'une tâche (Not Done → Done)
- Sauvegarde automatique dans un fichier JSON

## Prérequis

- Python 3.8+ (aucune bibliothèque externe)

## Lancer le projet

```bash
python todo.py
```

## Utilisation

```
===== GESTION DES TÂCHES =====
1. Ajouter une tâche
2. Afficher les tâches
3. modifier le status d'une tâche
4. Quitter
```

Tape le numéro de l'option puis appuie sur Entrée.

## Données

Les tâches sont enregistrées dans `taches.json`, créé automatiquement au premier ajout.

```json
{
    "id": 1,
    "titre": "Réviser Python",
    "status": false
}
```
