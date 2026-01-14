---
nav_title: Eventos de engajamento com mensagens
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "Este glossário lista os vários Eventos de Engajamento com Mensagens que o Braze pode rastrear e enviar para Data Warehouses escolhidos usando Currents."
tool: Currents
search_rank: 6
---

Os esquemas de armazenamento se aplicam aos dados de eventos de arquivo simples que enviamos aos parceiros de armazenamento do Data Warehouse (Google Cloud Storage, Amazon S3 e Microsoft Azure Blob Storage). Para esquemas que se aplicam a outros parceiros, consulte nossa lista de [parceiros disponíveis]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) e verifique suas respectivas páginas.

Entre em contato com o gerente da sua conta ou abra um [ticket de suporte]({{site.baseurl}}/braze_support/) se precisar de acesso a direitos de eventos adicionais. Se não encontrar o que precisa neste artigo, consulte nossa [Biblioteca de eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) ou nossos [exemplos de dados de amostra Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explicação da estrutura do evento de engajamento com mensagens e dos valores da plataforma %}

### Estrutura do evento

Esse detalhamento do evento mostra que tipo de informação geralmente é incluído em um evento de engajamento com mensagem. Com uma sólida compreensão de seus componentes, seus desenvolvedores e a equipe de estratégia de business intelligence podem usar os dados de eventos Currents recebidos para criar relatórios e gráficos orientados por dados e tirar proveito de outras métricas de dados valiosas.

![Detalhamento de um evento de engajamento com mensagem mostrando um evento de cancelamento de inscrição de e-mail com as propriedades listadas agrupadas por propriedades específicas do usuário, propriedades de rastreamento da campanha ou do Canvas e propriedades específicas do evento]({% image_buster /assets/img/message_engagement_event.png %})

Os eventos de engajamento com mensagens são compostos por propriedades **específicas do usuário**, propriedades de **rastreamento de campanha/canva** e propriedades **específicas do evento**.

### Esquema de ID de usuário

Note as convenções de nomenclatura para IDs de usuário.

| Esquema do Braze | Esquema de Currents | Descrição |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | O identificador exclusivo que é atribuído automaticamente pelo Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | O identificador exclusivo do perfil de um usuário que é definido pelo cliente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

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
O Currents descartará eventos com cargas úteis excessivamente grandes, superiores a 900 KB.
{% endalert %}

{% alert note %}
Os objetos relacionados ao Canvas Flow têm IDs que podem ser usados para agrupamento e traduzidos em nomes legíveis por meio do [endpoint Exportar detalhes do Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/).
{% endalert %}

{% alert note %}
Alguns campos podem levar mais tempo para exibir seu estado mais recente após a atualização de uma campanha ou do Canva. Esses campos são:
<ul>
  <li>"campaign_name" (nome da campanha)</li>
  <li>"canvas_name"</li>
  <li>"canvas_step_name"</li>
  <li>"conversion_behavior" (comportamento de conversão)</li>
  <li>"canvas_variation_name" (nome da variação da tela)</li>
  <li>"experiment_split_name"</li>
  <li>"message_variation_name" (nome da variação da mensagem)</li>
</ul>
Se for necessária uma consistência completa, recomendamos aguardar uma hora a partir da última atualização desses campos antes de enviar as mensagens aos usuários.
{% endalert %}