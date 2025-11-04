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

Pour accéder à la page de **facturation**, allez dans **Réglages** > **Facturation**.

La page **Facturation** comprend les onglets suivants :

- [Abonnements et utilisation](#subscriptions-and-usage)
- [Événements et attributs les plus utilisés par application](#most-used-events-and-attributes-by-app)
- [Utilisation totale des points de données](#total-data-points-dashboard)

## Abonnements et utilisation

L'onglet **Abonnements et utilisation** comprend des graphiques d'utilisation et les détails de votre contrat.

### Graphiques d'utilisation

Vous y trouverez des graphiques d'utilisation qui s'appliquent à vos espaces de travail. Il se peut que votre propre tableau de bord affiche des indicateurs d'utilisation différents en fonction des produits que vous avez achetés. 

[Graphique d'utilisation montrant les visiteurs uniques mensuels]({% image_buster /assets/img/subscription_and_billing4.png %}){: style="max-width:90%;"}

Ces graphiques peuvent indiquer le nombre d'utilisateurs actifs par mois, le nombre de visiteurs uniques par mois et le nombre d'envois d'e-mails. Les graphiques d'utilisation de ce type sont particulièrement utiles lorsqu'il s'agit de budgétiser l'utilisation et de mieux comprendre la contribution des espaces de travail à l'utilisation globale.

### Détails du contrat

Les détails du contrat indiquent les dates de début et de fin de votre contrat actuel avec Braze.

## Événements et attributs les plus utilisés par application

Sous **Événements et attributs les plus utilisés par application**, vous pouvez vérifier les pilotes de l'utilisation de vos points de données d'attributs et d'événements personnalisés. 

\![Événements et attributs les plus utilisés par application]({% image_buster /assets/img/most_used_events_attributes_time.png %})

Pour chaque application, vous pouvez sélectionner **Voir la répartition** pour afficher une estimation du nombre d'attributs personnalisés, d'attributs de profil et d'événements personnalisés pour la période sélectionnée, ainsi que le pourcentage de mises à jour d'attributs et d'événements de cette application qui ont été générées par cet attribut ou cet événement. 

!onglet des événements et attributs les plus utilisés par application]({% image_buster /assets/img/most_used_events_attributes_2.png %}){: style="max-width:60%"}

Les ventilations de données de ce type peuvent vous aider à comprendre quels sont les points de données spécifiques qui occupent une grande partie de votre espace de travail. Nous vous recommandons de contrôler ces informations de temps en temps pour vous assurer que vous ne dépensez pas des points de données de manière accidentelle et inutile. Votre gestionnaire satisfaction client peut vous conseiller pour tirer le meilleur parti de votre plan actuel ou vous proposer des options pour une plus grande flexibilité. 

## Total des points de données du tableau de bord

L'onglet **Utilisation totale des points de données** donne un aperçu approfondi de l'utilisation de vos points de données. Vous pouvez visualiser toutes les données de cette section agrégées par semaine ou par mois.

!Filtrage de l'utilisation des points de données par semaine]({% image_buster /assets/img/subscription_and_billing2.png %})

### Détails du contrat

Vous y trouverez des informations sur la date de début et de fin de votre contrat Braze en cours, ainsi que les points de données alloués et la somme de tous les points de données utilisés jusqu'à présent dans le cadre de votre contrat actuel.

Les champs de cette section sont définis comme suit :

- **Type de contrat :** Structure de la période de facturation, annuelle ou pluriannuelle.
- **Date de début et de fin du contrat :** Date de début et de fin de l'ensemble du contrat.
- **Points de données attribués :** La quantité de points de données alloués dans le contrat par période de facturation.
- **Utilisation des points de données du contrat :** Total cumulé de tous les points de données enregistrés pendant la durée du contrat, qui n'est pas réinitialisé lors de la prochaine période de facturation.

!section Détails du contrat de l'onglet Utilisation totale des points de données]({% image_buster /assets/img/contract_details.png %})

### Données de facturation de l'entreprise

#### Utilisation totale de points de données au niveau de l'application

Ce graphique montre l'utilisation de vos points de données dans les différentes applications.

L'utilisation totale des points de données au niveau de l'application indique les points de données utilisés pour chaque application.]({% image_buster /assets/img/app_level_total.png %})

Sélectionnez l'un des totaux pour afficher le tableau **Utilisation des points de données au fil du temps**, qui présente vos totaux de points de données hebdomadaires pour chaque espace de travail.  Les lignes dont la colonne **Nom de l'application** est vide représentent des points de données qui ne sont associés à aucune application (tels que les points de données utilisés dans les demandes qui ne spécifient pas de `app_id`).

L'utilisation des points de données au fil du temps montre le nombre total de points de données hebdomadaires pour deux espaces de travail.]({% image_buster /assets/img/data_point_usage_time.png %})

#### Utilisation des points de données de l'espace de travail

Ce graphique vous permet d'évaluer l'utilisation totale des points de données d'une entreprise par espace de travail. Ce graphique vous permet d'évaluer la contribution de chaque espace de travail à l'utilisation des points données de l'entreprise.

!Graphique de l'utilisation des points de données de l'espace de travail pour deux espaces de travail]({% image_buster /assets/img/appgroup_datapoint_usage.png %}){: style="max-width:90%;"}

#### Utilisation des points de données du cycle de facturation par source d'événement

Ce graphique vous permet de voir comment l'utilisation des points de données est répartie entre les différentes sources d'événements, telles que les différents attributs API, les événements personnalisés et les sessions.

!Utilisation des points de données du cycle de facturation par source d'événement affichant la répartition des points de données entre les différentes sources d'événements.]({% image_buster /assets/img/event_source_stats.png %})

#### Utilisation des points de données dans le temps

Ce graphique vous permet de voir rapidement votre utilisation totale de points de données par rapport à la quantité de points de données qui vous est allouée.

Utilisation des points de données dans le temps, avec comparaison entre les points de données alloués pour le cycle de facturation en cours et le total en cours.]({% image_buster /assets/img/company_data_point_usage_time.png %}){: style="max-width:90%;"}

