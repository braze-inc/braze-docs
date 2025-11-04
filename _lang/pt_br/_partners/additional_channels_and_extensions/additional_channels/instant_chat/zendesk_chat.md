---
nav_title: Zendesk
article_title: Zendesk Chat
description: "Saiba como integrar o Zendesk Chat ao Braze e configurar uma conversa bidirecional por SMS."
alias: /partners/zendesk_chat/
page_type: partner
search_tag: Partner

---

# Zendesk Chat

> O [Zendesk Chat](https://www.zendesk.com/service/messaging/) usa webhooks de cada plataforma para configurar uma conversa bidirecional por SMS. Quando um usuário solicita suporte, um ticket é criado no Zendesk. As respostas dos agentes são encaminhadas ao Braze por meio de uma campanha de SMS disparada pela API, e as respostas dos usuários são enviadas de volta ao Zendesk.

## Pré-requisitos


| Pré-requisito | Descrição |
|---|---|
| Uma conta do Zendesk | É necessário ter uma conta da Zendesk para aproveitar essa parceria.|
| Um token de autorização básica do Zendesk | Um token de autorização básica do Zendesk será usado para fazer uma solicitação de webhook de saída do Braze para o Zendesk.|
| Uma chave da API REST do Braze  | Uma chave da API REST da Braze com permissões `campaigns.trigger.send`. Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**.|

## Casos de uso

Aumente a eficiência do suporte ao cliente combinando os recursos do Braze SMS com as respostas dos agentes em tempo real da Zendesk para atender prontamente às consultas dos usuários com suporte humano.

## Integração do Zendesk Chat

### Etapa 1: Criar um webhook no Zendesk

1. No console de desenvolvedor do Zendesk, acesse webhooks: {% raw %}`https://{{url}}.zendesk.com/admin/apps-integrations/webhooks/webhooks`{% endraw %}
2. Em **Create Webhook**, selecione **Trigger ou automação**.
3. Para o **URL do endpoint**, adicione o endpoint **/campaign/trigger/send**.
4. Em **Authentication (Autenticação**), selecione **Bearer token (Token do portador)** e adicione a chave da API REST do Braze com as permissões `campaigns.trigger.send`.

![Um exemplo de webhook do Zendesk.]({% image_buster /assets/img/zendesk/instant_chat/chat1.png %}){: style="max-width:70%;"}

### Etapa 2: Criar uma campanha de SMS de saída

Em seguida, você criará uma campanha de SMS que ouvirá webhooks do Zendesk e enviará uma resposta de SMS personalizada para seus clientes.

#### Etapa 2.1: Crie sua mensagem

Quando o Zendesk envia o conteúdo de uma mensagem por meio da API, ele vem no seguinte formato:

```
**----------------------------------------------\n\n{Replier Name}, {Replier Date}\n\n{Message}**
```

Portanto, precisamos extrair os detalhes que desejamos dessa string para exibir na mensagem, caso contrário, o usuário verá todos os detalhes.

![Um exemplo de SMS sem formatação.]({% image_buster /assets/img/zendesk/instant_chat/chat2.png %}){: style="max-width:40%;"}

Na caixa de texto **Mensagem**, adicione o seguinte código Liquid e qualquer linguagem de aceitação ou outro conteúdo estático:

{% raw %}
```liquid
{% assign body = {{api_trigger_properties.${msg_body}}} %}
{% assign msg = body | split: "
" %}
New message from Zendesk: 
{{msg[2]}}
 
Feel free to respond directly to this number!
```
{% endraw %}

![Um exemplo de SMS com formatação.]({% image_buster /assets/img/zendesk/instant_chat/chat3.png %}){: style="max-width:70%;"}

#### Etapa 2.2: Agendar a entrega

Para o tipo de entrega, selecione **API-Triggered delivery** e, em seguida, copie o Campaign ID que será usado nas próximas etapas.

![Entrega disparada pela API]({% image_buster /assets/img/zendesk/instant_chat/chat4.png %}){: style="max-width:70%;"}

Por fim, em **Controles de entrega**, ative a reelegibilidade.

![Reelegibilidade ativada em "Controles de entrega".]({% image_buster /assets/img/zendesk/instant_chat/chat5.png %})

### Etapa 3: Criar um disparo no Zendesk para encaminhar as respostas do agente para o Braze

Acesse **Objetos e regras** > **Regras de negócios** > **Acionadores**.

1. Crie uma nova **categoria** (por exemplo, **Disparar uma mensagem**).
2. Crie um novo **disparador** (por exemplo, **Responder via SMS Braze**).
3. Em **Condições**, selecione:
- **Ticket>Comment** está **presente e o solicitante pode ver o comentário** para que a mensagem seja disparada sempre que um novo comentário público for incluído em uma atualização de tickets
- **Ticket>Update** *não é um* **serviço da Internet (API)**, de modo que, quando um usuário envia uma mensagem pelo Braze, ela não é encaminhada de volta para o telefone celular. Somente as mensagens provenientes do Zendesk serão encaminhadas.

![Responda via SMS Braze.]({% image_buster /assets/img/zendesk/instant_chat/chat6.png %}){: style="max-width:70%;"}

Em **Ações**, selecione **Notificar por Webhook** e escolha o endpoint que você criou na etapa 1. Em seguida, especifique o corpo da chamada à API. Insira o endereço `campaign_id` da [etapa 2.2](#step-22-schedule-the-delivery) no corpo da solicitação.

![Responda via corpo JSON do SMS Braze.]({% image_buster /assets/img/zendesk/instant_chat/chat7.png %}){: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
			"trigger_properties": {
    "msg_body": "{{ticket.latest_public_comment_html}}"
		},
		"attributes": {
        "zendesk_ticket" : "{{ticket.id}}",
	"zendesk_ticket_open" : "true"
    }
        }
    ]
}
```
{% endraw %}


### Etapa 4: Crie um disparo no Zendesk para atualizar um usuário quando um ticket for fechado

Se quiser notificar o usuário de que o ticket foi fechado, crie uma nova campanha no Braze com o corpo de resposta modelado.

![Atualize um usuário quando o ticket for fechado.]({% image_buster /assets/img/zendesk/instant_chat/chat8.png %}){: style="max-width:70%;"}

Selecione **API Triggered delivery (Entrega disparada pela API)** e copie o ID da campanha.

Em seguida, configure um disparo para notificar o Braze quando o tíquete for fechado:
- Categoria: **Disparar uma mensagem**
- Em Conditions (Condições), selecione **Ticket>Ticket Status (Status do ticket)** e altere-o para **Solved (Resolvido)**

![Criação de tickets resolvidos no Zendesk.]({% image_buster /assets/img/zendesk/instant_chat/chat9.png %}){: style="max-width:70%;"}

Em **Ações**, selecione **Notificar por Webhook** e escolha o segundo endpoint que você acabou de criar. A partir daí, precisamos especificar o corpo da chamada à API:

![Corpo JSON do ticket resolvido.]({% image_buster /assets/img/zendesk/instant_chat/chat10.png %}){: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_API_KEY}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
"trigger_properties": {
    "msg_body": "Your ticket has been closed"
		},
,
			"attributes": {
	"zendesk_ticket_open" : "false"
    }
        }
    ]
}
```
{% endraw %}

