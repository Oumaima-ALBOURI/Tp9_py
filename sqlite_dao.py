import sqlite3
from produit import Produit
from client import Client


class SQLiteDAO:

    def __init__(self):
        self.conn = sqlite3.connect("boutique.db")
        self.cursor = self.conn.cursor()
        self.creer_tables()

    # Création des tables
    def creer_tables(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prix REAL NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """)

        self.conn.commit()

    # Ajouter un produit
    def ajouter_produit(self, produit):

        self.cursor.execute("""
            INSERT INTO produits (nom, prix)
            VALUES (?, ?)
        """, (produit.nom, produit.prix))

        self.conn.commit()

    # Lister les produits
    def lister_produits(self):

        self.cursor.execute("SELECT * FROM produits")
        rows = self.cursor.fetchall()

        produits = []

        for row in rows:
            p = Produit(row[0], row[1], row[2])
            produits.append(p)

        return produits

    # Modifier le prix d'un produit
    def modifier_prix(self, id, nouveau_prix):

        self.cursor.execute("""
            UPDATE produits
            SET prix = ?
            WHERE id = ?
        """, (nouveau_prix, id))

        self.conn.commit()

        return self.cursor.rowcount > 0

    # Ajouter un client
    def ajouter_client(self, client):

        self.cursor.execute("""
            INSERT INTO clients (nom, email)
            VALUES (?, ?)
        """, (client.nom, client.email))

        self.conn.commit()

    # Lister les clients
    def lister_clients(self):

        self.cursor.execute("SELECT * FROM clients")
        rows = self.cursor.fetchall()

        clients = []

        for row in rows:
            c = Client(row[0], row[1], row[2])
            clients.append(c)

        return clients

    # Rechercher un client par email
    def rechercher_client(self, email):

        self.cursor.execute("""
            SELECT * FROM clients
            WHERE email = ?
        """, (email,))

        row = self.cursor.fetchone()

        if row:
            return Client(row[0], row[1], row[2])
        else:
            return None

    # Fermer la connexion
    def fermer(self):
        self.conn.close()