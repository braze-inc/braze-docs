---
nav_title: Jampp
article_title: Jampp
alias: /partners/jampp/
description: "Este artigo de referência descreve a parceria entre a Braze e a Jampp, uma plataforma de marketing de performance usada para aquisição e redirecionamento de clientes móveis."
page_type: partner
search_tag: Partner

---

# Jampp

> A [Jampp](https://www.jampp.com/) é uma plataforma de marketing de performance usada para aquisição e redirecionamento de clientes móveis. Jampp combina dados comportamentais com tecnologia preditiva e programática para gerar receita para os anunciantes, exibindo anúncios pessoais e relevantes que inspiram os consumidores a comprar pela primeira vez ou com mais frequência.

_Esta integração é mantida pela Jampp._

## Sobre a integração

A integração entre a Braze e a Jampp permite que os usuários da Braze sincronizem eventos na Jampp via eventos de webhook da Braze. Como resultado, os clientes podem adicionar conjuntos de dados mais ricos às suas iniciativas de redirecionamento dentro de seus ecossistemas de publicidade móvel.

Alguns exemplos de quando pode ser recomendável redirecionar clientes com anúncio:
- Quando o estado de inscrição de e-mail ou push de um cliente muda.
- Como um cliente interagiu com uma campanha de mensagens da Braze.
- Se o cliente tiver acionado uma geofence específica.

## Pré-requisitos

Esta integração suporta aplicativos iOS e Android.

| Requisito | Descrição |
|---|---|
| Conta da Jampp | Uma [conta Jampp](https://www.jampp.com/) é necessária para aproveitar esta parceria. |
| ID do app para Android | Seu identificador exclusivo do aplicativo Braze para Android (como "com.example"). |
| ID do app para iOS | Seu identificador exclusivo do aplicativo Braze para iOS (como "012345678"). |
| Ativar a coleta de IDFA no SDK da Braze | A coleta de IDFA é opcional no SDK da Braze e fica desativada por padrão. | 
| Coleta de ID de publicidade do Google via atributo personalizado | A coleta do ID de publicidade do Google é opcional para os clientes e pode ser coletada como um [atributo personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types).
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integração

### Etapa 1: Crie um modelo de webhook no Braze

Para criar um modelo de webhook do Jampp para usar em campanhas futuras ou canvas, navegue até **Modelos** > **Modelos de Webhook** na plataforma Braze.

Se você gostaria de fazer uma campanha de webhook única do Jampp ou usar um modelo existente, selecione **Webhook** no Braze ao criar uma nova campanha.

No seu novo modelo de Webhook, preencha os seguintes campos:
- **Corpo da solicitação**: Texto bruto
- **URL do webhook**:
{% raw %}
```liquid
{% assign event_name = 'your_jampp_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'{{event_name}}','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

http://tracking.jampp.com/event?kind={{event_name}}&rnd={{rnd}}&app={% if {{most_recently_used_device.${idfa}}} == blank %}{{android_app_id}}{% else %}{{iOS_app_id}}{% endif %}&apple_ifa={{most_recently_used_device.${idfa}}}&google_advertising_id={{custom_attribute.${aaid}}}&user_agent={user-agent}&prtnr=braze

{% if {{most_recently_used_device.${idfa}}} == blank and {{custom_attribute.${aaid}}} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

No URL do webhook, você precisa:
- Defina o nome do evento. Este nome aparecerá no seu dashboard do Jampp.
- Passe o identificador exclusivo do aplicativo do seu app para Android (como "com.example") e iOS (como "012345678").
- Insira [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid) para o atributo personalizado apropriado que você está rastreando como o ID de publicidade do Google. Observe que o ID de publicidade do Google está listado como `aaid` neste exemplo, mas você precisará substituí-lo pelo nome do atributo personalizado que seus desenvolvedores definiram.

![A URL do webhook e a prévia da mensagem mostradas no construtor de webhook do Braze.]({% image_buster /assets/img/jampp_webhook.png %})

{% alert important %}
A Braze não coleta automaticamente o IDFA/AAID do dispositivo, então você deve armazenar esses valores. Esteja ciente de que você pode precisar do consentimento do usuário para coletar esses dados.
{% endalert %}

#### Cabeçalhos de solicitação e método

O webhook do Jampp requer um método HTTP e um cabeçalho de solicitação.

- **Método HTTP**: OBTER
- **Cabeçalhos de solicitação**:
  - **Content-Type**: application/json

![Os cabeçalhos da solicitação, o método HTTP e a prévia da mensagem mostrados no construtor de webhook do Braze.]({% image_buster /assets/img/jampp_method.png %})

#### Corpo da solicitação

Você não precisa definir um corpo de solicitação para este webhook.

### Etapa 2: veja uma prévia da sua solicitação

Prévia a mensagem para garantir que a solicitação esteja sendo renderizada corretamente para diferentes usuários. Recomendamos visualizar e enviar solicitações de teste para usuários de Android e iOS. Se a solicitação for bem-sucedida, a API responderá com `HTTP 204`.

{% alert important %}
Lembre-se de salvar seu modelo antes de sair da página! <br>Os modelos de webhook atualizados podem ser encontrados na lista **Modelos de webhook salvos** ao criar uma nova [campanha de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}