### Etapa 5: Adicionar um campo de usuário personalizado no Zendesk

Na Central de administração, selecione **Pessoas** na barra lateral e, em seguida, selecione **Configuração** > **Campos de usuário**. Adicione o campo de usuário personalizado `braze_external_id`.

### Etapa 6: Configurar o encaminhamento de SMS de entrada

Em seguida, você criará duas novas campanhas de webhook no Braze para que possa encaminhar SMS recebidos de clientes para a caixa de entrada do Zendesk.

| Campanha interrompida           | Finalidade                                                                              |
|--------------------|--------------------------------------------------------------------------------------|
| Campanha de webhook 1 | Cria um novo ticket no Zendesk.                                                     |
| Campanha de webhook 2 | Encaminha todas as respostas de SMS de conversação enviadas pelo cliente para o Zendesk. |
{: .reset-td-br-1 .reset-td-br-2 }

#### Etapa 6.1: Criar uma categoria de palavra-chave SMS

No dashboard do Braze, acesse **Público**, escolha seu **grupo de inscrições de SMS** e selecione **Adicionar palavra-chave personalizada**. Preencha os campos a seguir para criar uma categoria de palavra-chave de SMS exclusiva para o Zendesk.

| Campo            | Descrição                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Categoria da palavra-chave | O nome da categoria da palavra-chave, como `ZendeskSMS1`.                                                                 |
| Palavras-chave         | Suas palavras-chave personalizadas, como `SUPPORT`.                                                                                  |
| Mensagem de resposta    | A mensagem que será enviada quando uma palavra-chave for detectada, como "Um representante do atendimento ao cliente entrará em contato com você em breve". |
{: .reset-td-br-1 .reset-td-br-2 }

![Um exemplo de categoria de palavra-chave SMS no Braze.]({% image_buster /assets/img/zendesk/instant_chat/chat11.png %}){: style="max-width:70%;"}

#### Etapa 6.2: Crie sua primeira campanha de webhook

No dashboard do Braze, crie sua primeira campanha de webhook. Essa mensagem sinalizará ao Zendesk que o suporte está sendo solicitado.

No criador do webhook, preencha os seguintes campos:
- URL do webhook: {% raw %}https://{{url}}.zendesk.com/api/v2/tickets{% endraw %}
- Método HTTP: POST
- Cabeçalhos de solicitação:
- Content-Type: application/json
- Autorização:  Básico {{Token}}
- Corpo da solicitação: 

{% raw %}
```liquid
{
  "ticket": {
    "subject": "Action Needed",
    "comment": {
      "body": "{{sms.${inbound_message_body}}}"
    },
"requester":{
"name": "{{${first_name}}} {{${last_name}}}",
"user_fields": {
"braze_external_id": "{{${user_id}}}"
}
},
    "priority": "normal",
    "type": "problem"
  }
}
```
{% endraw %}

![Um exemplo de solicitação com os dois cabeçalhos necessários.]({% image_buster /assets/img/zendesk/instant_chat/chat12.png %}){: style="max-width:70%;"}


#### Etapa 6.3: Agendar a primeira entrega

Em **Entrega programada**, selecione **Entrega baseada em ação** e, em seguida, escolha **Enviar uma mensagem de entrada SMS** para o tipo de disparo. Adicione também o grupo de inscrições de SMS e a categoria de palavras-chave que você configurou anteriormente.

![A página "Schedule Delivery" da primeira campanha de webhook.]({% image_buster /assets/img/zendesk/instant_chat/chat13.png %})

Em **Controles de entrega**, ative a reelegibilidade.

![Reelegível selecionado em "Delivery Controls" (Controles de entrega) para a primeira campanha de webhook.]({% image_buster /assets/img/zendesk/instant_chat/chat14.png %})

#### Etapa 6.4: Crie sua segunda campanha de webhook

Configure uma campanha de mensagens webhook para encaminhar as mensagens SMS restantes do usuário para o Zendesk:

Como o Zendesk envia o ID do ticket como uma string, crie um bloco de conteúdo para converter a string em um número inteiro para que você possa usá-lo no webhook do Zendesk.

{% raw %}
```liquid
{% assign var = {{custom_attribute.${zendesk_ticket}}} | to_i %}{{var}}
```
{% endraw %}

No criador do webhook:
- URL do webhook: {% raw %}https://{{url}}.zendesk.com/api/v2/tickets/{{content_blocks.${to_int}}}.json{% endraw %}
- Solicitação: PUT
- KVPs:
    - Content-Type:application/JSON
    - Autorização: Básico {{Token}}

Corpo da amostra: 

{% raw %}
```liquid
{
  "ticket": {
    "comment": {
      "body": "Inbound message from {{${first_name}}} {{${last_name}}}: {{sms.${inbound_message_body}}}"
    }
}
}
```
{% endraw %}

#### Etapa 6.5: Concluir a configuração da segunda campanha de webhook
- Configure um disparo baseado em ação para usuários que enviam uma mensagem de entrada na categoria "Outros".
- Estabelecer critérios de reelegibilidade.
- Adicione os públicos aplicáveis (nesse caso, o atributo personalizado **zendesk_ticket_open** é **verdadeiro**).

[2]: {% image_buster /assets/img/zendesk/instant_chat/chat2.png %}
