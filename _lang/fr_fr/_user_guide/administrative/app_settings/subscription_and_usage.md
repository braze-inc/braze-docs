---
nav_title: Facturation
article_title: Facturation
alias: /subscription_and_usage/
page_order: 25
page_type: reference
description: "Cet article de référence couvre la page Facturation, où vous pouvez surveiller et vérifier votre consommation de données."
tool: Dashboard
search_rank: 5
---

# Facturation

> Découvrez comment utiliser la page **Facturation** pour surveiller et vérifier votre consommation de données dans les espaces de travail, les apps et les sources d'événements. Cet article présente les différentes sections de la page et les informations qu'elles peuvent vous fournir.

Pour accéder à la page de **facturation**, allez dans **Réglages** > **Facturation.**

La page **Facturation** comprend les onglets suivants :

- [Abonnement et utilisation](#subscriptions-and-usage)
- [Événements et attributs les plus utilisés par application](#most-used-events-and-attributes-by-app)
- [Utilisation totale des points de données](#total-data-points-dashboard)

## Abonnement et utilisation

L'onglet **Abonnements et utilisation** comprend des graphiques d'utilisation et les détails de votre contrat.

### Graphiques d’utilisation

Vous y trouverez des graphiques d'utilisation qui s'appliquent à vos espaces de travail. Vous pouvez trouver votre propre tableau de bord pour afficher les différents indicateurs d’utilisation en fonction des produits que vous avez achetés. 

![Graphique d'utilisation montrant les visiteurs uniques mensuels]({% image_buster /assets/img/subscription_and_billing4.png %}){: style="max-width:90%;"}

Ces graphiques peuvent indiquer le nombre d'utilisateurs actifs par mois, le nombre de visiteurs uniques par mois et le nombre d'envois d'e-mails. Les graphiques d'utilisation de ce type sont particulièrement utiles lorsqu'il s'agit de budgétiser l'utilisation et de mieux comprendre la contribution des espaces de travail à l'utilisation globale.

### Détails du contrat

Les détails du contrat indiquent la date de début et de fin de votre contrat actuel avec Braze.

## Événements et attributs les plus utilisés par application

Sous **Événements et attributs les plus utilisés par application**, vous pouvez vérifier les pilotes de votre consommation de points de données d'attributs et d'événements personnalisés. 

![Événements et attributs les plus utilisés par l'application]({% image_buster /assets/img/most_used_events_attributes_time.png %})

Pour chaque application, vous pouvez sélectionner **Voir la répartition** pour afficher une estimation du nombre d'attributs personnalisés, d'attributs de profil et d'événements personnalisés pour la période sélectionnée, ainsi que le pourcentage de mises à jour d'attributs et d'événements de cette application qui ont été générées par cet attribut ou cet événement. 

![Événements et attributs les plus utilisés par onglet de répartition des applications]({% image_buster /assets/img/most_used_events_attributes_2.png %}){: style="max-width:60%"}

Les répartitions de données telles que celles-ci peuvent vous aider à comprendre quels points de données spécifiques prennent des pourcentages importants de votre attribution. Nous vous recommandons de surveiller ces informations de temps à autre afin de vous assurer de ne pas dépenser de points de données de manière accidentelle et inutile. Votre gestionnaire du succès des clients peut fournir des conseils pour tirer le meilleur parti de votre plan actuel ou fournir des options pour une plus grande flexibilité. 

## Tableau de bord total des points de données

L'onglet **Utilisation totale des points de données** offre un aperçu approfondi de votre consommation de points de données. Vous pouvez afficher toutes les données de cette section regroupées par semaines ou par mois.

![Filtrage de l'utilisation des points de données par semaine]({% image_buster /assets/img/subscription_and_billing2.png %})

### Détails du contrat

Ici, vous trouverez des informations sur le moment où votre contrat Braze actuel commence et se termine, ainsi que des points de données alloués et une somme de tous les points de données utilisés jusqu’à présent dans votre contrat actuel.

Les champs de cette section sont définis comme suit :

- **Type de contrat :** Structure de la période de facturation, annuelle ou pluriannuelle.
- **Date de début et de fin du contrat :** Date de début et de fin de l’intégralité du contrat.
- **Points de données alloués :** La quantité de points de données alloués dans le contrat par terme de facturation.
- **Utilisation des points de données du contrat :** Un total cumulé de tous les points de données consommés sur la durée de vie du contrat, et ne se réinitialise pas dans la prochaine période de facturation.

![Section "Détails du contrat" de l'onglet "Utilisation totale des points de données"]({% image_buster /assets/img/contract_details.png %})

### Données de facturation de la société

#### Utilisation totale de points de données au niveau de l'application

Ce graphique montre l'utilisation de vos points de données dans les différentes applications.

![App Level Total Data Point Usage indique les points de données utilisés pour chaque application.]({% image_buster /assets/img/app_level_total.png %})

Sélectionnez l'un des totaux pour afficher le tableau **Utilisation des points de données au fil du temps**, qui présente vos totaux de points de données hebdomadaires pour chaque espace de travail.  Les lignes dont la colonne **Nom de l'application** est vide représentent des points de données qui ne sont associés à aucune application (tels que les points de données utilisés dans les demandes qui ne spécifient pas de `app_id`).

![L'utilisation des points de données au fil du temps montre le nombre total de points de données hebdomadaires pour deux espaces de travail.]({% image_buster /assets/img/data_point_usage_time.png %})

#### Utilisation des points de données de l'espace de travail

Ce graphique vous permet d'évaluer l'utilisation totale des points de données d'une entreprise par espace de travail. Ce graphique vous permet d'évaluer la contribution de chaque espace de travail à l'utilisation des points données de l'entreprise.

![Graphique d'utilisation des points de données de l'espace de travail pour deux espaces de travail]({% image_buster /assets/img/appgroup_datapoint_usage.png %}){: style="max-width:90%;"}

#### Utilisation des points de données du cycle de facturation par source d'événement

Ce graphique vous permet de voir comment l'utilisation des points de données est répartie entre différentes sources d'événements, telles que différents attributs API, événements personnalisés et sessions.

![Utilisation des points de données du cycle de facturation par source d'événement : affichage de la répartition des points de données entre les différentes sources d'événement.]({% image_buster /assets/img/event_source_stats.png %})

#### Utilisation du point de données au fil du temps

Ce graphique vous permet d’afficher rapidement votre utilisation de points de données totaux par rapport à la quantité de points de données allouée.

![Utilisation des points de données dans le temps, en comparant les points de données alloués pour le cycle de facturation en cours avec le total en cours]({% image_buster /assets/img/company_data_point_usage_time.png %}){: style="max-width:90%;"}

