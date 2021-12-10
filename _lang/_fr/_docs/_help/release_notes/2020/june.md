---
nav_title: Juin
page_order: 7
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour Juin 2020."
---

# Juin 2020

## Rapports de rétention

Les rapports de fidélisation offrent maintenant des intervalles de conservation - Intervalle de conservation mesure le nombre d'utilisateurs qui reviennent et effectuent un événement de rétention sélectionné pendant des intervalles de temps spécifiques. Pour en savoir plus sur la portée des rapports de rétention et de rétention, visitez la documentation de [Canvas][1] et de [Campagne][2].

## Mise à jour de l'API de suivi utilisateur

Le point de terminaison [utilisateurs/piste][3] a maintenant un taux par défaut de 50 000 requêtes API par minute pour les entreprises du tableau de bord créées après le 2 juin 2020. Les entreprises existantes créées avant cette date et leurs groupes d'applications seront toujours autorisées à recevoir des requêtes API illimitées vers le point de terminaison utilisateur/piste.

Braze impose cette valeur par défaut à notre point de terminaison client le plus utilisé comme une étape vers nos objectifs de stabilité et de fiabilité pour notre API et notre infrastructure. La limite imposée est très libérale et affectera très peu de sociétés du tableau de bord et leurs opérations régulières. Dans le cas où vous auriez besoin d'une augmentation à cette limite, veuillez contacter votre Responsable du Service Clientèle ou notre équipe de support pour demander une augmentation.

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/
[3]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
