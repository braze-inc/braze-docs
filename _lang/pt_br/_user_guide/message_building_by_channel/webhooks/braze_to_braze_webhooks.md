---
nav_title: Crie um webhook Braze para Braze
article_title: Crie um Webhook Braze para Braze
page_order: 3
channel:
  - webhooks
description: "Este artigo de referência cobre quando usar Atualização de Usuário versus webhooks Braze para Braze e como criar um webhook Braze para Braze."

---

# Crie um webhook Braze para Braze

> Webhooks Braze para Braze permitem que você chame a [Braze REST API]({{site.baseurl}}/api/basics/) de dentro do Braze usando um [Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) em uma [Campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) ou [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/). Use isso para tarefas de orquestração, como acionar um [Canvas acionado por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/). Para atualizar [Atributos de usuário]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), [Eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) ou [Compras]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/) do Canvas, use [Atualização de Usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) em vez disso. É projetado para mudanças no perfil do usuário e processa atualizações de forma mais eficiente.

Para aproveitar ao máximo este artigo, você deve estar familiarizado com [como os webhooks funcionam]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) e como [criar um webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) no Braze.

## Use Atualização de Usuário para mudanças nos dados do usuário

Para atualizar perfis de usuário de dentro de um Canvas, incluindo modificar [Atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), registrar [Eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) ou registrar [Compras]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/), use [Atualização de Usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) em vez de um webhook Braze para Braze. 

A Atualização de Usuário agrupa várias mudanças e as envia em lotes, tornando-a mais rápida do que webhooks. É mais fácil de configurar do que um webhook e suporta atualizações complexas através de seu [composer JSON avançado]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#advanced-json-composer). Por exemplo, para contar quantas vezes um usuário viu uma mensagem, use o [recurso de incremento e decremento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#increasing-and-decreasing-values) da Atualização de Usuário em vez de um webhook Braze para Braze.

{% alert tip %}
Adicione [Atualização de Usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) ao seu Canvas para atualizar os atributos, eventos e compras de um usuário usando um composer JSON.
{% endalert %}

## Quando usar um webhook Braze para Braze

A Atualização de Usuário pode lidar com quase todas as mesmas tarefas que um webhook Braze para Braze para atualizar perfis de usuário. Para atualizações complexas além de atributos personalizados simples, você pode usar o [composer JSON avançado]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#advanced-json-composer).

Você pode usar um webhook Braze para Braze quando precisar chamar a [REST API]({{site.baseurl}}/api/basics/) do Braze de dentro do Braze para cenários além de atualizações diretas de usuários a partir de etapas do Canvas. Exemplos comuns incluem:

- Acionar um [Canvas acionado por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) de outro Canvas
- Chamando outros [endereços de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/) para padrões de orquestração onde um fluxo de trabalho no Braze precisa invocar uma API que não possui um componente Canvas dedicado

Para atualizações de usuários dentro do Canvas, o método recomendado é usar [Atualização de Usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/).

## Pré-requisitos

Para criar um webhook Braze-para-Braze, você precisa de uma [chave de API]({{site.baseurl}}/api/api_key/) com permissões para o endpoint que deseja alcançar. Por exemplo, para disparar um Canvas acionado por API, você precisa de uma chave de API com a permissão `canvas.trigger.send`.

## Configuração de seu webhook Braze-to-Braze

O fluxo de trabalho geral para criar um webhook Braze-para-Braze segue estas etapas:

1. [Criar um webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) como uma campanha ou componente Canvas. 
2. Escolha **Modelo em Branco**.
3. Na aba **Compor**, especifique a **URL do Webhook** e o **Corpo da Solicitação** para seu caso de uso da API.
4. Na aba **Configurações**, especifique seu **Método HTTP** e **Headers da Solicitação** conforme exigido pelo endpoint.
5. Configure quaisquer configurações de entrega adicionais (por exemplo, disparar a partir de um evento personalizado) e construa o restante de sua campanha ou Canvas.

## Disparar uma segunda canva a partir de uma canva inicial

Neste caso de uso, você cria dois Canvases e usa um webhook Braze-para-Braze para disparar o segundo Canvas a partir do primeiro. Isso age como um gatilho de entrada para quando um usuário atinge um certo ponto em outro canva.

1. Comece criando sua segunda canva—a canva que deve ser acionada pela sua canva inicial.
2. Para o canva **Programação de Entrada**, selecione **Disparado por API**.
3. Faça uma nota do seu **canva ID**. Você precisará disso em uma etapa posterior.
4. Continue construindo as etapas do seu segundo canva, depois salve o canva.
5. Finalmente, crie sua primeira canva. Encontre a etapa onde você deseja disparar o segundo canva e crie uma nova etapa com um webhook.

Consulte o seguinte ao configurar seu webhook:

- **URL do Webhook:** Sua [URL do endpoint REST]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) seguida de `/canvas/trigger/send`. Por exemplo, para a instância `US-06`, o URL seria `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Corpo da Solicitação:** Texto bruto

#### Cabeçalhos e método da solicitação

O Braze requer um cabeçalho HTTP para autorização que inclua sua chave de API e outro que declare seu tipo de conteúdo.

- **Cabeçalhos de solicitação:**
  - **Autorização:** `Bearer YOUR_API_KEY`
  - **Tipo de Conteúdo:** `application/json`
- **Método HTTP:** `POST`

Substitua `YOUR_API_KEY` por uma chave de API do Braze que tenha permissões `canvas.trigger.send`. Você pode criar uma chave de API no painel do Braze acessando **Configurações** > **Chaves de API**.

![Headers da solicitação para o webhook mostrando os campos de Autorização e Tipo de Conteúdo no painel do Braze.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Corpo da solicitação

Adicione seu `/canvas/trigger/send` pedido no campo de texto. Para detalhes, veja [Enviando mensagens do Canvas via entrega acionada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/). O seguinte é um exemplo do corpo da solicitação para este endpoint, onde `your_canvas_id` é o ID do canva do seu segundo canva:

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

Quando um usuário atinge esta etapa do webhook no primeiro canva, o Braze aciona o segundo canva para esse usuário via API.

## Considerações

- **Atualizações do usuário:** Para atualizar perfis de usuários a partir do canva (atributos, eventos, compras), use [Atualização de Usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) em vez de webhooks Braze-to-Braze para melhor eficiência e custo-benefício.
- Webhooks Braze-to-Braze estão sujeitos a [Limites de taxa]({{site.baseurl}}/api/api_limits/) do endpoint.
- Atualizações no perfil do usuário incorrerão em [Pontos de dados]({{site.baseurl}}/user_guide/data/data_points/) que contam para o seu consumo total, enquanto acionar outra mensagem através dos endpoints de envio de mensagens não conta.
- Para segmentar [Usuários anônimos]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles), use `braze_id` em vez de `external_id` no corpo da solicitação do seu webhook.
- Você pode salvar seu webhook Braze-to-Braze como um [Modelo de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) para reutilização.
- Você pode verificar o [Registro de Atividade de Mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) para visualizar e solucionar falhas de webhook.


