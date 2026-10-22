import json
import os



FICHIER = "taches.json"



def charger_taches():
    """Lit le fichier JSON et retourne la liste des tâches."""
    if os.path.exists(FICHIER):
        try:
            with open(FICHIER, "r", encoding="utf-8") as f:
                print(f)
                return json.load(f)
        except :
            return []
    return []  


def sauvegarder_taches(taches):
    """Écrit la liste des dépenses dans le fichier JSON."""
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(taches, f, ensure_ascii=False, indent=4)

def ajouter_tache(taches):
    """ Demande un titre et la tâche a la liste"""
    titre = input("titre de la tâche :")
    if titre =="":
        print('le titre ne peut pas etre vide.')
        return
    todo={"id":len(taches)+1,
          "titre":titre ,
            "status":False}
    taches.append(todo)
    sauvegarder_taches(taches)
    

def afficher_taches(taches):
    """affiche toutes les tâches enregistrée."""
    if len(taches) == 0:
        print("Aucune tâche enregistrée")
        return
    for i in range(len(taches)):
        print("id:",taches[i]["id"], " tache: " ,taches[i]["titre"] , " status: ", "Done" if taches[i]["status"]==True else "Not Done"  )
       
def modifier_tache(taches):
    afficher_taches(taches)
    try:
       id=int(input("Entre le numéro de la tâche dont tu veux changer le statut : "))
    except :
      print('choix invalide')
      return
    for i in range(len(taches)):
        if(taches[i]["id"]==id):
            taches[i]["status"]=True
            return
    
    
    
    
    
    
def menu():
    # Charger les tâches enregistrées
    taches = charger_taches()

    # Répéter le menu jusqu'à ce que l'utilisateur quitte
    while True:
        print("\n===== GESTION DES TÂCHES =====")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. modifier le status d'une tâche")
        print("4. Quitter")

        # Demander le choix de l'utilisateur
        choix = input("Votre choix : ")

        # Exécuter l'action correspondante
        if choix == "1":
            ajouter_tache(taches)

        elif choix == "2":
            afficher_taches(taches)

        elif choix == "3":
            modifier_tache(taches)
            
        elif choix == "4":
            print("Au revoir !")
            break
            
        else:
            print("Choix invalide, réessayez.")


# ---------- Lancement du programme ----------

menu()
