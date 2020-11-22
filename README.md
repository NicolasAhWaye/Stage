# Stage
Déployement
Installer les requirements
connection à la base de donnée
faire la commande ./manage.py makemigrations
puis ./manage.py migrate
et ./manage.py runserver

Temps estimé:15h
3h: réflexion de l'architecture
4h:déploiement de l'architecture
6h: contruction des foctionnalité
2h: déploiement
J'ai coder ce programme sur Pycharm qui est un IDE Python/Django. J'ai décidé de crée 2 models soit un pour les dates d'expirations et un pour les GTINs. Pour le design de mon application j'ai utiliser un template Boostrap.
Model:
Expiration: date type DateField()
GTIN: numero type char et date_expiration type OneToOneField()
Amélioration:
Création d'un moteur de recherche
Réflexions sur d'autres fonctionnalités.
Une Alerte de rapprochement de la date limite d'expiration
