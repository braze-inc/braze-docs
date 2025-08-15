---
nav_title: Aceitação e exclusão
article_title: Aceitação e exclusão do WhatsApp
description: "Este artigo de referência aborda diferentes métodos de aceitação e exclusão do WhatsApp."
page_type: partner
search_tag: Partner
page_order: 5
channel:
  - WhatsApp
alias: /user_guide/message_building_by_channel/whatsapp/opt-ins_and_opt-outs/
---

# Aceitação e exclusão

> O envio de mensagens de aceitação e exclusão do WhatsApp é crucial, pois o WhatsApp monitora a classificação de qualidade do seu [número de telefone](https://www.facebook.com/business/help/896873687365001), e classificações baixas podem resultar na redução dos limites de frequência das mensagens. <br><br>Uma maneira de criar uma classificação de alta qualidade é impedir que os usuários bloqueiem ou denunciem sua empresa. Isso pode ser feito com o [envio de mensagens de alta qualidade](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits) (como o valor da mensagem para seus usuários), controlando a frequência das mensagens e permitindo que os clientes aceitem receber comunicações futuras. <br><br>Esta página aborda como configurar aceitações e recusas e as diferenças entre os modificadores "regex" e "is".

As aceitações podem vir de fontes externas ou de métodos Braze, como SMS ou mensagens no app e no navegador. As aceitações podem ser tratadas usando palavras-chave definidas nos botões de marketing da Braze e do WhatsApp. Consulte os métodos a seguir para obter orientação sobre a configuração de aceitações e recusas.

#### Métodos de aceitação
- [Métodos de aceitação externos ao Braze](#external-to-braze-opt-in-methods)
  - [Lista de aceitação criada externamente](#externally-built-opt-in-list)
  - [Envio de mensagens no canal de envio de mensagens do WhatsApp de suporte ao cliente](#outbound-message-in-customer-support-whatsapp-channel)
  - [Envio de mensagens do WhatsApp](#inbound-whatsapp-message)
- [Métodos de aceitação com base no Braze](#braze-powered-opt-in-methods)

#### Métodos de aceitação
- [Palavras-chave gerais de aceitação](#general-opt-out-keywords)
- [Seleção de aceitação de marketing](#marketing-opt-out-selection)

## Configure as aceitações para seu canal do Braze WhatsApp

Para aceitação do WhatsApp, você deve cumprir os [requisitos do WhatsApp](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Você também precisará fornecer ao Braze as seguintes informações:
- Um `external_id`, um [número de telefone]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) e um status de inscrição atualizado para cada usuário. Isso pode ser feito usando o [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/) ou por meio do [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para atualizar o número de telefone e o status da inscrição.

{% alert note %}
A Braze lançou uma melhoria no endpoint `/users/track` que permite atualizações no status da inscrição que você pode conhecer em [Grupos de inscrições]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status). No entanto, se você já tiver criado protocolos de aceitação usando o [endpoint `/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/), poderá continuar a fazê-lo lá.
{% endalert %}

### Métodos de aceitação externos ao Braze

Seu app ou site (registro de conta, página de checkout, configurações de conta, terminal de cartão de crédito) para o Braze.

Sempre que já houver consentimento de marketing para envio de e-mail ou mensagens de texto, inclua uma seção adicional para o WhatsApp. Após a aceitação do usuário, ele precisa de um endereço `external_id`, um [número de telefone]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) e um status de inscrição atualizado. Para fazer isso, dependendo de como sua instalação da Braze estiver configurada, aproveite o [endpoint`/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) ou use o [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/).

#### Lista de aceitação criada externamente

Se você já usou o WhatsApp anteriormente, talvez já tenha criado uma lista de usuários com aceitações de acordo com os requisitos do WhatsApp. Nesse caso, faça upload de um CSV ou use a API com as [seguintes informações]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv) na Braze.

#### Envio de mensagens no canal de envio de mensagens do WhatsApp de suporte ao cliente

Em seu canal de suporte ao cliente, acompanhe os problemas resolvidos com uma mensagem automática perguntando se eles querem aceitar o envio de mensagens de marketing. A funcionalidade aqui depende da disponibilidade de recursos na ferramenta de suporte ao cliente de sua escolha e de onde você mantém as informações do usuário.

1. Forneça um [link de mensagem](https://business.facebook.com/business/help/890732351439459?ref=search_new_0) do seu número de telefone do WhatsApp Business.
2. Fornecer [ações de resposta rápida]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/#quick-replies) em que o cliente responde "Sim" para indicar a aceitação
3. Configure o disparo de palavras-chave personalizadas.
4. Para qualquer uma dessas ideias, você provavelmente precisará terminar a jornada com o seguinte:
	- Chame o [endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para atualizar ou criar um usuário
	- Aproveite o [endpoint `/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) ou use o [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)

#### Envio de mensagens do WhatsApp 

Faça com que os clientes enviem uma mensagem de entrada para o número do WhatsApp.

Isso pode ser configurado como um Canva ou uma campanha, dependendo se você deseja que o usuário receba uma mensagem de confirmação no novo canal.

1. Crie uma campanha com o disparo de entrega baseada em ação de uma mensagem de entrada.
2. Crie uma campanha de webhook. Para ver um exemplo de webhook, consulte [Grupos de inscrições]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#update-subscription-status).

{% alert tip %}
Observe que você pode criar um URL ou código QR para entrar em um canal do [WhatsApp](https://business.facebook.com/wa/manage/phone-numbers/) no gerenciador do WhatsApp em **Número de telefone** > **Links de mensagens**.<br>![Criador do código QR do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Métodos de aceitação com base no Braze 

#### Envio de mensagens SMS

No Canva, configure uma campanha que pergunte aos clientes se eles desejam aceitar o recebimento de mensagens do WhatsApp usando um dos seguintes métodos:
- Segmento de clientes: grupo de marketing inscrito fora dos EUA
- Configuração de disparo de palavra-chave personalizada

Saiba como atualizar o status de inscrição dos perfis de usuário visualizando [Grupos de inscrições]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status).

#### Mensagem no app ou no navegador

Crie uma mensagem no app ou um pop-up no navegador solicitando que os clientes aceitem o uso do WhatsApp.

Use [a mensagem HTML no app](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal) com a ["ponte" JavaScript]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge) para fazer a interface com o SDK da Braze. Certifique-se de usar o ID do grupo de inscrições do WhatsApp. 

#### Formulário de captura de número de telefone

Use o modelo de [formulário de captura de número de telefone]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/) no editor de arrastar e soltar para mensagens no app para coletar números de telefone de usuários e aumentar seus grupos de inscrições do WhatsApp.

## Configure as aceitações para seu canal do WhatsApp da Braze

### Palavras-chave gerais de aceitação

É possível configurar uma campanha ou um canva que permita que os usuários que enviarem mensagens com palavras específicas aceitem o envio de mensagens futuras. Os canvas podem ser especialmente benéficos, pois permitem que você inclua uma mensagem de acompanhamento que confirma a aceitação bem-sucedida. 

#### Etapa 1: Crie um canva com um disparo de "Mensagem de entrada do WhatsApp"
 
![Etapa de entrada do Canva baseada em ação que insere os usuários que enviam uma mensagem de entrada do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

Ao selecionar disparadores de palavras-chave, inclua palavras como "Parar" ou "Nenhuma mensagem". Se você escolher esse método, certifique-se de que seus clientes conheçam as palavras de aceitação. Por exemplo, depois de receber a aceitação inicial, inclua uma resposta de acompanhamento como "Para optar por não receber essas mensagens, envie a mensagem "Parar" a qualquer momento". 

![Etapa da mensagem para enviar uma mensagem de entrada do WhatsApp em que o corpo da mensagem é "STOP" ou "NO MESSAGE".]({% image_buster /assets/img/whatsapp/whatsapp117.png %}){: style="max-width:85%;"}

#### Etapa 2: Atualizar o perfil do usuário

Atualize o perfil do usuário usando um dos métodos descritos em [Grupos de inscrições]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status).

### Seleção de aceitação de marketing

No criador de modelos de mensagens do WhatsApp, você pode incluir a opção "aceitação de marketing". Sempre que incluir isso, certifique-se de que o modelo seja usado em um Canva com uma etapa subsequente para uma alteração no grupo de inscrições. 

1. Crie um modelo de mensagem com a resposta rápida "aceitação de marketing".<br>![Modelo de mensagem com uma opção de rodapé de "Aceitação de marketing"]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>![Seção para configurar um botão de opt-out de marketing.]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. Crie um Canva que use esse modelo de mensagem.<br><br>
3. Siga as etapas do exemplo anterior, mas com o texto do disparador "STOP PROMOTIONS".<br><br>
4. Atualize o status da inscrição do usuário usando um dos métodos descritos em [Grupos de inscrições]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status).

## Configurar fluxos de trabalho de aceitação e exclusão

Você pode configurar fluxos de trabalho de resposta de palavras-chave "START" e "STOP" para o WhatsApp com esses dois métodos:

- [Etapa de atualização do usuário](#user-update-step)
- [Campanha de webhook para disparar uma segunda campanha do WhatsApp](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### Etapa de atualização do usuário

A [etapa Atualização do usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) pode adicionar o número de telefone do usuário ao grupo de inscrições do WhatsApp quando o usuário envia uma palavra-chave para o número de telefone do grupo de inscrições.

A etapa de atualização do usuário evita condições de corrida porque o usuário não passará para a próxima etapa do canva antes que seu número de telefone seja adicionado ao grupo de inscrições. Ele também tem menos etapas para configurar do que os outros métodos, portanto a Braze geralmente recomenda esse método.

1. Crie um Canvas com a etapa baseada em ação **Enviar uma mensagem de entrada do WhatsApp**. Selecione **Onde o corpo da mensagem** e digite "START" para **Is**.

{% alert important %}
Para mensagens "STOP", inverta a etapa da mensagem que confirma a aceitação e a etapa de atualização do usuário. Caso contrário, o usuário será excluído do grupo de inscrições primeiro e, depois, não será elegível para receber a mensagem de confirmação.
{% endalert %}

![Etapa de uma mensagem do WhatsApp em que o corpo da mensagem é "START".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. No Canva, crie uma etapa do tipo **Configurar atualização do usuário** e, para **Ação**, selecione **Advanced JSON Editor**. <br><br>![Etapa de atualização do usuário com uma ação de "Advanced JSON Editor".]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
3\. Preencha o **objeto User Update** com a seguinte carga útil JSON, substituindo `XXXXXXXXXXX` pelo ID do seu grupo de inscrições:

{% raw %}
```json
{
    "attributes": [
        {
            "subscription_groups": [
                {
                    "subscription_group_id": "XXXXXXXXXXX",
                    "subscription_state": "subscribed"
                }
            ]
        }
    ]
}
```
{% endraw %}

{: start="4"}
4\. Adicione uma etapa subsequente da mensagem do WhatsApp. <br><br>![Etapa de atualização do usuário em um Canvas.]({% image_buster /assets/img/whatsapp/message_step.png %}){: style="max-width:25%;"}

#### Considerações

A atualização pode ser concluída em velocidades variáveis porque o Braze agrupa as solicitações da [etapa de atualização do usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/).

### Campanha de webhook para disparar uma segunda campanha do WhatsApp

Uma campanha Webhook pode disparar a entrada em uma segunda campanha depois de adicionar o número de telefone do usuário ao grupo de inscrições do WhatsApp quando o usuário envia uma palavra-chave para o número de telefone do grupo de inscrições.

{% alert important %}
Não é necessário usar esse método para mensagens STOP. A mensagem de confirmação será enviada antes que o usuário seja removido do grupo de inscrições, portanto, você pode usar uma das outras duas etapas.
{% endalert %}

1. Crie uma campanha ou um Canva com uma etapa baseada em ação **Envie uma mensagem de entrada do WhatsApp**. Selecione **Onde o corpo da mensagem** e digite "START" para **Is**.

![Etapa do envio de mensagens do WhatsApp em que o corpo da mensagem é "START".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

{: start="2"}
2\. Na campanha ou no Canva, crie uma etapa do Webhook Message e altere o **Request Body (Corpo da solicitação)** para **Raw Text (Texto bruto)**.

![Etapa da mensagem para um webhook.]({% image_buster /assets/img/whatsapp/webhook_step.png %}){: style="max-width:85%;"}

{: start="3"}
3\. Digite o [URL do endpoint]({{site.baseurl}}/api/basics/) do cliente no **URL do Webhook**, seguido pelo link do endpoint `campaigns/trigger/send`. Por exemplo, `https://dashboard-02.braze.eu/campaigns/trigger/send`.

![Campo URL do webhook na seção "Criador de webhook".]({% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %}){: style="max-width:70%;"}

{: start="4"}
4\. No texto bruto, insira a seguinte carga útil JSON e substitua `XXXXXXXXXXX` pelo ID do seu grupo de inscrições. Você precisará substituir o endereço `campaign_id` depois de criar sua segunda campanha.

{% raw %}
```json
{
    "campaign_id": "XXXXXXXXXXX",
    "recipients": [
        {
            "external_user_id": "{{${user_id}}}",
            "attributes": {
                "subscription_groups": [
                    {
                        "subscription_group_id": "XXXXXXXXXXX",
                        "subscription_state": "subscribed"
                    }
                ]
            }
        }
    ]
}
```
{% endraw %}

{: start="5"}
5\. Crie uma campanha do WhatsApp (sua segunda campanha) e defina o disparo como API. Copie esse endereço `campaign_id` na carga útil JSON de sua primeira campanha.

#### Considerações

- Ainda não há suporte para atualizações de atribuições na carga útil JSON do acionador da API do Canvas, portanto, você só pode disparar uma campanha do WhatsApp para a mensagem de resposta do WhatsApp (como na etapa 2).
- Um modelo do WhatsApp deve ser aprovado para ser enviado como uma mensagem de resposta. Isso ocorre porque uma resposta rápida exige que o disparo da mensagem de entrada esteja dentro da mesma campanha ou Canva. Se você usar uma [Etapa de atualização do usuário](#user-update-step), poderá enviar uma mensagem de resposta rápida sem a aprovação da Meta.

## Entendendo a diferença entre os modificadores "regex" e "is"

Nesta tabela, `STOP` é usado como um exemplo de palavra disparadora para demonstrar como os modificadores funcionam.

| Modificador | Palavra disparadora | Ação |
| --- | --- | --- |
| `Is` | `STOP` | Captura qualquer uso de palavra inteira de "stop", independentemente do caso. Por exemplo, isso captura "stop", mas não "please stop". |
| `Matches regex` | `STOP` | Captura qualquer uso de "STOP" nesse caso. Por exemplo, isso captura "stop" (pare), mas não "PLEASE STOP" (por favor, pare). |
| `Matches regex` | `(?i)STOP(?-i)` | Captura qualquer uso de "STOP" em qualquer caso. Por exemplo, isso captura "stop" (pare), "please stop" (por favor, pare) e "never stop sending me messages" (nunca pare de me enviar mensagens). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

