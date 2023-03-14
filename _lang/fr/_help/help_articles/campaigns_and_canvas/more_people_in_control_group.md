---
nav_title: Gérer un gros groupe de contrôle
article_title: Gérer un gros groupe de contrôle
page_order: 2

page_type: solution
description: "Cet article d’aide décrit la raison pour laquelle votre groupe de contrôle peut être plus gros que prévu et vous guide à travers les étapes pour résoudre cela."
tool: Canvas
---

# Gérer un gros groupe de contrôle 

En créant votre Canvas, vous vous attendiez peut-être à ce que votre public soit réparti uniformément entre votre groupe de contrôle et votre groupe de variantes, comme dans l’[exemple](#example) suivant. Nous pouvons expliquer pourquoi et comment le résoudre !

Le groupe que rejoint un utilisateur dépend de ses paramètres. Il peut s’agir du groupe de contrôle ou du groupe de variantes. Un utilisateur va entrer dans un Canvas lorsqu’il correspond à tous les critères que vous avez définis dans [Entry Step][1]. Lors de la configuration de votre Canvas, vous définissez quel pourcentage d’utilisateurs entreront dans chaque variante et dans le groupe de contrôle.

Si la taille de votre groupe de contrôle est importante par rapport à votre groupe de variantes (et que ce n’était pas votre intention), nous vous recommandons ce qui suit :
1. Définissez votre filtre d’audience sur « Is Push Enabled » (Push activé).
2. Définissez votre filtre d’audience sur « is Opted In or Subscribed » (A consenti ou S’est abonné).

Lors de la création d’un Canvas avec un groupe de contrôle, assurez-vous que tous les utilisateurs du public entrant peuvent recevoir des messages dans le Canvas (c.-à-d. que le Canvas contient des notifications push et des e-mails).

## Exemple

Imaginons le scénario suivant :
- Un Canvas a une seule variante et un groupe de contrôle.
- La première étape de la variante est une notification push.
- 90 % des utilisateurs ont été sélectionnés pour entrer dans la variante et 10 % pour entrer dans le groupe de contrôle.

![Exemple de Canvas][41]

Dans ce scénario, 90 % des utilisateurs qui entrent dans Canvas entreront dans la variante. 

Si nous regardons les utilisateurs actifs, nous pouvons voir que, bien qu’ils soient 39 800, seuls 73 % d’entre eux sont activés pour les notifications push :

![Public entrant][42]

Cela signifie que même si nous avons indiqué que 90 % des utilisateurs doivent entrer dans la variante, tous ces utilisateurs ne peuvent pas recevoir une notification push. Ces utilisateurs qui ne sont pas en mesure de recevoir une notification push entreront quand même dans la variante.

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 3 décembre 2020_

[1]: {{site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2-use-the-entry-wizard-to-set-up-your-canvas
[41]: {% image_buster /assets/img_archive/trouble15.png %}
[42]: {% image_buster /assets/img_archive/trouble16.png %}
