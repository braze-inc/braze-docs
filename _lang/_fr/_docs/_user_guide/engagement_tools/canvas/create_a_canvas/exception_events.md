---
nav_title: Événements d'exception
article_title: Événements d'exception
page_order: 4
page_type: Référence
description: "Cet article de référence décrit les événements d'exception et leur impact sur les étapes de votre Canvas ."
tool: Toile
---

# Événements d'exception sur Canvas

Lorsque vous planifiez une étape pour un [Canvas][2], vous avez la possibilité de configurer un événement d’exception tout en planifiant votre canevas. Vous pouvez ajouter un événement d’exception à une étape tant que le public n’est pas immédiatement avancé. Les utilisateurs qui effectuent l'événement d'exception ne seront pas [avancés à l'étape][3] et seront exclus de votre public de Canvas .

!\[Canvas Exception Events\]\[1\]

Les événements d'exception ne se déclencheront que lorsqu'un utilisateur attend de recevoir l'étape Canvas à laquelle il est associé. Si un utilisateur effectue la même action sur une étape Canvas précédente, l'événement d'exception ne se déclenchera pas.

Les événements d'exception pour une étape basée sur l'action fonctionneront pendant le délai d'étape ou la fenêtre. Les étapes planifiées n'ont pas de fenêtre, et par conséquent, l'événement d'exception ne fonctionnera que si cela se produit pendant le délai.

Par exemple, si vous avez un événement d'exception pour le « Panier abandonné » à la troisième étape de votre toile, mais un utilisateur abandonne son panier pendant qu'il est à la deuxième étape, l'événement d'exception ne se déclenchera pas. Dans cet exemple, l’événement d’exception ne se déclenchera que si l’utilisateur abandonne son panier pendant la troisième étape de votre Canvas.
[1]:{% image_buster /assets/img_archive/Canvas_Exception_Events.png %}

[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/
[3]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/
