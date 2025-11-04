---
nav_title: Criação de um webhook Braze-to-Braze
article_title: Criação de um webhook Braze-to-Braze
page_order: 3
channel:
  - webhooks
description: "Este artigo aborda como criar um webhook Braze-to-Braze para os principais casos de uso."

---

# Criação de um webhook Braze-to-Braze

> Você pode usar webhooks para se comunicar com a Braze [REST API]({{site.baseurl}}/api/basics/), basicamente fazendo qualquer coisa que nossa API permita que você faça. Nós nos referimos a isso como um webhook Braze-to-Braze - um webhook que está se comunicando de Braze para Braze. Os casos de uso nesta página pressupõem que você esteja familiarizado com o [funcionamento dos]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) [webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) e com a [criação de um webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) no Braze.

## Pré-requisitos

Para criar um webhook Braze-to-Braze, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com permissões para o endpoint que deseja acessar.

## Configuração de seu webhook Braze-to-Braze

Embora as especificidades de sua solicitação de webhook variem de um caso de uso para outro, o fluxo de trabalho geral para criar um webhook Braze-to-Braze permanece o mesmo.

1. [Crie um webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) como uma campanha ou componente do Canvas. 
2. Selecione **Blank Template (Modelo em branco**).
3. Na guia **Compose (Compor** ), especifique o **URL do webhook** e o **Request Body (Corpo da solicitação** ) conforme indicado para o seu caso de uso.
4. Na guia **Settings (Configurações** ), especifique seu **HTTP Method (Método HTTP** ) e **Request Headers (Cabeçalhos de solicitação** ) conforme indicado para seu caso de uso.
5. Continue a desenvolver o restante de seu webhook conforme necessário. Alguns casos de uso exigem configurações de entrega específicas, como o acionamento da campanha ou do Canvas a partir de um evento personalizado.

## Casos de uso

Embora haja muitas coisas que você pode fazer com os webhooks Braze-to-Braze, aqui estão alguns casos de uso para você começar:

- Incrementa um atributo personalizado inteiro para um contador quando um usuário recebe uma mensagem.
- Aciona um segundo Canvas a partir de um Canvas inicial.

{% alert tip %}
Adicione uma [etapa de atualização de usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) ao seu Canvas para rastrear os atributos, eventos e compras de um usuário em um compositor JSON. Dessa forma, essas atualizações são agrupadas para que o Braze possa processá-las com mais eficiência do que um webhook Braze-to-Braze.
{% endalert %}

### Caso de uso: Incrementar um atributo personalizado inteiro para um contador

Esse caso de uso envolve a criação de um atributo personalizado e o uso do Liquid para contar o número de vezes que uma ação específica ocorreu. 

Por exemplo, você pode querer contar quantas vezes um usuário viu uma campanha de mensagem in-app ativa e impedir que ele receba a campanha novamente depois de tê-la visto três vezes. Para obter mais ideias sobre o que você pode fazer com a lógica Liquid no Braze, consulte nossa [biblioteca de casos de uso Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases).

Siga as etapas gerais para criar um webhook Braze-to-Braze e consulte o seguinte ao configurar seu webhook:

- **URL do webhook:** Seu [URL do endpoint REST]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) seguido de `/users/track`. Por exemplo, para a instância `US-06`, o URL seria `https://rest.iad-06.braze.com/users/track`.
- **Corpo da solicitação:** Texto bruto

#### Cabeçalhos de solicitação e método

O Braze exige um cabeçalho HTTP para autorização que inclui sua chave de API e outro que declara seu endereço `content-type`.

- **Cabeçalho da solicitação:**
  - **Autorização:** Portador {YOUR_API_KEY}
  - **Content-Type:** application/json
- **Método HTTP:** POST

Substitua `YOUR_API_KEY` por uma chave Braze API com permissões `users.track`. Você pode criar uma chave de API no painel de controle do Braze em **Configurações** > **Chaves de API**.

