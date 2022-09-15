---
nav_title: Événements d’exception 
article_title: Événements d’exception
page_order: 4
page_type: reference
description: "Cet article de référence décrit des événements d’exception et la façon dont ils impactent vos étapes Canvas."
tool: Canvas

---

# Événements d’exception Canvas

Lorsque vous définissez une étape pour un Canvas, vous pouvez configurer un événement d’exception. Vous pouvez ajouter un événement d’exception à une étape tant que le public n’accède pas immédiatement à l’étape suivante. Les utilisateurs qui effectuent l’événement d’exception ne [passeront pas à l’étape suivante][2] et seront exclus de votre public Canvas.

Les événements d’exception seront uniquement déclenchés alors qu’un utilisateur attend de recevoir la Canvas Step associée. Si un utilisateur effectue la même action sur une Canvas Step précédente, l’événement d’exception ne sera pas déclenché.

Les événements d’exception pour une étape basée sur une action fonctionneront au cours du retard ou de la fenêtre d’étape. Les étapes planifiées n’ont pas de fenêtre et l’événement d’exception fonctionnera alors uniquement s’il survient au cours du retard.

Par exemple, si vous avez un événement d’exception pour « Panier abandonné » sur la troisième étape de votre Canvas et qu’un utilisateur renonce à son panier à la deuxième étape, l’événement d’exception ne sera pas déclenché. Dans cet exemple, l’événement d’exception sera uniquement déclenché si l’utilisateur renonce à son panier à la troisième étape de votre Canvas. 

![][1]


[1]:{% image_buster /assets/img_archive/Canvas_Exception_Events.png %}
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/
