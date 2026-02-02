---
nav_title: WhatsApp e sistema externo
article_title: Integre Braze e WhatsApp com um sistema externo
page_order: 2
description: "Este artigo de referência fornece um guia passo a passo para integrar a integração do Braze e WhatsApp com um sistema externo de IA ou de comunicação."
page_type: reference
alias: /whatsapp_external_system_integration/
channel:
  - WhatsApp
---

# Integre Braze e WhatsApp com um sistema externo de IA ou de comunicação

> Aproveite o poder dos chatbots de IA e das transferências para agentes humanos no canal do WhatsApp para otimizar suas operações de suporte ao cliente. Ao automatizar consultas rotineiras e transitar perfeitamente para agentes humanos quando necessário, você pode melhorar significativamente os tempos de resposta e aprimorar a experiência geral do cliente.

## Como funciona?

A integração entre Braze e o sistema externo de IA ou de comunicação funciona como uma via de mão dupla, onde Braze é o canal de comunicação e o sistema externo é a "inteligência" que processa mensagens e formula respostas.

O fluxo de trabalho de integração pode ser dividido em dois fluxos principais:
**Fluxo de entrada:** A mensagem de um usuário chega ao Braze e é então encaminhada para o seu sistema externo para processamento.
**Fluxo de saída:** Após processar a mensagem, seu sistema externo envia uma resposta ao Braze, que então entrega a mensagem ao usuário final.

Para automatizar eficientemente essa comunicação, esta integração utiliza duas funcionalidades principais do Braze: [campanhas de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) e [campanhas acionadas por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).

![Arquitetura da integração entre o canal WhatsApp do Braze e um sistema externo.]({% image_buster /assets/img/whatsapp/external_system_architecture.png %})
<sup>*Arquitetura da integração entre o canal WhatsApp do Braze e um sistema externo.*</sup>

## Pré-requisitos

| Pré-requisito | Descrição |
| - | - |
| Sistema externo | Um sistema de IA ou de comunicação de terceiros capaz de construir e gerenciar chatbots, sistemas de atendimento ao cliente automatizados usando APIs, ou ambos. |
| Integração Braze e WhatsApp | Um número do WhatsApp gerenciado pelo Braze |
| Chave da API REST do Braze | Uma chave da API REST com `campaigns.trigger.send` permissões. Isso pode ser criado no dashboard do Braze indo para **Configurações** > **Chaves da API**. |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

## Configuração da integração

### Etapa 1: Crie uma campanha de webhook para mensagens recebidas.

Primeiro, crie uma campanha de webhook para estabelecer uma forma de enviar mensagens do WhatsApp recebidas pelo Braze para seu sistema externo.

1. No Braze, crie uma campanha de webhook.
2. No criador de webhook, selecione **Compor webhook**.
3. No campo **URL do Webhook**, insira o endpoint da API (URL) para o sistema externo que receberá a mensagem.
4. Selecione **Texto bruto** para o corpo da solicitação e insira uma carga útil com personalização que contenha o `external_id` do usuário e o número de telefone, o conteúdo da mensagem e outras informações relevantes, como:

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
5\. Na etapa **Agendar Entrega** do seu criador de campanha, selecione **Baseada em Ação** para o tipo de entrega e **Enviar uma mensagem recebida do WhatsApp** para o gatilho da campanha.

![Entrega baseada em ação com um gatilho de envio de uma mensagem recebida do WhatsApp.]({% image_buster /assets/img/whatsapp/inbound_message_trigger.png %})

{: start="6"}
6\. Finalize a composição da sua campanha, depois salve e lance a campanha. Após lançar a campanha, toda vez que uma mensagem for recebida, o Braze envia um webhook para seu sistema externo.

### Etapa 2: Crie uma campanha acionada por API para mensagens enviadas {#step-2}.

Em seguida, crie uma campanha acionada por API para estabelecer uma forma de seu sistema externo enviar mensagens de volta para os usuários através do WhatsApp.

1. No Braze, crie uma campanha do WhatsApp. 
2. No criador de mensagens, selecione **Mensagem de Modelo do WhatsApp** ou **Mensagem de Resposta**, depois selecione o modelo ou layout da mensagem de resposta. Você pode selecionar qualquer layout de mensagem de resposta porque a mensagem recebida abriu a janela de 24 horas do WhatsApp.

![Criador de mensagens com opções para selecionar o tipo de mensagem e o layout da mensagem.]({% image_buster /assets/img/whatsapp/response_message_layout.png %})

{: start="3"}
3\. Adicione a propriedade de gatilho da API ao corpo da mensagem, como {% raw %}```{{api_trigger_properties.${external_system_msg+body}}}```{% endraw %}. Isso permite que seu sistema de IA preencha a mensagem que será enviada.

![Criador de mensagem com corpo de mensagem que contém propriedades de disparo.]({% image_buster /assets/img/whatsapp/api_trigger_properties.png %})

{: start="4"}
4\. Na etapa **Agendar Entrega** do criador de campanha, selecione **Ação Baseada** para o tipo de entrega.
5\. Salve a campanha, depois anote a `campaign_id` única que a Braze gera para esta campanha. Você precisará do ID para a próxima etapa.

### Etapa 3: Conecte o sistema externo à campanha disparada pela API.

Por último, configure seu sistema externo para chamar a Braze e enviar a resposta.

1. No código do seu sistema externo, após processar a mensagem recebida e gerar a resposta, faça uma solicitação POST para o endpoint `/messages/send` da Braze.
2. No corpo da solicitação `/messages/send`, inclua a `campaign_id` de [Etapa 2](#step-2), o `external_id` do usuário e o conteúdo da resposta do sistema externo.
3. Use a propriedade de disparo da API de [Etapa 2](#step-2) para inserir a resposta do sistema externo, e não se esqueça de incluir sua chave de API no cabeçalho da solicitação para autenticação, como neste exemplo de cURL:

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

Agora você tem uma base sólida para construir um fluxo de trabalho de chatbot de IA!

### Personalizando seu fluxo de trabalho

Você pode expandir sua lógica de integração para:
- Usar palavras-chave diferentes para disparar campanhas de webhook distintas.
- Criar fluxos de conversa mais complexos com campanhas disparadas pela API de múltiplas etapas.
- Registrar informações de chat na Braze como atributos personalizados para enriquecer o perfil do usuário e segmentar campanhas futuras.
