---
nav_title: Exporter les données de segment en CSV
article_title: Exporter les données de segment en CSV
page_order: 2
page_type: Référence
description: "Cet article de référence couvre la façon d'exporter les données de segment vers CSV."
---

# Exportation vers CSV

Pour demander un export CSV des données utilisateur à partir d'un segment, cliquez sur le bouton "Données utilisateur" en haut à droite lors de l'édition d'un segment:

!\[csvexport\]\[1\]

Vous pouvez également demander une exportation CSV depuis la page principale des Segments en cliquant sur l'icône d'engrenage sur le côté droit pour accéder à ce menu déroulant :

!\[csvexport2\]\[2\]

La sortie CSV contient les données de chaque profil utilisateur capturées dans le segment au moment de l'exportation. Vous pouvez exporter n'importe quel segment en cliquant sur l'icône d'engrenage et l'export CSV. Braze va générer le rapport en arrière-plan et l'envoyer par courriel à l'utilisateur qui est actuellement connecté.

{% alert important %}
En raison des restrictions sur la taille des fichiers, votre exportation peut échouer si la taille estimée de votre segment est supérieure à 500 000 utilisateurs. Notez que cette restriction utilise la taille estimée de votre segment, et non le calcul exact. Si la taille de votre fichier est trop grande, pensez à utiliser [numéros de compartiments aléatoires]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute) pour diviser votre base utilisateur en plusieurs segments, puis les combiner après l'exportation. Par exemple, si vous devez diviser votre segment en 2 segments différents, vous pouvez le faire avec les filtres suivants :

- Segment 1 : le nombre de segments aléatoires est inférieur à 5000 (incluant 0-4999)
- Segment 2 : Le nombre de segments aléatoires est supérieur à 4999 (comprend 5000-9999)

{% endalert %}

Si vous avez [lié vos identifiants Amazon S3 à Braze][26], alors le CSV sera téléchargé dans votre compartiment S3 sous la clé `segment-export/SEGMENT_ID/AAAA-MM-dd/users-RANDOMSTRING. IP`. Le lien qui vous est envoyé expirera après 1 jour d'exportation et nécessite que vous soyez connecté au tableau de bord pour y accéder.

Données incluses dans les exportations:

- Toutes les données de l'utilisateur
    - Identifiant de l'utilisateur
    - Prénom
    - Nom de famille
    - Fuseau horaire
    - Ville
    - Sexe
    - Adresse e-mail
    - Numéro de téléphone
    - Nombre de jetons Push
    - Nom d'utilisateur Twitter
    - Nombre de sessions
    - Première session
    - Dernière session
    - Dernière version de l'application utilisée
    - Total d'Achat In-App
    - Heure de désinscription par e-mail
    - Infos sur l'appareil
    - Nombre d'IDFAs
    - Nombre d'IDFV
    - Événements personnalisés
    - Attributs personnalisés
- Adresses e-mail
    - Identifiant de l'utilisateur
    - Prénom
    - Nom de famille
    - Adresse e-mail
    - Date de désinscription par e-mail
    - Courriel Date d'Opt-in

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article [dépannage]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}
[1]: {% image_buster /assets/img_archive/csvexport.png %} [2]: {% image_buster /assets/img_archive/csvexport2.png %}

[26]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration
