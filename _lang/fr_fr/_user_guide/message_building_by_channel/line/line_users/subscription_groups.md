---
nav_title: "Groupes d'abonnement"
article_title: "Groupes d'abonnement"
page_order: 1
description: "Cet article traite des groupes d'abonnement aux messages LINE."
page_type: reference
channel:
 - LINE
alias: /line/subscription_groups/
---

# LINE groupes d'abonnement

> Il existe deux états d'abonnement pour les utilisateurs de LINE : abonné et désabonné. LINE peut compter jusqu'à 100 groupes d'abonnement par espace de travail, chaque groupe d'abonnement étant connecté à son propre canal LINE.

| État | Définition |
| --- | --- |
| Abonné | L'utilisateur a suivi la chaîne LINE à partir de son application LINE. Les utilisateurs sont automatiquement abonnés lorsqu'ils suivent après que vous avez effectué les étapes d'intégration. |
| Désabonné | L'utilisateur n'a pas suivi la chaîne LINE à partir de son application LINE, ou l'utilisateur a explicitement désapprouvé la chaîne LINE. <br><br> Les utilisateurs qui se désabonnent d'un groupe d'abonnement LINE ne recevront plus aucun message LINE provenant des canaux de communication appartenant au groupe d'abonnement. |
{: .reset-td-br-1 .reset-td-br-2 }

## Définition du groupe d'abonnement LINE d'un utilisateur

LINE héberge l'état de l'abonnement des utilisateurs. Braze traite les événements de suivi et de désabonnement qui mettent à jour l'état de l'abonnement.