\![Os cabeçalhos de solicitação do webhook.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Corpo da solicitação

Adicione sua solicitação de rastreamento de usuário no corpo da solicitação e o Liquid para atribuir uma variável de contador. Para obter mais detalhes, consulte o [ponto de extremidade`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

A seguir, um exemplo do Liquid necessário e do corpo da solicitação para esse endpoint, em que `your_attribute_count` é o atributo que você está usando para contar quantas vezes um usuário viu uma mensagem:

{% raw %}
```json
{% assign new_number = {{custom_attribute.${your_attribute_count}}} | plus: 1 %}
{
    "attributes": [
        {
        "external_id": "{{${user_id}}}",
        "your_attribute_count": "{{new_number}}"
        }
    ]
}
```
{% endraw %}

{% alert note %}
Cada vez que um contador de atributo personalizado é atualizado (incrementado ou decrementado), ele consome um [ponto de dados]({{site.baseurl}}/user_guide/data/data_points/), que conta para o seu consumo geral.
{% endalert %}

### Caso de uso: Acionar um segundo Canvas a partir de um Canvas inicial

Para esse caso de uso, você criará dois Canvases e usará um webhook para acionar o segundo Canvas a partir do primeiro Canvas. Isso funciona como um acionador de entrada para quando um usuário atinge um determinado ponto em outro Canvas.

1. Comece criando seu segundo Canvas - o Canvas que deve ser acionado pelo Canvas inicial. 
2. Para o **cronograma de entrada** do Canvas, selecione **API-Triggered**.
3. Anote sua **ID do Canvas**. Você precisará disso em uma etapa posterior.
4. Continue construindo as etapas de seu segundo Canvas e salve o Canvas.
5. Por fim, crie seu primeiro Canvas. Encontre a etapa em que você deseja acionar o segundo Canvas e crie uma nova etapa com um webhook. 

Consulte o seguinte ao configurar seu webhook:

- **URL do webhook:** Seu [URL do endpoint REST]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) seguido de `canvas/trigger/send`. Por exemplo, para a instância US-06, o URL seria `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Corpo da solicitação:** Texto bruto

#### Cabeçalhos de solicitação e método

O Braze exige um cabeçalho HTTP para autorização que inclui sua chave de API e outro que declara seu endereço `content-type`.

- **Cabeçalho da solicitação:**
  - **Autorização:** Portador `YOUR_API_KEY`
  - **Content-Type:** application/json
- **Método HTTP:** POST

Substitua `YOUR_API_KEY` por uma chave Braze API com permissões `canvas.trigger.send`. Você pode criar uma chave de API no painel de controle do Braze em **Configurações** > **Chaves de API**.

\![Os cabeçalhos de solicitação do webhook.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Corpo da solicitação

Adicione sua solicitação `canvas/trigger/send` no campo de texto. Para obter mais detalhes, consulte [Envio de mensagens do Canvas por meio de entrega acionada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/). A seguir, um exemplo do corpo da solicitação para esse endpoint, em que `your_canvas_id` é a ID do Canvas do seu segundo Canvas: 

{% raw %}
```json
{
      "canvas_id": "your_canvas_id",
      "recipients": [
        {
          "external_user_id": "{{${user_id}}}"
         }
      ]
}
```
{% endraw %}

## Coisas para saber

- Os webhooks Braze-to-Braze estão sujeitos a [limites de taxa de]({{site.baseurl}}/api/api_limits/) endpoint.
- As atualizações do perfil do usuário incorrerão em [pontos de dados]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#consumption-count) adicionais, enquanto o acionamento de outra mensagem por meio dos pontos de extremidade de mensagens não.
- Se quiser atingir [usuários anônimos]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles), poderá usar `braze_id` em vez de `external_id` no corpo da solicitação do webhook.
- Você pode salvar seu webhook Braze-to-Braze como um [modelo]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) para ser usado novamente.
- Você pode verificar o [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) para visualizar e solucionar problemas de falhas no webhook.


