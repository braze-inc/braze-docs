---
nav_title: Tableau de bord d’utilisation de l’API
article_title: Tableau de bord d’utilisation de l’API
permalink: "/api_usage/"
hidden: true
description: "Cet article donne un aperçu du tableau de bord de l'utilisation de l'API."
---

# Tableau de bord de l'utilisation de l'API

> Le tableau de bord de l'utilisation de l'API vous permet de surveiller le trafic de votre API REST entrant dans Braze afin de comprendre les tendances de votre utilisation de nos API REST et de résoudre les problèmes éventuels.

Le tableau de bord par défaut est une vue de toutes les demandes d'API REST entrantes pour votre espace de travail au cours de la dernière journée (24 heures). En fonction de votre cas d'utilisation, vous pouvez ajuster les contrôles du tableau de bord pour filtrer ou regrouper le trafic et également configurer la plage horaire du tableau de bord.

![]({% image_buster /assets/img/api_usage_dashboard/api_usage_dashboard.png %})

## Statistiques sommaires

- **Nombre total de requêtes :** Le nombre total de demandes envoyées à Braze pour votre espace de travail actuel, compte tenu des filtres et des contrôles appliqués au tableau de bord.
- **Taux de succès :** Pourcentage du total des demandes pour lesquelles Braze a envoyé une réponse positive à l'adresse `2XX`.
- **Taux d'erreur :** Pourcentage du total des demandes pour lesquelles Braze a émis une réponse d'erreur `4XX` ou `5XX`.

## Contrôles du tableau de bord

![]({% image_buster /assets/img/api_usage_dashboard/filters.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

### Filtres

Appliquez des filtres pour réduire l'affichage du trafic de l'API REST pour votre espace de travail. Les filtres disponibles sont les suivants :

- Endpoint de l’API
- Clé API
- Code de réponse

### Données du groupe

Regroupez les données en diverses séries de données afin d'explorer différents modèles d'utilisation. Les options de regroupement disponibles sont les suivantes :

- Codes de réponse (par défaut)
- Endpoint de l’API
- Clé API
- Réussite et échec uniquement

### Date

Ajustez le filtre de date pour afficher une plage de temps plus petite ou plus grande selon vos besoins. Les options de dates disponibles sont les suivantes :

- Aujourd'hui (par défaut)
- Personnalisé
- 3 dernières heures
- 6 dernières heures
- 12 dernières heures
- 24 dernières heures
- Hier
- 7 derniers jours
- 14 derniers jours
- 30 derniers jours
- Dernier mois à ce jour

{% alert note %}
Les options **3 dernières heures** et **6 dernières heures** affichent le trafic par minutes. Des périodes plus longues permettent d'afficher le trafic par heures ou par jours.
{% endalert %}

## Considérations

Le tableau de bord de l'utilisation de l'API inclut toutes les requêtes d'API REST que Braze a reçues et pour lesquelles la solution a renvoyé une réponse `2XX`, `4XX` ou `5XX`. Cela comprend les sorties de transformation des données et les synchronisations d'ingestion de données dans le cloud. Les étapes relatives au trafic de SDK et à la mise à jour des utilisateurs ne sont pas incluses dans ce tableau de bord.

Les données affichées dans le tableau de bord peuvent présenter un retard de 15 minutes dans l'affichage du trafic récent. Pendant les périodes de forte utilisation, vous pouvez actualiser le tableau de bord jusqu'à 4 fois par minute. Il se peut que vous deviez attendre quelques minutes avant d'actualiser à nouveau le tableau de bord.
