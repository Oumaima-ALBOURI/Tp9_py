from produit import Produit
from client import Client


def afficher_menu():
    print("\n========== GESTION BOUTIQUE ==========")
    print("1. Ajouter un produit")
    print("2. Lister les produits")
    print("3. Modifier le prix d'un produit")
    print("4. Ajouter un client")
    print("5. Lister les clients")
    print("6. Rechercher un client par email")
    print("0. Quitter")
    print("===================================")


def main():

    print("===== CHOIX DE LA BASE DE DONNEES =====")
    print("1. SQLite")
    print("2. MySQL")

    choix_db = input("Votre choix : ")

    # Choisir le DAO
    try:
        if choix_db == "1":
            from sqlite_dao import SQLiteDAO
            dao = SQLiteDAO()
            print("Connexion SQLite réussie.")

        elif choix_db == "2":
            from mysql_dao import MySQLDAO
            dao = MySQLDAO()
            print("Connexion MySQL réussie.")

        else:
            print("Choix invalide.")
            return

    except Exception as e:
        print("Erreur de connexion :", e)
        return

    # Menu principal
    try:

        while True:

            afficher_menu()
            choix = input("Votre choix : ")

            try:

                # Ajouter un produit
                if choix == "1":

                    nom = input("Nom du produit : ")
                    prix = float(input("Prix du produit : "))

                    if prix < 0:
                        print("Le prix ne peut pas être négatif.")
                        continue

                    produit = Produit(None, nom, prix)
                    dao.ajouter_produit(produit)

                    print("Produit ajouté avec succès.")

                # Lister les produits
                elif choix == "2":

                    produits = dao.lister_produits()

                    if len(produits) == 0:
                        print("Aucun produit trouvé.")
                    else:
                        print("\n--- LISTE DES PRODUITS ---")
                        for produit in produits:
                            print(produit)

                # Modifier le prix
                elif choix == "3":

                    id = int(input("ID du produit : "))
                    nouveau_prix = float(input("Nouveau prix : "))

                    if nouveau_prix < 0:
                        print("Le prix ne peut pas être négatif.")
                        continue

                    resultat = dao.modifier_prix(id, nouveau_prix)

                    if resultat:
                        print("Prix modifié avec succès.")
                    else:
                        print("Produit introuvable.")

                # Ajouter un client
                elif choix == "4":

                    nom = input("Nom du client : ")
                    email = input("Email du client : ")

                    client = Client(None, nom, email)
                    dao.ajouter_client(client)

                    print("Client ajouté avec succès.")

                # Lister les clients
                elif choix == "5":

                    clients = dao.lister_clients()

                    if len(clients) == 0:
                        print("Aucun client trouvé.")
                    else:
                        print("\n--- LISTE DES CLIENTS ---")
                        for client in clients:
                            print(client)

                # Rechercher un client
                elif choix == "6":

                    email = input("Email du client à rechercher : ")

                    client = dao.rechercher_client(email)

                    if client is not None:
                        print("Client trouvé :")
                        print(client)
                    else:
                        print("Aucun client avec cet email.")

                # Quitter
                elif choix == "0":

                    print("Fermeture du programme.")
                    break

                else:
                    print("Choix invalide.")

            except ValueError:
                print("Erreur : saisie numérique invalide.")

            except Exception as e:
                print("Erreur lors de l'opération :", e)

    finally:
        dao.fermer()
        print("Connexion à la base fermée.")


if __name__ == "__main__":
    main()