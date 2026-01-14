---
nav_title: Abortar conteúdo conectado
article_title: Abortar conteúdo conectado
page_order: 2
description: "Este artigo de referência aborda algumas práticas recomendadas de interrupção de mensagens para o Connected Content."
---

# Abortar conteúdo conectado {#aborting-connected-content}

> Ao usar o modelo Liquid, você tem a opção de abortar mensagens com lógica condicional. Esta página aborda as práticas recomendadas para fazer isso.

No exemplo a seguir, as condicionais `connected.recommendations.size < 5` e `connected.foo.bar == nil` especificam situações que fariam com que a mensagem fosse abortada.

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```
{% endraw %}

## Especificar um motivo para abortar

Também é possível especificar um motivo de cancelamento, que será salvo no [Registro de atividades de mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). Esse motivo de abortamento deve ser uma cadeia de caracteres e não pode conter Liquid.

{% raw %}
`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
O Braze não conta as mensagens abortadas para a contagem de envios em sua conta do Braze ou no Currents.
{% endalert %}
