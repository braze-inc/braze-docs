---
nav_title: WhatsApp e sistema externo
article_title: Integração do Braze e do WhatsApp com um sistema externo
page_order: 2
description: "Este artigo de referência fornece um guia passo a passo para integrar a integração do Braze e do WhatsApp com um sistema externo de IA ou de comunicação."
page_type: reference
alias: /whatsapp_external_system_integration/
channel:
  - WhatsApp
---

# Integração do Braze e do WhatsApp com um sistema externo de IA ou de comunicação

> Aproveite o poder dos chatbots com IA e das transferências de agentes ao vivo no canal do WhatsApp para otimizar suas operações de suporte ao cliente. Ao automatizar as consultas de rotina e fazer a transição perfeita para agentes humanos quando necessário, você pode melhorar significativamente os tempos de resposta e aprimorar a experiência geral do cliente.

## Como funciona

A integração entre o Braze e a IA externa ou o sistema de comunicação funciona como uma via de mão dupla, em que o Braze é o canal de comunicação e o sistema externo é a "inteligência" que processa as mensagens e formula as respostas.

O fluxo de trabalho de integração pode ser dividido em dois fluxos principais:
**Fluxo de entrada:** A mensagem de um usuário chega ao Braze e é encaminhada ao seu sistema externo para processamento.
**Fluxo de saída:** Depois de processar a mensagem, seu sistema externo envia uma resposta ao Braze, que, por sua vez, entrega a mensagem ao usuário final.

Para automatizar essa comunicação de forma eficiente, essa integração usa dois recursos importantes do Braze: [campanhas de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) e [campanhas acionadas por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).

Arquitetura da integração entre o canal Braze WhatsApp e um sistema externo.]({% image_buster /assets/img/whatsapp/external_system_architecture.png %})
<sup>*Arquitetura da integração entre o canal Braze WhatsApp e um sistema externo.*</sup>

## Pré-requisitos

| Pré-requisito
| - | - |
| Sistema externo: um sistema de comunicação ou IA de terceiros capaz de criar e gerenciar chatbots, sistemas automatizados de atendimento ao cliente usando APIs ou ambos. |
| Integração entre a Braze e o WhatsApp
| Braze REST API Key | Uma chave REST API com permissões `campaigns.trigger.send`. Isso pode ser criado no painel de controle do Braze, acessando **Configurações** > **Chaves de API**. |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

## Configuração da integração

### Etapa 1: Criar uma campanha de webhook para mensagens de entrada

Primeiro, crie uma campanha de webhook para estabelecer uma maneira de enviar mensagens do WhatsApp recebidas pelo Braze para seu sistema externo.

1. No Braze, crie uma campanha de webhook.
2. No compositor de webhook, selecione **Compose webhook**.
3. No campo **URL do webhook**, digite o endpoint da API (URL) do sistema externo que receberá a mensagem.
4. Selecione **Raw text** para o corpo da solicitação e insira uma carga útil com personalização que contenha o endereço `external_id` e o número de telefone do usuário, o conteúdo da mensagem e outras informações relevantes, como

{% raw %}
```liquid
{
  "user_id": "{{${user_id}}}",
  "phone_number": "{{${phone_number}}}",
  "message": "{{whats_app.${inbound_message_body}}}"
}
```
{% endraw %}

{: start="5"}
5\. Na etapa **Agendar entrega** do compositor de sua campanha, selecione **Baseado em ação** para o tipo de entrega e **Enviar uma mensagem de entrada do WhatsApp** para o acionador da campanha.

Entrega baseada em ação com um gatilho de envio de uma mensagem de entrada do WhatsApp.]({% image_buster /assets/img/whatsapp/inbound_message_trigger.png %})

{: start="6"}
6\. Conclua a composição de sua campanha, salve e inicie a campanha. Agora, toda vez que uma mensagem for recebida, o Braze enviará um webhook para seu sistema externo.

### Etapa 2: Criar uma campanha acionada por API para mensagens de saída {#step-2}

Em seguida, crie uma campanha acionada por API para estabelecer uma maneira de seu sistema externo enviar mensagens de volta aos usuários por meio do WhatsApp.

1. No Braze, crie uma campanha do WhatsApp. 
2. No compositor de mensagens, selecione **WhatsApp Template Message** ou **Response Message** e, em seguida, selecione o layout do modelo ou da mensagem de resposta. Você pode selecionar qualquer layout de mensagem de resposta porque a mensagem recebida abriu a janela do WhatsApp 24 horas.

Compositor de mensagens com opções para selecionar o tipo de mensagem e o layout da mensagem.]({% image_buster /assets/img/whatsapp/response_message_layout.png %})

{: start="3"}
3\. Adicione a propriedade do acionador da API ao corpo da mensagem, como {% raw %}```{{api_trigger_properties.${external_system_msg+body}}}```{% endraw %}. Isso permite que seu sistema de IA preencha a mensagem que será enviada.

Compositor de mensagem com corpo de mensagem que contém propriedades de acionamento.]({% image_buster /assets/img/whatsapp/api_trigger_properties.png %})

{: start="4"}
4\. Na etapa **Agendar entrega** do compositor de sua campanha, selecione **Baseado em ação** para o tipo de entrega.
5\. Salve a campanha e anote o endereço eletrônico `campaign_id` exclusivo que o Braze gera para essa campanha. Você precisará do ID para a próxima etapa.

### Etapa 3: Conecte o sistema externo à campanha acionada pela API

Por fim, configure seu sistema externo para chamar o Braze e enviar a resposta.

1. No código de seu sistema externo, após processar a mensagem recebida e gerar a resposta, faça uma solicitação POST para o endpoint do Braze `/messages/send`.
2. No corpo da solicitação `/messages/send`, inclua o `campaign_id` da [Etapa 2](#step-2), o `external_id` do usuário e o conteúdo da resposta do sistema externo.
3. Use a propriedade de acionador de API da [Etapa 2](#step-2) para inserir a resposta do sistema externo e não se esqueça de incluir sua chave de API no cabeçalho da solicitação para autenticação, como neste exemplo de cURL:

{% raw %}
```json
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer a valid rest API key' \
  -d '{
    "campaign_id": "campaign_id",
    "recipients": [
      {
        "external_user_id": "external_id",
        "trigger_properties": {
          "external_system_msg_body": "your external system message"         
        }
      }
    ]
  }' \
  {{Braze endpoint}}/campaigns/trigger/send
```
{% endraw %}

Agora você tem uma base sólida para criar um fluxo de trabalho de chatbot de IA!

### Personalizar seu fluxo de trabalho

Você pode expandir sua lógica de integração para:
- Use palavras-chave diferentes para acionar campanhas de webhook distintas.
- Crie fluxos de conversação mais complexos com campanhas acionadas por API em várias etapas.
- Registre informações de bate-papo no Braze como atributos personalizados para enriquecer o perfil do usuário e segmentar campanhas futuras.
