---
nav_title: Comprendre le statut de la campagne
article_title: Comprendre le statut de la campagne
page_order: 2
tool: Campagnes
page_type: Référence
description: "Cet article de référence donne un aperçu des différents statuts qu'une campagne peut avoir et de ce qu'elle signifie."
---

# Comprendre le statut de la campagne

> Cet article de référence donne un aperçu des différents statuts qu'une campagne peut avoir et de ce qu'elle signifie.

Sur votre tableau de bord Braze, vos campagnes sont regroupées par statut. Vérifiez les différents statuts et descriptions de la campagne pour ce qu'ils signifient.

## Brouillon
Les campagnes marquées comme brouillons sont sauvegardées mais non lancées. Cliquer dessus vous permet de continuer à éditer et à commencer à envoyer.

## Actif
Des campagnes actives sont en cours d'envoi. Ils peuvent tomber sous l'un des comportements suivants :
- Prévu pour envoyer une fois et n'a pas encore commencé à envoyer
- Prévu pour envoyer une fois et est en cours d'envoi (fuseau horaire local et campagnes de Timing intelligentes envoyées sur 24 heures)
- Planifié pour envoyer sur un planning récurrent et a au moins une occurrence qui n'a pas fini d'envoyer

## Archivé
Les campagnes archivées ne sont plus envoyées et sont effacées de l'onglet **Tous actifs** sur le tableau de bord de Braze. Ces campagnes sont également supprimées des graphiques de statistiques détaillés sur les pages **Aperçu** et **Revenu**.

Pour [archiver une campagne][2], cliquez sur l'icône d'engrenage à droite de la campagne, ou tout simplement cochez la case et sélectionnez **Archive Sélectionnée**.

## Inactif
Les campagnes inactives ont été suspendues mais sont encore modifiables. Vous pouvez reprendre une campagne inactive en cliquant sur l'icône d'engrenage par le nom de la campagne et en sélectionnant **Reprendre**.

## Tests multivariés en cours
Ce statut marque les campagnes avec [tests multivariés][1] encore en cours d'exécution. S'ils atteignent un point où une variante surpasse les autres avec plus de 95 % de confiance, alors la variante sera marquée comme le « gagnant ».

## Test multivarié inactif - Sélection du gagnant requise
Ce statut indique les campagnes avec des tests multivariés qui ont terminé leur exécution et exigent qu'un utilisateur du tableau de bord Braze [déclare un gagnant][3] pour sélectionner quelle variante les utilisateurs restants recevront .

## Terminé
Les campagnes terminées sont terminées et ne doivent pas être renvoyées dans le futur.


[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#multivariate-testing
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/archiving_campaigns/#archiving-campaigns
[3]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-5-pick-the-action-that-determines-the-winner
