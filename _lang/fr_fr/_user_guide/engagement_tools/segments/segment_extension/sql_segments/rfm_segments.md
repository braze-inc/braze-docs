---
nav_title: "Segmentations RFM"
article_title: Segments RFM SQL
page_order: 1
page_type: reference
alias: "/rfm_segments/"
description: "Cet article explique comment créer des extensions de segments RFM, qui identifient vos meilleurs utilisateurs en mesurant leurs habitudes d'achat."
tool: Segments
---

# Segments RFM SQL

> Vous pouvez créer une extension segmentation RFM (récence, fréquence, monétaire) pour cibler vos meilleurs utilisateurs en mesurant leurs habitudes d'achat.

L'analyse RFM est une technique marketing qui permet d'identifier vos meilleurs utilisateurs en les notant sur une échelle de 0 à 3 pour chaque catégorie (récurrence, fréquence, monétaire), 3 étant le meilleur score et 0 le plus mauvais. La récence, la fréquence et les valeurs monétaires sont toutes basées sur les données d'une période spécifique de votre choix.

## Catégories de RFM

| Catégorie | Définition |
| --- | --- |
| Caractère récent | La date à laquelle un client a effectué un achat. Un score plus élevé signifie des achats plus récents. |
| Fréquence | Fréquence d'achat d'un client. Un score plus élevé signifie une fréquence plus élevée. |
| Valeur monétaire | Montant total dépensé par un client. Un score plus élevé signifie des dépenses plus importantes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
Les événements d'achat doivent être activés pour utiliser les segments RFM SQL car la valeur monétaire de vos utilisateurs est déterminée par les chiffres d'affaires qu'ils ont générés grâce aux événements d'achat de Braze.
{% endalert %}

## Création d'une segmentation de l'appel d'offres

1. Sélectionnez **Audience** > **Extensions de segments**.
2. Sélectionnez **Nouvelle extension**, puis sélectionnez **Segment de récence, de fréquence et de valeur monétaire (RFM)**.

![Fenêtre modale offrant la possibilité de créer un segment de catalogue pour les événements, les achats ou les segments RFM.]({% image_buster /assets/img/segment/select_rfm_segment.png %}){: style="max-width:80%" }

{: start="3"}
3\. Dans le panneau **Variables**, sélectionnez votre **intervalle de temps** pour spécifier la période des données d'achat à analyser. Vous pouvez spécifier jusqu'aux 60 derniers jours. L'intervalle de temps que vous sélectionnez est l'intervalle de temps à partir duquel les données comportementales des utilisateurs sont extraites et dépend des objectifs de votre campagne.

| Champ de l'intervalle de temps | Description | Cas d’utilisation |
| --- | --- | --- |
| Relative | Précisez l'activité au cours des X derniers jours | Analysez le comportement le plus récent des utilisateurs à l'aide d'une fenêtre mobile. | 
| Date de début | Spécifiez un point de départ fixe pour votre analyse | Analysez l'activité des utilisateurs à partir d'une date précise, par exemple après le lancement d'une campagne. |
| Date de fin | Spécifiez un point final fixe pour votre analyse | Analysez l'activité des utilisateurs jusqu'à une date précise, par exemple avant une mise à jour du produit. |
| Plage de dates | Spécifiez une date de début et une date de fin pour une période personnalisée. | Analysez le comportement des utilisateurs pendant une période définie, par exemple lors d'un événement promotionnel. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{: start="4"}
4\. Sélectionnez les [groupes d'appels d'offres](#rfm-groups) générés à inclure dans votre segmentation. Si vous sélectionnez plusieurs groupes, votre segmentation inclut les utilisateurs qui font partie de l'un des groupes sélectionnés.

![Panneau des variables avec les groupes RFM "Champions" et "Utilisateurs fidèles" sélectionnés.]({% image_buster /assets/img/segment/rfm_groups.png %})

{: start="5"}
5\. Lancez une prévisualisation et enregistrez votre segment.

{% alert note %}
Vous n'avez pas besoin de modifier le code SQL dans le modèle pour créer un segment RFM. Vous pouvez utiliser exclusivement le panneau des **variables** pour personnaliser votre segmentation.
{% endalert %}

### Groupes RFM

Les segments de l'appel d'offres sont évalués dans un ordre spécifique. Les utilisateurs sont affectés au premier segment dont ils remplissent les critères, en partant du haut de la liste des priorités vers le bas. Par exemple, un utilisateur qui remplit à la fois les conditions requises pour les "Champions" et les "Utilisateurs fidèles" est affecté au segment des "Champions" parce qu'il a une priorité plus élevée.

| Groupe RFM          | Description du segment                                                                 | Rang de récence (R) | Rang de fréquence (F) | Rang monétaire (M) |
|--------------------|-------------------------------------------------------------------------------------|------------------|--------------------|-------------------|
| Champions          | Le segment d'utilisateurs le plus précieux avec les meilleurs scores dans toutes les catégories.                   | 3                | 2-3                | 2-3               |
| Utilisateurs fidèles        | Utilisateurs dont la récence et la fréquence sont élevées. Leur valeur monétaire peut être inférieure à celle des champions. | 2-3              | 2-3                | 1-3               |
| Loyalistes potentiels| Utilisateurs ayant acheté récemment avec une fréquence modérée et une valeur monétaire modérée.   | 3                | 1-3                | 1-3               |
| Prometteur          | Les utilisateurs qui ont effectué un premier achat récent et de grande valeur, mais qui n'ont pas encore établi une fréquence d'achat élevée. | 3                | 0-3                | 1-3               |
| Nouveau client       | Utilisateurs ayant effectué leur premier achat très récemment.                             | 3                | 0-3                | 0-3               |
| Besoin d'attention  | Utilisateurs dont la récence est supérieure à la moyenne, mais dont la fréquence d'achat ou la valeur monétaire sont inférieures à la moyenne. | 2-3              | 0-3                | 0-3               |
| Ne pas les perdre   | Utilisateurs qui avaient auparavant une valeur élevée avec de bons scores de fréquence et monétaires, mais qui n'ont pas acheté depuis longtemps. | 0-1              | 2-3                | 2-3               |
| En danger            | Les utilisateurs qui ont historiquement eu des scores de fréquence et monétaires modérés, mais qui n'ont pas acheté depuis longtemps. | 0-1              | 1-3                | 1-3               |
| Sur le point de dormir     | Les utilisateurs qui ont des scores faibles pour tous les indicateurs.                                       | 1                | 0-3                | 0-3               |
| Hibernation        | Utilisateurs dont la fréquence est modérée mais qui ont été inactifs pendant une période prolongée.    | 0                | 0-2                | 0-3               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
