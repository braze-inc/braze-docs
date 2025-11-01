---
nav_title: Opt-ins e opt-outs
article_title: Opção de inclusão e exclusão do WhatsApp
description: "Este artigo de referência aborda diferentes métodos de ativação e desativação do WhatsApp."
page_type: partner
search_tag: Partner
page_order: 5
channel:
  - WhatsApp
alias: /user_guide/message_building_by_channel/whatsapp/opt-ins_and_opt-outs/
---

# Opt-in e opt-out

> O manuseio de opt-ins e opt-outs do WhatsApp é crucial, pois o WhatsApp monitora [a classificação de qualidade do](https://www.facebook.com/business/help/896873687365001) seu [número de telefone](https://www.facebook.com/business/help/896873687365001), e classificações baixas podem resultar na redução dos limites de mensagens. <br><br>Uma maneira de criar uma classificação de alta qualidade é impedir que os usuários bloqueiem ou denunciem sua empresa. Isso pode ser feito fornecendo [mensagens de alta qualidade](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits) (como valor para seus usuários), controlando a frequência das mensagens e permitindo que os clientes optem por não receber comunicações futuras. <br><br>Esta página aborda como configurar opt-ins e opt-outs e as diferenças entre os modificadores "regex" e "is".

Os opt-ins podem vir de fontes externas ou de métodos do Braze, como SMS ou mensagens no aplicativo e no navegador. As recusas podem ser tratadas usando palavras-chave definidas no Braze e botões de marketing do WhatsApp. Consulte os métodos a seguir para obter orientação sobre a configuração de opt-ins e opt-outs.

#### Métodos de opt-in
- [Métodos de opt-in externos ao Braze](#external-to-braze-opt-in-methods)
  - [Lista de opt-in criada externamente](#externally-built-opt-in-list)
  - [Mensagem de saída no canal WhatsApp de suporte ao cliente](#outbound-message-in-customer-support-whatsapp-channel)
  - [Mensagem de entrada do WhatsApp](#inbound-whatsapp-message)
- [Métodos de opt-in com tecnologia Braze](#braze-powered-opt-in-methods)

#### Métodos de exclusão
- [Palavras-chave gerais de opt-out](#general-opt-out-keywords)
- [Seleção de opt-out de marketing](#marketing-opt-out-selection)

## Configurar opt-ins para seu canal do Braze WhatsApp

Para opt-ins do WhatsApp, você deve cumprir os [requisitos do WhatsApp](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Você também precisará fornecer ao Braze as seguintes informações:
- Um `external_id`, um [número de telefone]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) e um status de assinatura atualizado para cada usuário. Isso pode ser feito usando o [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/) ou por meio do [ponto de extremidade`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para atualizar o número de telefone e o status da assinatura.

{% alert note %}
O Braze lançou um aprimoramento no endpoint `/users/track` que permite atualizações no status da assinatura que você pode conhecer em [Grupos de assinaturas]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status). No entanto, se você já tiver criado protocolos opt-in usando o [ponto de extremidade`/v2/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/), poderá continuar a fazê-lo lá.
{% endalert %}

### Métodos de opt-in externos ao Braze

Seu aplicativo ou site (registro de conta, página de checkout, configurações de conta, terminal de cartão de crédito) para a Braze.

Sempre que já tiver consentimento de marketing para e-mail ou mensagens de texto, inclua uma seção adicional para o WhatsApp. Depois que um usuário opta por participar, ele precisa de um `external_id`, um [número de telefone]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) e um status de assinatura atualizado. Para fazer isso, dependendo de como sua instalação do Braze estiver configurada, aproveite o [endpoint`/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) ou use o [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/).

#### Lista de opt-in criada externamente

Se você já usou o WhatsApp anteriormente, talvez já tenha criado uma lista de usuários com opt-ins de acordo com os requisitos do WhatsApp. Nesse caso, carregue um CSV ou use a API com as [seguintes informações]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv) no Braze.

#### Mensagem de saída no canal WhatsApp de suporte ao cliente

Em seu canal de suporte ao cliente, acompanhe os problemas resolvidos com uma mensagem automática perguntando se eles querem optar por receber mensagens de marketing. A funcionalidade aqui depende da disponibilidade de recursos na ferramenta de suporte ao cliente de sua escolha e de onde você mantém as informações do usuário.

1. Forneça um [link de mensagem](https://business.facebook.com/business/help/890732351439459?ref=search_new_0) do seu número de telefone do WhatsApp Business.
2. Fornecer [ações de resposta rápida]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/#quick-replies) em que o cliente responde "Sim" para indicar a adesão
3. Configure o acionador de palavras-chave personalizado.
4. Para qualquer uma dessas ideias, você provavelmente precisará terminar o caminho com o seguinte:
	- Chame o [endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para atualizar ou criar um usuário
	- Aproveite o [endpoint`/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) ou use o [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)

#### Mensagem de entrada do WhatsApp 

Faça com que os clientes enviem uma mensagem de entrada para o número do WhatsApp.

Isso pode ser configurado como um Canvas ou uma campanha, dependendo se você deseja que o usuário receba uma mensagem de confirmação no novo canal.

1. Crie uma campanha com o acionador de entrega baseado em ação de uma mensagem de entrada.
2. Crie uma campanha de webhook. Para obter um exemplo de webhook, consulte [Grupos de assinatura]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#update-subscription-status).

{% alert tip %}
Observe que você pode criar um URL ou código QR para entrar em um canal do WhatsApp no [gerenciador do WhatsApp](https://business.facebook.com/wa/manage/phone-numbers/) em **Phone Number** > **Message Links (** **Número de telefone** > **Links de mensagens**).<br>\![Compositor de código QR do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Métodos de opt-in com tecnologia Braze 

#### Mensagem SMS

No Canvas, configure uma campanha que pergunte aos clientes se eles querem optar por receber mensagens do WhatsApp usando um dos seguintes métodos:
- Segmento de clientes: grupo de marketing inscrito fora dos EUA
- Configuração do acionador de palavra-chave personalizado

Saiba como atualizar o status de assinatura dos perfis de usuário visualizando [Grupos de assinatura]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status).

#### Mensagem no aplicativo ou no navegador

Crie uma mensagem no aplicativo ou um pop-up no navegador solicitando que os clientes optem pelo uso do WhatsApp.

Use [a mensagem HTML no aplicativo](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal) com a ["ponte" JavaScript]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge) para fazer a interface com o Braze SDK. Certifique-se de usar o ID do grupo de assinatura do WhatsApp. 

#### Formulário de captura de número de telefone

Use o modelo de [formulário de captura de número de telefone]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/) no editor de arrastar e soltar para mensagens no aplicativo para coletar números de telefone de usuários e aumentar seus grupos de assinatura do WhatsApp.

## Configure as opções de exclusão para seu canal do Braze WhatsApp

### Palavras-chave gerais de opt-out

Você pode configurar uma campanha ou um Canvas que permita que os usuários que enviarem mensagens com palavras específicas optem por não receber mensagens futuras. As telas podem ser especialmente benéficas, pois permitem que você inclua uma mensagem de acompanhamento que confirme o cancelamento bem-sucedido. 

#### Etapa 1: Criar um Canvas com um acionador de "Mensagem de entrada do WhatsApp"
 
Etapa de entrada do Canvas baseada em ação que insere os usuários que enviam uma mensagem de entrada do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

Ao selecionar acionadores de palavras-chave, inclua palavras como "Parar" ou "Nenhuma mensagem". Se você optar por esse método, certifique-se de que seus clientes conheçam as palavras de cancelamento. Por exemplo, depois de receber o opt-in inicial, inclua uma resposta de acompanhamento como "Para optar por não receber essas mensagens, envie a mensagem "Stop" a qualquer momento". 

\![Etapa da mensagem para enviar uma mensagem de entrada do WhatsApp em que o corpo da mensagem seja "STOP" ou "NO MESSAGE".]({% image_buster /assets/img/whatsapp/whatsapp117.png %}){: style="max-width:85%;"}

#### Etapa 2: Atualizar o perfil do usuário

Atualize o perfil do usuário usando um dos métodos descritos em [Grupos de assinatura]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status).

### Seleção de opt-out de marketing

No criador de modelos de mensagens do WhatsApp, você pode incluir a opção "opt-out de marketing". Sempre que você incluir isso, certifique-se de que o modelo seja usado em um Canvas com uma etapa subsequente para uma alteração no grupo de assinaturas. 

1. Crie um modelo de mensagem com a resposta rápida "opt-out de marketing".<br>Modelo de mensagem com uma opção de rodapé de "Marketing opt-out"]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>Seção para configurar um botão de saída de marketing.]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. Crie um Canvas que use esse modelo de mensagem.<br><br>
3. Siga as etapas do exemplo anterior, mas com o texto do acionador "STOP PROMOTIONS".<br><br>
4. Atualize o status da assinatura do usuário usando um dos métodos descritos em [Grupos de assinatura]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status).

## Configurar fluxos de trabalho de opt-in e opt-out

Você pode configurar fluxos de trabalho de resposta de palavras-chave "START" e "STOP" para o WhatsApp com esses dois métodos:

- [Etapa de atualização do usuário](#user-update-step)
- [Campanha de webhook para acionar uma segunda campanha do WhatsApp](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### Etapa de atualização do usuário

A [etapa Atualização do usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) pode adicionar o número de telefone do usuário ao grupo de assinatura do WhatsApp quando o usuário envia uma palavra-chave para o número de telefone do grupo de assinatura.

A etapa de atualização do usuário evita condições de corrida porque o usuário não passará para a próxima etapa do Canvas antes que seu número de telefone seja adicionado ao grupo de assinatura. Ele também tem menos etapas de configuração do que os outros métodos, por isso a Braze geralmente recomenda esse método.

1. Crie um Canvas com a etapa baseada em ação **Enviar uma mensagem de entrada do WhatsApp**. Selecione **Onde o corpo da mensagem** e digite "START" para **Is**.

{% alert important %}
Para mensagens "STOP", inverta a etapa da mensagem que confirma a desativação e a etapa de atualização do usuário. Caso contrário, o usuário será excluído do grupo de assinatura primeiro e, depois, não estará qualificado para receber a mensagem de confirmação.
{% endalert %}

Uma etapa da mensagem do WhatsApp em que o corpo da mensagem é "START".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. No Canvas, crie uma etapa **Set Up User Update** e, para **Action**, selecione **Advanced JSON Editor**. <br><br>Etapa de atualização do usuário com uma ação de "Advanced JSON Editor".]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
3\. Preencha o **objeto User Update** com o seguinte payload JSON, substituindo `XXXXXXXXXXX` pelo ID do seu grupo de assinatura:

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
4\. Adicione uma etapa subsequente da mensagem do WhatsApp. <br><br>Etapa de atualização do usuário em um Canvas.]({% image_buster /assets/img/whatsapp/message_step.png %}){: style="max-width:25%;"}

#### Considerações

A atualização pode ser concluída em velocidades variáveis porque o Braze agrupa as solicitações da [etapa de atualização do usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/).

### Campanha de webhook para acionar uma segunda campanha do WhatsApp

Uma campanha de webhook pode acionar a entrada em uma segunda campanha depois de adicionar o número de telefone do usuário ao grupo de assinatura do WhatsApp quando o usuário envia uma palavra-chave para o número de telefone do grupo de assinatura.

{% alert important %}
Não é necessário usar esse método para mensagens STOP. A mensagem de confirmação será enviada antes que o usuário seja removido do grupo de assinatura, portanto, você pode usar uma das outras duas etapas.
{% endalert %}

1. Crie uma campanha ou Canvas com uma etapa baseada em ação **Envie uma mensagem de entrada do WhatsApp**. Selecione **Onde o corpo da mensagem** e digite "START" para **Is**.

\![Etapa da mensagem do WhatsApp em que o corpo da mensagem é "START".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

{: start="2"}
2\. Na campanha ou no Canvas, crie uma etapa de Mensagem de webhook e altere o **Corpo da solicitação** para **Texto bruto**.

\![Etapa da mensagem para um webhook.]({% image_buster /assets/img/whatsapp/webhook_step.png %}){: style="max-width:85%;"}

{: start="3"}
3\. Digite o [URL do endpoint]({{site.baseurl}}/api/basics/) do cliente no **URL do Webhook**, seguido pelo link do endpoint `campaigns/trigger/send`. Por exemplo, `https://dashboard-02.braze.eu/campaigns/trigger/send`.

Campo URL do webhook na seção "Compose Webhook".]({% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %}){: style="max-width:70%;"}

{: start="4"}
4\. No texto bruto, insira a seguinte carga útil JSON e substitua `XXXXXXXXXXX` pela ID do seu grupo de assinatura. Você precisará substituir o endereço `campaign_id` depois de criar sua segunda campanha.

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
5\. Crie uma campanha do WhatsApp (sua segunda campanha) e defina o acionador como API. Certifique-se de copiar esse endereço `campaign_id` na carga útil JSON de sua primeira campanha.

#### Considerações

- Ainda não há suporte para atualizações de atributos na carga útil JSON do acionador da API do Canvas, portanto, você só pode acionar uma campanha do WhatsApp para a mensagem de resposta do WhatsApp (como na etapa 2).
- Um modelo do WhatsApp deve ser aprovado para ser enviado como uma mensagem de resposta. Isso ocorre porque uma resposta rápida exige que o acionador da mensagem de entrada esteja dentro da mesma campanha ou Canvas. Se você usar uma [etapa de atualização do usuário](#user-update-step), poderá enviar uma mensagem de resposta rápida sem a aprovação do Meta.

## Entendendo a diferença entre os modificadores "regex" e "is"

Nessa tabela, `STOP` é usado como um exemplo de palavra acionadora para demonstrar como os modificadores funcionam.

| Modificador | Palavra de gatilho | Ação |
| --- | --- | --- |
| `Is` | `STOP` | Captura qualquer uso de palavra inteira de "stop", independentemente do caso. Por exemplo, isso captura "stop", mas não "please stop". |
| `Matches regex` | `STOP` | Captura qualquer uso de "STOP" nesse exato caso. Por exemplo, isso captura "STOP" e "PLEASE STOP", mas não "stop". |
| `Matches regex` | `(?i)STOP(?-i)` | Captura qualquer uso de "STOP" em qualquer caso. Por exemplo, isso captura "stop", "please stop" e "never stop sending me messages". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

