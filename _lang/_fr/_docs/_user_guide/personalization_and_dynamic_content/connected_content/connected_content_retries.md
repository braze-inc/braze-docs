---
nav_title: Tentatives de contenu connecté
article_title: Tentatives de contenu connecté
page_order: 3
description: "Parce que le Contenu Connecté dépend de la réception de données provenant d'API, il est possible qu'une API soit indisponible par intermittence pendant que Braze fait l'appel. Cet article explique comment gérer les tentatives de contenu connecté."
---

# Tentatives de contenu connecté

Parce que le Contenu Connecté dépend de la réception de données provenant d'API, il est possible qu'une API soit indisponible par intermittence pendant que Braze fait l'appel. Dans ce cas, Braze prend en charge la logique de retenter la requête en utilisant le backoff exponentiel. Pour activer les tentatives, ajoutez `:retry` dans l'appel de contenu connecté, comme indiqué ci-dessous:
{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

Si l'appel API échoue et que ceci est activé, Braze va recommencer l'appel tout en respectant la [limite de taux][47] que vous avez définie pour chaque renvoyé. Braze déplacera tous les messages échoués à l'arrière de la file et ajoutera des minutes supplémentaires si nécessaire, au total les minutes qu'il faudrait pour envoyer votre message.

Si une tentative de réessai réussit, le message est envoyé et aucune nouvelle tentative n'est tentée pour ce message. Si les erreurs d'appel de contenu connecté sont 5 fois, le message est abandonné de la même façon que si une balise [d'annulation][1] a été déclenchée.

{% alert note %}
Le contenu connecté `:retry` n'est pas disponible pour les messages In-App.
{% endalert %}


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[47]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting
