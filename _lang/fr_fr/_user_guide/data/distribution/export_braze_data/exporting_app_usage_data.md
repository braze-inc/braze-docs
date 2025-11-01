---
nav_title: "Exporter les analyses/analytiques de l'utilisation (si utilisée)"
article_title: "Exportation d'analyses/analytiques de l'utilisation (si utilisées comme adjectifs)"
page_order: 3

page_type: reference
description: "Cet article de référence explique comment exporter des données de haut niveau sur l'utilisation des apps."
tool: 
  - Reports

---

# Exporter des analyses/analytiques d'utilisation (si utilisé comme adjectif)

> Cette page couvre la page d'**accueil** du tableau de bord, qui contient des données de haut niveau sur l'utilisation de l'app, ainsi que des statistiques détaillées de différents KPI par date.

Pour exporter des données au format CSV à partir de cette page :

1. Définissez la période et les apps dont vous souhaitez consulter les données. Par défaut, le tableau de bord affiche les données des 30 derniers jours pour toutes les apps.

\![Champs de la période et de l'application sur le tableau de bord de l'accueil.]({% image_buster /assets/img_archive/home_dashboard_select_date.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Faites défiler vers le bas jusqu'au graphique des **performances dans le temps**.
3\. Sélectionnez les données que vous souhaitez exporter dans le champ **Statistiques pour.**  Voir les [données disponibles](#available-data) pour l'exportation.

!Graphique des performances dans le temps sur le tableau de bord de l'accueil.]({% image_buster /assets/img_archive/home_dashboard_export.png %})

{:start="4"}
4\. Sélectionnez <i class="fas fa-bars" title="Menu contextuel Graphique"></i> puis sélectionnez votre option d'exportation.

## Données disponibles

Vous pouvez exporter des CSV contenant les données suivantes :

- Nombre de sessions par date
    - (Facultatif) Nombre de sessions pour différents segments
    - (Facultatif) Nombre de sessions pour les différentes versions de l'application
- DAUs par date
    - (Facultatif) DAU pour les différents segments
- Statistiques des e-mails par date
    - Nombre d'e-mails envoyés
    - Nombre d'e-mails délivrés
    - Nombre d'e-mails ouverts
    - Nombre de clics sur l'e-mail
    - Nombre d'e-mails rejetés
    - Nombre d'e-mails signalement de courrier indésirable
- Messages in-app par date
    - Nombre de messages in-app envoyés
    - Impressions des messages in-app
    - Nombre de messages in-app ouverts
- UAM par date
- Nombre de nouveaux utilisateurs par date
- Notifications push par date
    - (Facultatif) Notifications push pour différentes plateformes d'applications
    - Nombre de notifications push envoyées
    - Total des ouvertures
    - Ouvertures directes
    - Rebonds
- Nombre de sessions par heure
- Nombre de sessions par MAU par date
- Adhérence par date

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consultez notre article sur la [résolution des problèmes liés aux exportations.]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/) 
{% endalert %}

