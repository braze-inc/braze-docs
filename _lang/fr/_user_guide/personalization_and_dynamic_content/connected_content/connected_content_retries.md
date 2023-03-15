---
nav_title: Nouvelles tentatives de contenu connecté
article_title: Nouvelles tentatives de contenu connecté
page_order: 3
description: "Cet article de référence explique comment gérer les tentatives de contenu connecté."

---

# Tentatives de contenu connecté

Étant donné que le Contenu connecté repose sur la réception des données des API, il est possible qu’une API soit momentanément indisponible tandis que Braze effectue l’appel. Dans ce cas, Braze prend en charge la logique de nouvelle tentative pour tenter de nouveau la demande à l’aide d’un délai exponentiel. Pour activer les tentatives, ajouter `:retry` dans l’appel Contenu connecté, comme indiqué dans l’extrait de code suivant :
{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

Si l’appel API échoue et que cela est activé, Braze reprendra l’appel tout en respectant la [limites de débit][47] pour chaque renvoi. Le braze déplace les messages défaillants vers l’arrière de la file d’attente et ajoute des minutes supplémentaires, si nécessaire, au nombre total de minutes qu’il faudrait pour envoyer votre message.

Si une tentative de récupération réussit, le message est envoyé et aucune nouvelle tentative n’est tentée pour ce message. Si les erreurs d’appel du Contenu connecté sont sorties 5 fois, le message est interrompu comme si [balise de message d’abandon][1] a été déclenché.

{% alert note %}
Contenu connecté `:retry` n’est pas disponible pour les messages dans l’application.
{% endalert %}


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[16]: [success@braze.com](mailto:success@braze.com)
[47]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting
