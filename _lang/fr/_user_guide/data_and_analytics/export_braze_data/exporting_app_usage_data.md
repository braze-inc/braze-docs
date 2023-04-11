---
nav_title: Exporter les données d’aperçu
article_title: Exporter les données d’aperçu
page_order: 3

page_type: reference
description: "Cet article de référence explique comment exporter les données sur l’utilisation des applications."
tool: 
  - Reports

---

# Exportation des données d’aperçu

La page **Overview** du tableau de bord contient des données de haut niveau sur l’utilisation de l’application, ainsi que des statistiques détaillées sur différents indicateurs clés de performance par date. Pour obtenir des CSV avec les informations de cette page, définissez d’abord le période que vous souhaitez afficher, puis accédez au graphique en bas de la page et choisissez les données à inclure dans votre exportation.

![Graphique d’utilisation de l’application][27]

Vous pouvez exporter les CSV avec les données suivantes :
- Nombre de sessions par date
    - (Facultatif) Nombre de sessions pour différents segments
    - (Facultatif) Nombre de sessions pour différentes versions d’application
- DAU par date
    - (Facultatif) DAU pour différents segments
- Statistiques e-mail par date
    - Nombre d’e-mails envoyés
    - Nombre d’e-mails livrés
    - Nombre d’e-mails ouverts
    - Nombre d’e-mails cliqués
    - Nombre de rebonds (bounce) d’e-mail
    - Nombre d’e-mails signalés comme spam
- Messages in-app par date
    - Nombre de messages in-app envoyés
    - Impressions des messages in-app
    - Nombre de messages in-app ouverts
- MAU par date
- Nombre de nouveaux utilisateurs par date
- Impressions de Fil d'actualité par date
- Notifications push par date
    - (En option) Notifications Push pour différentes plateformes d’applications
    - Nombre de notifications Push envoyées
    - Nombre total d’ouvertures
    - Ouvertures directes
    - Rebonds
- Nombre de sessions par heure
- Nombre de sessions par MAU par date
- Adhérence par date

{% alert tip %}
Pour obtenir de l’aide sur les exportations de CSV et l’API, consultez notre article [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

[27]: {% image_buster /assets/img_archive/app_usage.png %}
