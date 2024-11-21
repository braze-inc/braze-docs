---
nav_title: Abortando Conteúdo Conectado
article_title: Abortando Conteúdo Conectado
page_order: 2
description: "Este artigo de referência cobre algumas das melhores práticas de interrupção de mensagens para conteúdo conectado."

---

# Abortando conteúdo conectado {#aborting-connected-content}

> Usando a modelagem Liquid, você tem a opção de abortar mensagens com lógica condicional. 

No exemplo a seguir, os condicionais `connected.recommendations.size < 5` e `connected.foo.bar == nil` especificam situações que causariam a interrupção da mensagem.

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```
{% endraw %}

Você também pode especificar um motivo de aborto, que será salvo no [Registro de Atividade de Mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). Este motivo de aborto deve ser uma string e não pode conter Liquid.

{% raw %}
`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
Braze não conta mensagens abortadas para a contagem de envios na sua conta Braze ou em Currents.
{% endalert %}
