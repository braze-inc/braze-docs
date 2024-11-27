---
nav_title: Abandon du contenu connecté
article_title: Abandon du contenu connecté
page_order: 2
description: "Cet article de référence couvre plusieurs bonnes pratiques d’abandon de messages pour le contenu connecté."

---

# Abandonner du contenu connecté {#aborting-connected-content}

> À l’aide d’un modèle Liquid, vous avez la possibilité d’abandonner des messages avec logique conditionnelle. 

Dans l’exemple suivant, les conditions `connected.recommendations.size < 5` et `connected.foo.bar == nil` spécifient des situations qui entraîneront l’abandon du message.

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```
{% endraw %}

Vous pouvez également spécifier un motif d'abandon, qui sera enregistré dans le [journal des activités liées aux messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). Cette raison d’abandon doit être une chaîne de caractères et ne peut pas contenir de liquide.

{% raw %}
`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
Braze ne comptabilise pas les messages interrompus dans le nombre d'envois de votre compte Braze ou de Currents.
{% endalert %}
