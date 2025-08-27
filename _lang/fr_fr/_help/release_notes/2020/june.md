---
nav_title: juin
page_order: 7
noindex: true
page_type: update
description: "Cet article contient les notes de version de juin 2020."
---
# Juin 2020

## Rapports de rétention

Les rapports de rétention offrent désormais une plage de rétention pour les [campagnes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/) et les [toiles.]({{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/) La rétention par plage mesure le nombre d’utilisateurs qui reviennent et effectuent un événement de rétention sélectionné pendant une période spécifique. 

## Mises à jour de l’API pour le suivi des utilisateurs

L'[endpoint`users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) dispose désormais d'un taux par défaut de 50 000 demandes d'API par minute pour les sociétés de tableaux de bord créées après le 2 juin 2020. Les entreprises existantes créées avant cette date et leurs espaces de travail seront toujours autorisés à effectuer un nombre illimité de requêtes API vers l'endpoint `users/track`.

Braze impose cette valeur par défaut sur notre endpoint orienté client le plus utilisé dans le cadre de nos objectifs de stabilité et de fiabilité pour notre API et notre infrastructure. La limite imposée est très libérale et affectera très peu de sociétés de tableaux de bord et leurs opérations régulières. Si vous avez besoin d’augmenter cette limite, contactez votre gestionnaire du succès des clients ou notre équipe d’assistance pour leur demander.

