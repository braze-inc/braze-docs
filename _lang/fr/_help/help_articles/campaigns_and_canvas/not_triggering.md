---
nav_title: Campagne ou Canvas non déclenché
article_title: Campagne ou Canvas non déclenché
page_order: 5

page_type: solution
description: "Cet article d’aide décrit les étapes pour résoudre les problèmes liés aux campagnes ou aux canvas qui ne se déclenchent pas comme prévu."
tool: 
- Campagnes
- Canvas
---

# Campagne ou Canvas non déclenché

Plusieurs raisons peuvent expliquer pourquoi un comportement de déclenchement attendu ne s’est pas produit. La solution pour l’erreur la plus courante est de s’assurer que la campagne que vous déclenchez n’utilise pas le même événement déclencheur dans le segment.

## Déclencheurs de campagne

Rappelez-vous que si l’utilisateur n’entre pas d’abord dans le segment, il ne recevra pas la campagne même s’il exécute le déclencheur.

Si votre campagne déclenche un événement personnalisé, vous devez vous assurer que cet événement n’est pas préfiltré par un segment que vous souhaitez faire entrer dans la campagne. 

Par exemple, si le segment inclut l’événement [`SessionStart`][1] « Has Used App more than once » (A déjà utilisé l’application plus d’une fois) et l’événement déclencheur de la campagne est `SessionStart`, l’utilisateur recevra le message. Ce ne sera pas nécessairement à la première session parce que la première étape examine le public cible du segment pour voir si un utilisateur doit recevoir une campagne. 

En bref, évitez de configurer une campagne ou un Canvas basé sur une action avec le même déclencheur que le filtre d’audience (c.-à-d. une modification d’attribut ou un événement personnalisé). Une [condition de concurrence] peut se produire lorsque l’utilisateur ne figure pas dans l’audience au moment de l’événement déclencheur, ce qui signifie qu’il ne recevra pas la campagne ou ne pourra pas accéder au Canvas.  

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 5 août 2021_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/#session-start-event/
[2]: {{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#race-conditions/