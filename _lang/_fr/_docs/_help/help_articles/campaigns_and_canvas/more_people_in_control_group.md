---
nav_title: Manipulation d'un grand groupe de contrôle
article_title: Manipulation d'un grand groupe de contrôle
page_order: 2
page_type: Solution
description: "Cet article d'aide décrit pourquoi votre groupe de contrôle peut être plus grand que prévu, et vous guide à travers des étapes pour résoudre ce problème."
tool: Toile
---

# Gestion d'un grand groupe de contrôle

Lors de la création de votre Canvas, vous avez pu vous attendre à ce que votre public se répartisse équitablement entre votre groupe de contrôle et votre groupe de variantes, comme dans [notre exemple](#example) ci-dessous. Nous pouvons expliquer pourquoi c'est et comment le corriger !

Le groupe auquel un utilisateur adhère dépend de ses paramètres. Cela peut être soit le groupe de contrôle soit le groupe de variantes. Un utilisateur entrera dans un Canevas lorsqu'il répondra à tous vos critères définis à l'étape \[Étape d'entrée\]\[1\]. Lors de la configuration de votre Canvas, vous définissez le pourcentage d'utilisateurs qui entreront dans chaque variante et le groupe de contrôle.

Si votre groupe de contrôle est grand par rapport à votre groupe de variantes (et ce n'est pas votre intention), nous vous recommandons les éléments suivants :
1. Définissez le filtre d'audience de votre entrée à "Est Push activé".
2. Définissez le filtre d'audience de votre entrée à "est choisi ou abonné".

Lors de la création d'une toile avec un groupe de contrôle, assurez-vous que tous les utilisateurs de l'audience d'entrée sont en mesure de recevoir des messages dans la toile (i. Le Canvas contient des messages push et email).

## Exemple

Imaginons le scénario suivant :
- Une toile a une seule variante **** et un groupe de contrôle ****.
- La première étape de la variante **** est une notification push.
- 90 % des utilisateurs ont été sélectionnés pour entrer dans la **variante**et 10 % pour entrer dans le groupe de contrôle ****.

!\[Exemple de Canvas\]\[41\]

Dans ce scénario, 90 % des utilisateurs qui entrent dans le Canvas entreront dans la variante.

Si nous regardons le public d'entrée (utilisateurs actifs), nous pouvons le voir même s'il contient 39. k utilisateurs, seulement 29,1k (73%) d'entre eux sont activés par push :

!\[Public d'entrée\]\[42\]

Cela signifie que même si nous avons spécifié 90 % des utilisateurs pour entrer dans la variante, tous ces utilisateurs ne sont pas en fait **en mesure de recevoir** une notification push. Ces utilisateurs qui ne sont pas en mesure de recevoir une notification push entreront quand même dans la variante.

Vous avez encore besoin d'aide ? Ouvrez un ticket de support []({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 3 décembre 2020_
[1]: {{site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2-use-the-entry-wizard-to-set-up-votre-canvas [41]: {% image_buster /assets/img_archive/trouble15.png %} [42]: {% image_buster /assets/img_archive/trouble16.png %}
