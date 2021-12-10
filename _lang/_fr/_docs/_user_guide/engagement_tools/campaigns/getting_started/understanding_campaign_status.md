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

Sur votre tableau de bord Braze, vos campagnes sont regroupées par statut. Voici les différents statuts que vos campagnes pourraient avoir et les descriptions de ce qu'elles signifient :

- __Brouillon__
    - Campagnes sauvegardées mais non lancées. Cliquer dessus vous permet de continuer à éditer et à commencer à envoyer.


- __Actif__
    - Les campagnes qui sont en cours d'envoi et qui sont soumises à l'un des comportements suivants :
        - Prévu pour envoyer une fois et n'a pas encore commencé à envoyer
        - Prévu pour envoyer une fois et est en cours d'envoi (fuseau horaire local et campagnes de Timing intelligentes envoyées sur 24 heures)
        - Planifié pour envoyer sur un planning récurrent et a au moins une occurrence qui n'a pas fini d'envoyer


- __Archivé__
    - Campagnes qui ne sont plus envoyées et qui sont effacées de l'onglet "Toutes Actives" sur le Tableau de bord, ainsi que les graphiques des statistiques détaillées sur les pages **Aperçu** et **Revenu**.
    - Pour [archiver des campagnes][2] cliquez sur l'icône d'engrenage à droite de la campagne, ou tout simplement cochez la case et sélectionnez **Archive Sélectionnée**.
    - Vous ne pouvez pas modifier une campagne archivée, et vous devez donc la désarchiver pour le faire.


- __Inactif__
    - Les campagnes qui ont été mises en pause mais sont toujours rendues éditables. Vous pouvez reprendre une campagne inactive en cliquant sur l'icône d'engrenage par le nom de la campagne et en sélectionnant **Reprendre**.


- __Tests multivariés en cours__
    - Campagnes avec [tests multivariés][1] encore en cours d'exécution. Si elles atteignent un point où une variante surpasse les autres avec plus de 95 % de confiance, la variante sera marquée comme le « gagnant ».


- __Test multivarié inactif - Sélection du gagnant requise__
    - Campagnes avec des tests multivariés qui ont terminé leur exécution et ont besoin d'un utilisateur du tableau de bord pour déclarer un gagnant pour informer la variante que les utilisateurs restants recevront .


- __Terminé__
    - Les campagnes qui ont fini d'envoyer et qui ne sont pas planifiées pour envoyer à nouveau à l'avenir.



[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#multivariate-testing
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/archiving_campaigns/#archiving-campaigns
