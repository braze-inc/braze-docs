---
nav_title: Campagne ou Canvas non déclenchée
article_title: Campagne ou Canvas non déclenchée
page_order: 5
page_type: Solution
description: "Cet article d'aide vous guide à travers les étapes pour résoudre les problèmes liés aux campagnes ou aux Canvases qui ne se déclenchent pas comme prévu."
tool:
  - Campagnes
  - Toile
---

# Campagne ou Canvas non déclenchée

Il y a un certain nombre de raisons pour lesquelles vous n'avez pas eu le comportement de déclenchement attendu. La solution pour l'erreur la plus courante est de s'assurer que la campagne que vous déclenchez n'utilise pas le même événement déclencheur dans le segment.

## Déclencheurs de la campagne

Rappelez-vous que si l'utilisateur ne tombe pas dans le segment en premier, il ne recevra pas la campagne même s'il effectue la gâchette.

Si votre campagne se déclenche sur un événement personnalisé, vous voudrez vous assurer que cet événement n'est pas pré-filtré par un segment que vous voulez entrer dans la campagne.

Par exemple, si le segment inclut la session de début d'événement « A utilisé l'application plus d'une fois» et l'événement dont la campagne se déclenche est Session Start, l'utilisateur recevra le message. Ce ne sera pas nécessairement pour la première session. Ceci est dû au fait que la première étape lors de la vérification de savoir si un utilisateur doit recevoir une campagne est de passer en revue le public cible du segment.

En bref, évitez de configurer une campagne basée sur l'action ou Canvas avec le même déclencheur que le filtre d'audience (i. ., un attribut modifié ou effectué un événement personnalisé). Une condition de course peut se produire dans laquelle l'utilisateur n'est pas dans le public au moment où il effectue l'événement de déclenchement ce qui signifie qu'ils ne recevront pas la campagne ou n'entreront pas dans le Canvas.

Vous avez encore besoin d'aide ? Ouvrez un ticket de support []({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 5 août 2021_