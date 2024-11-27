---
nav_title: "Événements d'exception" 
article_title: "Événements d'exception"
page_order: 4
page_type: reference
description: "Cet article de référence décrit des événements d’exception et la façon dont ils impactent vos composants Canvas."
tool: Canvas

---

# Événements d’exception Canvas

{% alert important %}
Depuis le 28 février 2023, vous ne pouvez plus créer ou dupliquer de Canvas à l’aide de l’éditeur Canvas d’origine. Cet article est disponible pour référence lors de la configuration d’événements d’exception pour le flux de travail Canvas d’origine. <br><br> Braze recommande aux clients qui utilisent l’expérience Canvas d’origine de passer à Canvas Flow. Il s’agit d’une expérience d’édition améliorée permettant de mieux créer et gérer les Canvas. En savoir plus sur le [clonage de vos toiles dans Canvas Flow.]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/)
{% endalert %}

> Lorsque vous planifiez un composant pour un Canvas en utilisant l’éditeur Canvas d’origine, vous pouvez configurer un événement d’exception. Vous pouvez ajouter un événement d’exception à un composant tant que l’audience n’accède pas immédiatement au composant suivant. Les utilisateurs qui effectuent l’événement d’exception [ne passeront pas à l’étape][2] et seront exclus de votre audience Canvas.

Les événements d’exception seront uniquement déclenchés alors qu’un utilisateur attend de recevoir le composant Canvas associé. Si un utilisateur effectue la même action sur une étape de Canvas précédente, l’événement d’exception ne sera pas déclenché.

{% alert important %}
Pour Canvas Flow, les événements d'exception ne sont configurés qu'à l'aide des [chemins d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/). Vous pouvez par exemple définir un parcours d’action et utiliser le parcours « Tous les autres » en tant qu’exception.
{% endalert %}

Les événements d’exception pour une étape basée sur une action fonctionneront au cours du retard ou de la fenêtre d’étape. Les étapes planifiées n’ont pas de fenêtre et l’événement d’exception fonctionnera alors uniquement s’il survient au cours du retard.

Par exemple, si vous avez un événement d’exception pour « Panier abandonné » sur la troisième étape de votre Canvas et qu’un utilisateur renonce à son panier à la deuxième étape, l’événement d’exception ne sera pas déclenché. Dans cet exemple, l’événement d’exception sera uniquement déclenché si l’utilisateur renonce à son panier à la troisième étape de votre Canvas. 

![][1]


[1]:{% image_buster /assets/img_archive/Canvas_Exception_Events.png %}
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/
