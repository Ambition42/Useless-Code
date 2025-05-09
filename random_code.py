import random
from random import randint
import time

def random_sentence():
    caracters = ""
    caracters_len = randint(1, 150)

    while len(caracters) < caracters_len:
        caracters += str(randint(0, 1))
    print(caracters)


while True:
    print("Chargement des résultats...")
    for x in range(randint(1, 64)):
        random_sentence()
        time.sleep(randint(0, 100) / 1000)

    random_message = randint(0, 10)
    messages = [
    "Erreur de chargement : la connexion au serveur a échoué.",
    "En attente des données...",
    "Connexion établie avec le serveur Apache.",
    "Liaison SSL...",
    "Installation du module : threading via pip.",
    "Authentification par clé SSH...",
    "Synchronisation avec le serveur NTP.",
    "Échec du handshake TLS : code 0x2F1A.",
    "Montage du disque distant /mnt/data...",
    "Mise en cache des dépendances...",
    "Analyse du trafic sur le port 443...",
    "Redémarrage du service systemd-networkd...",
    "Détection d’une boucle récursive dans le thread principal.",
    "Compression des logs système : 42.3 Mo compressés.",
    "Création de l’environnement virtuel : /env/bin/python3.7",
    "Exécution du script d’amorçage : init_env.sh",
    "Vérification du hash SHA256... terminé.",
    "Mise à jour de la base de données SQLite locale.",
    "Appel à la fonction asynchrone main()...",
    "Attente du port COM3 : périphérique non détecté.",
    "Transfert de paquets via protocole UDP...",
    "Initialisation du module numpy.core.multiarray...",
    "Attribution dynamique de l’adresse IPv6...",
    "Compilation du noyau : version 5.15.0",
    "Tentative de reconnexion dans 15 secondes...",
    "Envoi des métriques à Prometheus...",
    "Chargement du conteneur Docker : success.",
    "Écoute des événements système avec epoll...",
    "Erreur critique : segmentation fault (core dumped)",
    "Assignation des privilèges root au processus PID 4187..."
]

    print(messages[random_message])
    time.sleep(randint(0, 2000) / 1000)
