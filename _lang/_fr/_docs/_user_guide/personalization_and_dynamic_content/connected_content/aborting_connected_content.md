---
nav_title: Abandon du contenu connecté
article_title: Abandon du contenu connecté
page_order: 2
description: "En utilisant le modèle Liquid, vous avez la possibilité d'annuler les messages avec des conditions. Cet article de référence couvre certains messages qui annulent les meilleures pratiques."
---

# Abandon des messages {#aborting-connected-content}

En utilisant le modèle Liquid, vous avez la possibilité d'annuler les messages avec des conditions. Par exemple :

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```

Dans l'exemple ci-dessus, les conditions `connected.recommendations.size < 5` et `connectées. oo.bar == nil` spécifie des situations qui feraient échouer le message.

Vous pouvez également spécifier une raison d'abandon qui sera enregistrée dans le __Journal d'activité des messages__ dans votre __Console développeur__. Cette raison d'annulation doit être une chaîne de caractères et ne peut pas contenir de Liquid.

`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
Braze ne compte pas les Messages Abandonnés pour le nombre d'envoi dans votre compte Braze ou dans le compte actuel.
{% endalert %}
