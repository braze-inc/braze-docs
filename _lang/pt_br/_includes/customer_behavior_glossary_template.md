---
nav_title: Comportamento do cliente e eventos do usuário
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Este glossário lista os vários eventos de comportamento do cliente e do usuário que o Braze pode rastrear e enviar para os Data Warehouses escolhidos usando Currents."
tool: Currents
search_rank: 7
---

Entre em contato com seu representante Braze ou abra um [ticket de suporte]({{site.baseurl}}/braze_support/) se precisar de acesso a direitos de eventos adicionais. Se não encontrar o que precisa nesta página, consulte nossa [Biblioteca de eventos de engajamento com mensagens]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) ou nossos [exemplos de dados de amostra do Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explicação do comportamento do cliente e da estrutura de eventos do usuário e valores da plataforma %}

### Estrutura do evento

Esse detalhamento do comportamento do cliente e dos eventos do usuário mostra que tipo de informação é geralmente incluído em um comportamento do cliente ou evento do usuário. Com uma sólida compreensão de seus componentes, seus desenvolvedores e a equipe de estratégia de business intelligence podem usar os dados de eventos Currents recebidos para criar relatórios e gráficos orientados por dados e tirar proveito de outras métricas de dados valiosas.

![Detalhamento de um evento de usuário mostrando um evento de compra com as propriedades listadas agrupadas por propriedades específicas do usuário, propriedades específicas do comportamento e propriedades específicas do dispositivo]({% image_buster /assets/img/customer_engagement_event.png %})

O comportamento do cliente e os eventos do usuário são compostos por propriedades **específicas do usuário**, propriedades **específicas do comportamento** e propriedades **específicas do dispositivo**.

### Valores da plataforma

Certos eventos retornam um valor `platform` que especifica a plataforma do dispositivo do usuário.
<br>A tabela a seguir detalha os possíveis valores retornados:

| Dispositivo do usuário | Valor da plataforma |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% enddetails %}

{% alert important %}
Os esquemas de armazenamento se aplicam aos dados de eventos de arquivo simples que enviamos aos parceiros de armazenamento de data warehouse (como Google Cloud Storage, Amazon S3 e Microsoft Azure Blob Storage). Algumas combinações de eventos e destinos listadas aqui ainda não estão disponíveis para todos. Para obter informações sobre quais eventos são apoiados por vários parceiros, consulte nossa lista de [parceiros disponíveis]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) e verifique suas respectivas páginas.<br><br>Além disso, observe que o Currents descartará eventos com cargas úteis excessivamente grandes, superiores a 900 KB.
{% endalert %}