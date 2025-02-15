---
nav_title: Exporter des segments volumineux
article_title: Exporter des segments volumineux
page_order: 4

page_type: solution
description: "Cet article d’aide vous guide à travers plusieurs méthodes d’exportation de segments d’utilisateurs volumineux."
tool: Segments
---

# Exporter des segments volumineux

Il existe plusieurs méthodes pour exporter un segment d’utilisateurs volumineux. Pour les segments contenant plus de 500 000 utilisateurs, vous pouvez décomposer ce segment plus large en segments plus petits pour capturer ces utilisateurs et exporter chacun des segments plus petits à partir du tableau de bord de Braze. 

Vous pouvez également envisager d'utiliser des [numéros de compartiment aléatoire]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute) pour diviser votre base d'utilisateurs en plusieurs segments, puis les combiner après l'exportation. Par exemple, si vous voulez diviser votre segment en deux, vous pouvez le faire avec les filtres suivants :
- Segment 1 : Le numéro de compartiment aléatoire est inférieur à 5 000 (inclut 0-4999)
- Segment 2 : Le numéro de compartiment aléatoire est supérieur à 4999 (inclut 5000-9999)

Vous pouvez également tirer parti des endpoints suivants pour exporter les données utilisateur d’un segment spécifique. Notez que ces endpoints sont soumis à des limites de données.
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 24 octobre 2022_
