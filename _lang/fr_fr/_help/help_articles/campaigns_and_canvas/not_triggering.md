---
nav_title: Campagne ou Canvas non déclenché
article_title: Campagne ou Canvas non déclenché
page_order: 5

page_type: solution
description: "Cet article d’aide décrit les étapes pour résoudre les problèmes liés aux campagnes ou aux canvas qui ne se déclenchent pas comme prévu."
tool: 
- Campaigns
- Canvas
---

# Campagne ou Canvas non déclenché

Plusieurs raisons peuvent expliquer pourquoi un comportement de déclenchement attendu ne s’est pas produit. La solution pour l’erreur la plus courante est de s’assurer que la campagne que vous déclenchez n’utilise pas le même événement déclencheur dans le segment.

## Déclencheurs de campagne

L’appartenance au segment est évaluée avant les actions de déclenchement. Cela signifie que si l’utilisateur n’entre pas d’abord dans le segment, il ne recevra pas la campagne même s’il exécute le déclencheur.

Si votre campagne déclenche un événement personnalisé, vous devez vous assurer que cet événement n’est pas préfiltré par un segment que vous souhaitez utiliser dans la campagne. 

Par exemple, si le segment inclut l'événement `SessionStart` "A utilisé l'application plus d'une fois" et que l'événement à partir duquel la campagne se déclenche est `SessionStart`, l'utilisateur recevra le message, mais pas nécessairement pour la première session. En effet, lors de la première étape au cours de la vérification pour savoir si un utilisateur doit recevoir une campagne, la campagne examine l’audience cible du segment. 

En bref, évitez de configurer une campagne basée sur une action ou un Canvas avec le même déclencheur que le filtre d'audience (comme un attribut modifié ou l'exécution d'un événement personnalisé). Une [condition de concurrence]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#race-conditions/) peut se produire : l'utilisateur n'est pas dans l'audience lorsqu'il effectue l'événement déclencheur, ce qui signifie qu'il ne recevra pas la campagne ou n'entrera pas dans le Canvas.

{% alert tip %}
Pour toute assistance supplémentaire avec le dépannage de la campagne, assurez-vous de contacter le support Braze dans les 30 jours suivant la survenue de votre problème, car nous ne disposons que des 30 derniers jours de journaux de diagnostic.
{% endalert %}

_Dernière mise à jour le 25 juin 2024_

