---
nav_title: "Abandon d'un contenu connecté"
article_title: "Abandon d'un contenu connecté"
page_order: 2
description: "Cet article de référence présente les meilleures pratiques en matière d'envoi de messages pour le contenu connecté."
---

# Abandon d'un contenu connecté {#aborting-connected-content}

> Lorsque vous utilisez le modèle Liquid, vous avez la possibilité d'interrompre les messages à l'aide d'une logique conditionnelle. Cette page présente les meilleures pratiques en la matière.

Dans l'exemple suivant, les conditionnelles `connected.recommendations.size < 5` et `connected.foo.bar == nil` précisent les situations qui entraîneraient l'abandon du message.

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```
{% endraw %}

## Spécifiez un motif d'abandon

Vous pouvez également spécifier un motif d'abandon, qui sera enregistré dans le [journal d'activité des messages.]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) Ce motif d'abandon doit être une chaîne de caractères et ne peut pas contenir de Liquid.

{% raw %}
`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
Braze ne comptabilise pas les messages interrompus dans le nombre d'envois de votre compte Braze ou de Currents.
{% endalert %}
