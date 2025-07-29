---
nav_title: Como criar um webhook Braze-to-Braze
article_title: Como criar um webhook Braze-to-Braze
page_order: 3
channel:
  - webhooks
description: "Este artigo aborda como criar um webhook Braze-para-Braze para casos de uso chave."

---

# Criação de um webhook Braze-to-Braze

> Você pode usar webhooks para se comunicar com a [API]({{site.baseurl}}/api/basics/) Braze [REST]({{site.baseurl}}/api/basics/), essencialmente fazendo qualquer coisa que nossa API permita que você faça. Nós nos referimos a isso como um webhook Braze-to-Braze—um webhook que está se comunicando de Braze para Braze. Os casos de uso nesta página pressupõem que você esteja familiarizado com o [funcionamento dos]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) [webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) e com a [criação de um webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) no Braze.

## Pré-requisitos

Para criar um webhook Braze-to-Braze, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com permissões para o endpoint que deseja acessar.

## Configuração de seu webhook Braze-to-Braze

Embora os detalhes da sua solicitação de webhook variem de caso para caso, o fluxo de trabalho geral para criar um webhook Braze-para-Braze permanece o mesmo.

1. [Crie um webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) como uma campanha ou componente do Canva. 
2. Escolha **Modelo em Branco**.
3. Na **guia** Compose, especifique a **URL do Webhook** e o **Corpo da Solicitação** conforme observado para seu caso de uso.
4. Na guia **Configurações**, especifique seu **Método HTTP** e **Headers de Solicitação** conforme observado para seu caso de uso.
5. Continue a construir o restante do seu webhook conforme necessário. Alguns casos de uso exigem configurações de entrega específicas, como acionar a campanha ou canva a partir de um evento personalizado.

## Casos de uso

Embora haja muito o que fazer com os webhooks Braze-to-Braze, aqui estão alguns casos de uso para você começar:

- Incremente um atributo personalizado de inteiro para um contador quando um usuário receber uma mensagem.
- Disparar um segundo canva a partir de um canva inicial.

{% alert tip %}
Adicione uma [etapa de Atualização do Usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) ao seu canva para rastrear os atributos, eventos e compras de um usuário em um criador de JSON. Dessa forma, essas atualizações são agrupadas para que a Braze possa processá-las de maneira mais eficiente do que um webhook Braze-para-Braze.
{% endalert %}

### Caso de uso: Incrementar um atributo personalizado de inteiro para um contador

Este caso de uso envolve a criação de um atributo personalizado e o uso de Liquid para contar o número de vezes que uma ação específica ocorreu. 

Por exemplo, você pode querer contar quantas vezes um usuário viu uma campanha ativa de mensagem no app e impedi-lo de receber a campanha novamente depois de tê-la visto três vezes. Para mais ideias sobre o que você pode fazer com a lógica Liquid no Braze, confira nossa [biblioteca de casos de uso do Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases).

Siga as etapas gerais para criar um webhook Braze-para-Braze e consulte o seguinte ao configurar seu webhook:

- **URL do Webhook:** Seu [URL do endpoint REST]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) seguido por `/users/track`. Por exemplo, para a instância `US-06`, o URL seria `https://rest.iad-06.braze.com/users/track`.
- **Corpo da Solicitação:** Texto bruto

#### Cabeçalhos e método da solicitação

A Braze requer um cabeçalho HTTP para autorização que inclua sua chave de API e outro que declare seu `content-type`.

- **Cabeçalho da solicitação:**
  - **Autorização:** Portador {YOUR_API_KEY}
  - **Content-Type:** application/json
- **Método HTTP:** POST

Substitua `YOUR_API_KEY` por uma chave de API da Braze com permissões `users.track`. Você pode criar uma chave de API no dashboard do Braze em **Configurações** > **Chaves de API**.

![Os cabeçalhos de solicitação para o webhook.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Corpo da solicitação

Adicione sua solicitação de faixa de usuário no corpo da solicitação e o Liquid para atribuir uma variável de contador. Para obter mais detalhes, consulte o [ponto de extremidade`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

A seguir, um exemplo do Liquid necessário e do corpo da solicitação para esse endpoint, em que `your_attribute_count` é a atribuição que você está usando para contar quantas vezes um usuário viu uma mensagem:

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
Cada vez que um contador de atributo personalizado é atualizado (incrementado ou decrementado), ele consumirá um [ponto de dados]({{site.baseurl}}/user_guide/data/data_points/), que conta para o seu consumo geral.
{% endalert %}

### Caso de uso: Disparar uma segunda canva a partir de uma canva inicial

Para este caso de uso, você criará dois canvas e usará um webhook para disparar o segundo canva a partir do primeiro canva. Isso age como um gatilho de entrada para quando um usuário atinge um certo ponto em outro canva.

1. Comece criando sua segunda canva—a canva que deve ser acionada pela sua canva inicial. 
2. Para o canva **Programação de Entrada**, selecione **Disparado por API**.
3. Faça uma nota do seu **canva ID**. Você precisará disso em uma etapa posterior.
4. Continue construindo as etapas do seu segundo canva, depois salve o canva.
5. Finalmente, crie sua primeira canva. Encontre a etapa onde você deseja disparar o segundo canva e crie uma nova etapa com um webhook. 

Consulte o seguinte ao configurar seu webhook:

- **URL do Webhook:** Seu [URL do endpoint REST]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) seguido por `canvas/trigger/send`. Por exemplo, para a instância US-06, o URL seria `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Corpo da Solicitação:** Texto bruto

#### Cabeçalhos e método da solicitação

A Braze requer um cabeçalho HTTP para autorização que inclua sua chave de API e outro que declare seu `content-type`.

- **Cabeçalho da solicitação:**
  - **Autorização:** Portador `YOUR_API_KEY`
  - **Content-Type:** application/json
- **Método HTTP:** POST

Substitua `YOUR_API_KEY` por uma chave de API da Braze com permissões `canvas.trigger.send`. Você pode criar uma chave de API no dashboard do Braze em **Configurações** > **Chaves de API**.

![Os cabeçalhos de solicitação para o webhook.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Corpo da solicitação

Adicione seu `canvas/trigger/send` pedido no campo de texto. Para obter mais detalhes, consulte [Envio de mensagens do Canva via entrega disparada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/). O seguinte é um exemplo do corpo da solicitação para este endpoint, onde `your_canvas_id` é o ID do canva do seu segundo canva: 

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

- Os webhooks de Braze para Braze estão sujeitos a[limites de taxa]({{site.baseurl}}/api/api_limits/) de endpoints.
- As atualizações no perfil do usuário incorrerão em [pontos de dados extras]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#consumption-count), enquanto disparar outra mensagem através dos endpoints de envio de mensagens não incorrerá.
- Se você quiser direcionar [usuários anônimos]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles), pode usar `braze_id` em vez de `external_id` no corpo da solicitação do seu webhook.
- Você pode salvar seu webhook Braze-to-Braze como um [modelo]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) para ser usado novamente.
- Você pode verificar o [Registro de Atividade de Mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) para visualizar e solucionar falhas de webhook.


