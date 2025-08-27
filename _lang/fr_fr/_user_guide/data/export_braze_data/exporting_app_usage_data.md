---
nav_title: "Exporter les analyses d'utilisation"
article_title: "Exporter les analyses d'utilisation"
page_order: 3

page_type: reference
description: "Cet article de référence explique comment exporter les données de haut niveau sur l’utilisation des applications."
tool: 
  - Reports

---

# Exportation des analyses d'utilisation

> Cette page couvre la page d'**accueil** du tableau de bord, qui contient des données de haut niveau sur l'utilisation de l'app, ainsi que des statistiques détaillées de différents KPI par date.

Pour exporter des données au format CSV à partir de cette page :

1. Définissez la période et les applications pour lesquelles vous souhaitez afficher les données. Par défaut, le tableau de bord affiche les données des 30 derniers jours pour toutes les applications.

![Période et champs d'application sur le tableau de bord de l'accueil.]({% image_buster /assets/img_archive/home_dashboard_select_date.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Faites défiler vers le bas jusqu'au graphique **Performance au fil du temps**.
3\. Sélectionnez les données que vous souhaitez exporter dans le champ **Statistiques Pour**. Consultez les [données disponibles](#available-data) pour votre exportation.

![Graphique des performances au fil du temps sur le tableau de bord de l'accueil.]({% image_buster /assets/img_archive/home_dashboard_export.png %})

{:start="4"}
4\. Sélectionnez <i class="fas fa-bars" title="Menu contextuel Graphique"></i> puis sélectionnez votre option d'exportation.

## Données disponibles

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
    - Impressions du in-app Message
    - Nombre de messages in-app ouverts
- MAU par date
- Nombre de nouveaux utilisateurs par date
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
Pour obtenir de l'aide sur les exportations CSV et API, consultez notre article [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

