---
nav_title: Aperçu des données d'exportation
article_title: Aperçu des données d'exportation
page_order: 3
page_type: Référence
description: "Cet article de référence couvre la façon d'exporter les données d'utilisation de l'application."
tool:
  - Rapports
---

# Exportation des données d'aperçu

La page **Aperçu** du tableau de bord contient des données de haut niveau d'utilisation de l'application, ainsi que des statistiques détaillées de différents ICP par date. Pour obtenir des CSV d'informations à partir de cette page, définissez d'abord la période que vous voulez afficher, puis allez au graphique en bas de la page et choisissez les données à inclure dans votre exportation.

!\[Graphique d'utilisation de l'appli\]\[27\]

Vous pouvez exporter des CSV avec les données suivantes :
- Nombre de sessions par date
    - (Facultatif) Nombre de sessions pour différents segments
    - (Facultatif) Nombre de sessions pour différentes versions de l'application
- DAUs par date
    - (Facultatif) DAUs pour différents segments
- Statistiques par date de l'e-mail
    - Nombre d'emails envoyés
    - Nombre d'E-mails envoyés
    - Nombre d'e-mails ouverts
    - Nombre de clics de courriel
    - Nombre d'emails Bounces
    - Nombre d'emails signalés comme spam
- Messages dans l'application par date
    - Nombre de messages envoyés dans l'application
    - Impressions de message dans l'application
    - Nombre de messages ouverts dans l'application
- MAUX par date
- Nombre de nouveaux utilisateurs par date
- Impressions du fil d'actualité par date
- Notifications push par date
    - (Facultatif) Notifications push pour différentes plateformes d'applications
    - Nombre de notifications envoyées
    - Ouvertures totales
    - Ouvertures directes
    - Bounces
- Nombre de sessions par heure
- Nombre de sessions par MAU par date
- Stickiness par date

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}
[27]: {% image_buster /assets/img_archive/app_usage.png %}
