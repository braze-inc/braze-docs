---
nav_title: Comprendre le statut d’une campagne
article_title: Comprendre le statut d’une campagne
page_order: 2
tool: Campaigns
page_type: reference
description: "Le présent article de référence donne un aperçu des différents statuts qu’une campagne peut avoir et ce qu’ils signifient."
---

# Comprendre le statut d’une campagne

> Le présent article de référence donne un aperçu des différents statuts qu’une campagne peut avoir et ce qu’ils signifient.

Sur votre tableau de bord de Braze, vos campagnes sont groupées par statut. Consultez les différents statuts de campagne ainsi que les descriptions de ce qu’ils signifient.

## Brouillon
Les campagnes marquées en tant que brouillons sont enregistrées mais pas lancées. Cliquez dessus pour continuer à les modifier et commencer à les envoyer.

## Active
Les campagnes actives sont en cours d’envoi. Elles peuvent suivre l’un des comportements suivants :
- Planifiée pour un seul envoi et n’a pas encore commencé à être envoyée
- Planifiée pour un seul envoi et est en train de s’envoyer (campagnes selon le fuseau horaire local et à Timing Intelligent envoyées sur 24 heures)
- Planifiée pour être envoyée selon une planification récurrente et pour laquelle au moins une occurrence n’a pas fini d’être envoyée

## Archivée
Les campagnes archivées ne sont plus envoyées et sont effacées de l’onglet **All Active (Tous actifs)** sur le tableau de bord de Braze. Ces campagnes sont également supprimées des graphiques statistiques détaillés sur les pages **Overview** et **Revenu**.

Pour [archiver une campagne][2], cliquez sur l’icône d’engrenage pour une campagne donnée ou cochez simplement la case et sélectionnez **Archive Selected** (Archiver la sélection).

## Inactive
Les campagnes inactives ont été mises en pause mais sont toujours modifiables. Vous pouvez reprendre une campagne inactive en cliquant sur l’icône d’engrenage à côté du nom de la campagne et en sélectionnant **Reprendre**.

## Tests multivariés en cours
Ce statut indique les campagnes avec des [tests multivariés][1] en cours de fonctionnement. S’ils atteignent le point où une variante dépasse la performance des autres avec une confiance supérieure à 95 %, la variante sera alors indiquée comme « gagnante »."

## Test multivarié inactif : sélection du gagnant nécessaire
Ce statut indique des campagnes avec des tests multivariés qui ont fini de fonctionner et nécessitent qu’un utilisateur du tableau de bord de Braze [déclare le gagnant][3] pour sélectionner la variante que les utilisateurs restants recevront.

## Terminée
Les campagnes terminées ont fini d’envoyer et ne sont pas planifiées pour être à nouveau envoyées à l’avenir.

[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#multivariate-testing
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/archiving_campaigns/#archiving-campaigns
[3]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-5-pick-the-action-that-determines-the-winner
