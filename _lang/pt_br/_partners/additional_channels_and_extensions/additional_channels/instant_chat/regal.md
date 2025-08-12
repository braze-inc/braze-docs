---
nav_title: Regal
article_title: Regal
description: "Este artigo de referência descreve a parceria entre o Braze e a Regal, uma solução de vendas por telefone e SMS que permite usar dados de ambas as fontes para criar experiências personalizadas para seus clientes."
alias: /partners/regal/
page_type: partner
search_tag: Partner

---

# Regal

> [Regal.io](https://regal.io) é a solução de vendas por telefone e SMS criada para gerar mais conversas, para que você possa atingir suas metas de crescimento muito mais rapidamente.

Ao integrar a Regal e o Braze, você pode criar uma experiência mais consistente e personalizada em todos os pontos de contato com o cliente.
- Envie o próximo melhor e-mail ou notificação por push da Braze com base no que foi dito em uma conversa telefônica na Regal.
- Dispare uma chamada na Regal quando um cliente de alto valor clica em um e-mail de marketing da Braze, mas não converte.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Regal | É necessário ter uma conta Regal para aproveitar essa parceria. |
| Chave de API da Regal | Uma chave de API da Regal permitirá o envio de eventos da Braze para a Regal.<br><br>Envie um e-mail para [support@regal.io](mailto:support@regal.io) para obter essa chave. |
| Transformação de Dados Braze | A transformação de dados está atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente da Braze se quiser em participar do acesso antecipado. Isso é necessário para receber dados do Regal. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração: Envio de dados do Braze para a Regal

A seção a seguir descreve como usar o Braze como fonte para enviar o perfil do cliente e os dados do evento para a Regal usando o Braze Canvas ou webhooks de campanha.

### Etapa 1: Criar novos contatos no Regal

Crie um canva ou uma campanha que se conecte à Regal sempre que um novo contato for criado na Braze e que você queira que esteja disponível para chamadas e mensagens de texto na Regal. 

1. Crie um Canva ou uma campanha intitulada "Create New Contact for Regal" (Criar novo contato para a Regal) e selecione **Action-Based (Baseado em ação** ) como o tipo de entrada.

2. Defina a lógica do disparo como **Evento personalizado** e selecione o evento que é disparado quando um contato com um número de telefone é criado. A Regal também recomenda adicionar um filtro extra no campo do telefone para garantir que ele esteja definido.

3. Em seu novo modelo de webhook, preencha os seguintes campos:
   - **URL do webhook**: <https://events.regalvoice.com/events>
   - **Corpo da solicitação**: Texto bruto

#### Cabeçalhos de solicitação e método

A Regal.io também requer um cabeçalho HTTP para autorização e um método HTTP. O seguinte já estará incluído no modelo como um par de valores-chave na guia **Settings (Configurações)**:
{% raw %}
- **Método HTTP**: POST
- **Cabeçalhos de solicitação**:
    - **Autorização**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Corpo da solicitação

O único campo obrigatório abaixo é a propriedade `traits.phone`. O restante é opcional. No entanto, se você incluir `optIn`, deverá incluir `optIn.channel` e `optIn.subscribed`.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "email": "<email>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": true
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": true
            }
        ],
        "custom1": "<custom1>",
        "custom2": "<custom2>"
    },
    "eventSource": "braze"
}
```

O exemplo de carga útil acima pressupõe que todos os seus contatos aceitaram a aceitação de voz e SMS. Se isso não for válido para o seu caso, você poderá remover a propriedade `optIn` do item acima e configurar um canva ou uma campanha separada para atualizar um contato na Regal quando o `optIn` for coletado.

### Etapa 2: Atualizar informações de aceitação 

Se a aceitação e a saída puderem ocorrer em diferentes partes da experiência do usuário no app, é importante atualizar o Regal à medida que os usuários aceitarem ou saírem. Abaixo está um canva recomendado para enviar informações de aceitação atualizadas para a Regal. Ele presume que você salvará as informações como campo de perfil na Braze. Se não for o caso, o disparo poderá ser um evento na sua conta da Braze que represente a aceitação ou o cancelamento da inscrição de um usuário (o exemplo abaixo é para aceitação por telefone, mas você pode configurar uma canva ou campanha semelhante para aceitação por SMS, caso faça a coleta separadamente).

1. Crie uma nova tela ou campanha com o título "Send Opt In or Out to Regal" (Enviar aceitação ou recusa para a Regal).

2. Selecione uma das seguintes opções de disparo e escolha o campo que representa o status de aceitação do usuário. Se você disparar um evento para a Braze para representar a aceitação ou o cancelamento, use esse evento como o gatilho.
    - Campo do perfil do usuário atualizado
    - Atualizar status do grupo de inscrições
    - Status de inscrição

3. Em seu novo modelo de webhook, preencha os seguintes campos:
   - **URL do webhook**: <https://events.regalvoice.com/events>
   - **Corpo da solicitação**: Texto bruto

#### Cabeçalhos de solicitação e método

A Regal.io também requer um cabeçalho HTTP para autorização e um método HTTP. O seguinte já estará incluído no modelo como um par de valores-chave, mas na guia **Configurações**:
{% raw %}
- **Método HTTP**: POST
- **Cabeçalhos de solicitação**:
    - **Autorização**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Corpo da solicitação

Você também pode adicionar outros atributos de perfil de usuário nessa carga útil se quiser garantir que mais atributos sejam atualizados simultaneamente.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            }
        ]
    },
    "eventSource": "braze"
}
```

### Etapa 3: Enviar eventos personalizados

Por fim, configure um canva ou uma campanha para cada um dos principais eventos que deseja enviar à Regal. A Regal recomenda o envio de quaisquer eventos que sejam importantes para disparar SMS e chamadas na Regal (como um evento em cada etapa do fluxo de inscrição ou compra) ou que sejam usados como critérios de saída para que os contatos saiam das campanhas da Regal.

Por exemplo, abaixo está um fluxo de trabalho para enviar um evento à Regal quando um usuário conclui a primeira etapa de um aplicativo.

1. Crie um novo canva ou campanha com o nome "Enviar evento concluído da etapa 1 do aplicativo para a Regal".

2. Defina a lógica do nó de gatilho como **Evento personalizado** e selecione o nome do evento que deseja enviar à Regal, como "Etapa 1 do aplicativo concluída".

3. Em seu novo modelo de webhook, preencha os seguintes campos:
   - **URL do webhook**: <https://events.regalvoice.com/events>
   - **Corpo da solicitação**: Texto bruto

#### Cabeçalhos de solicitação e método

A Regal.io também requer um cabeçalho HTTP para autorização e um método HTTP. O seguinte já estará incluído no modelo como um par de valores-chave, mas na guia **Configurações**:
{% raw %}
- **Método HTTP**: POST
- **Cabeçalhos de solicitação**:
    - **Autorização**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Corpo da solicitação

Você pode adicionar outros atributos de perfil de usuário nessa carga útil se quiser garantir que mais atributos sejam atualizados simultaneamente.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "custom1": "<custom1>",
        "custom2": "<custom2>",
        "custom3": "<custom3>"
    },
    "name": "Application Step 1 Completed",
    "properties": {
      "educationalLevel": "<educationalLevel>",
      "preferredLocation": "<preferredLocation>",
      "preferredSubject": "<preferredSubject>",
      "readytoCommit": true
    },
    "eventSource": "braze"
}
```

#### Atribuições de contato atualizadas

Embora não seja necessário, a Regal recomenda também enviar quaisquer campos de dados de perfil de usuários importantes nas cargas úteis dos fluxos de trabalho do evento para garantir que a Regal tenha acesso às atribuições de contato mais atualizadas no momento em que os eventos importantes estiverem disponíveis.

{% alert note %}
Se tiver dúvidas sobre quais eventos são importantes para enviar à Regal ou sobre a melhor forma de configurar esses canvas e campanhas, entre em contato pelo e-mail support@regal.io.
{% endalert %}

## Integração: Envio de dados do Regal para o Braze

Esta seção descreve como obter eventos de relatórios da Regal, como `SMS.sent` e `call.completed`, no Braze para que eles possam aparecer em seus perfis do Braze e estar disponíveis na ferramenta de segmentação do Braze, no Canva e nas campanhas. Essa integração usa os Webhooks do Regal Reporting e a transformação de dados do Braze para automatizar o fluxo de dados.

### Etapa 1: Criar uma transformação de dados no Braze

{% alert important %}
A transformação de dados está atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente da Braze se quiser em participar do acesso antecipado.
{% endalert %}

O Braze recomenda criar uma transformação de acordo com o webhook do Regal que você planeja enviar ao Braze. 

Para criar uma transformação de dados:
1. Navegue até a página **Transformations (Transformações** ) em seu dashboard do Braze.
2. Dê um nome à sua transformação e clique em **Create transformation (Criar transformação**).
3. Na lista de transformações, clique em <i class="fa-solid fa-ellipsis-vertical" title="Exibir ações"></i> e selecione **Copiar URL do webhook**.

![]({% image_buster /assets/img/regal/copy_webhook_url.png %})

### Etapa 2: Ativar webhooks de relatórios no Regal

Para configurar webhooks de relatórios:
1. Acesse o app da Regal e abra a página **de configurações**.

2. Na seção **Reporting Webhooks** (Webooks de relatório), clique em **Create Webhooks** (Criar webhooks).

3. Na entrada do endpoint do webhook, adicione o URL do webhook da transformação de dados da Braze para a transformação de dados associada.

![]({% image_buster /assets/img/regal/edit_webhook.png %}){: style="max-width:60%;"}

#### Atualização de um ponto de extremidade
Quando você edita um endpoint, pode levar até 5 minutos para que o cache seja atualizado e envie eventos para o novo endpoint.
#### Tentativas
Atualmente, não há novas tentativas nesses eventos. Se uma resposta não for recebida em 5 segundos, o evento será descartado e não passará por novas tentativas. A Regal adicionará novas tentativas em uma versão futura.
#### Eventos
O [guia Webhooks de relatórios](https://developer.regal.io/docs/reporting-webhooks#events) da Regal inclui a lista completa de eventos de relatórios que eles publicam. Lá você pode ver definições de propriedades e exemplos de cargas úteis.

### Etapa 3: Transforme os eventos Regal em eventos Braze

O recurso Braze [Data Transformation]({{site.baseurl}}/data_transformation) permite que você mapeie os eventos Regal recebidos no formato necessário para serem adicionados como atribuições, eventos ou compras no Braze.

1. Dê um nome à sua transformação de dados. Recomenda-se configurar uma transformação de dados por webhook de evento.

2. Para testar a conexão, crie uma chamada de saída do Regal Agent Desktop para seu telefone celular e envie o formulário Resumo da conversa para criar um evento call.completed.

3. Determine quais identificadores serão usados para mapear seus contatos da Regal para seus perfis da Braze. Os identificadores disponíveis nos eventos do Regal incluem:
   - `userId` - somente definido em eventos se você tiver enviado anteriormente esse identificador para um contato
   - `traits.phone`
   - `traits.email` - somente definido em eventos se você tiver enviado anteriormente esse identificador para um contato

#### Identificadores com suporte da Braze
- O Braze não oferece suporte a números telefônicos como identificador. Para usar isso como um identificador, o número de telefone pode ser definido como um [alias de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) no Braze.
- Ao usar a transformação de dados do Braze, o endereço de e-mail pode ser usado como um identificador. Se o endereço de e-mail existir como perfil na Braze, o perfil existente será atualizado. Se o endereço de e-mail ainda não existir no Braze, será criado um perfil somente de e-mail.

## Casos de uso

{% tabs %}
{% tab Disparar um e-mail %}

**Disparar um e-mail da Braze com base em uma disposição de chamada na Regal**

Abaixo está um exemplo de carga útil para um evento `call.completed` no Regal. 

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com"
  },
  "name": "call.completed",
  "properties": {
    "agent_firstname": "Rebecca",
    "agent_fullname": "Rebecca Greene",
    "agent_id": "xxxx@yourbrand.com",
    "direction": "OUTBOUND",
    "regal_voice_phone": "+19545558563",
    "regal_voice_phone_internal_name": "Sales Line",
    "contact_phone": "+17625555555",
    "call_id": "WTxxxxx9",
    "type": "Outbound Call",
    "disposition": "Converted During Convo",
    "notes": null,
    "objections": null,
    "campaign_name": "Life Insurance Quote Follow Up",
    "campaign_friendly_id": "445",
    "started_at": 1657855046,
    "ended_at": 1657855053,
    "completed_at": 1657855059,
    "talk_time": 7,
    "wrapup_time": 6,
    "handle_time": 13,
    "journey_uuid": null,
    "journey_name": null,
    "journey_friendly_id": null
  },
  "originalTimestamp": "1657855059",
  "eventSource": "Regal Voice"
}
```

Abaixo está um exemplo de transformação de dados para mapear isso para um evento personalizado no Braze.

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is a default template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "name": "Call Completed",
     "time": isoString,
     "_update_existing_only": false,
     "properties": {
       "agent_firstname": payload.properties.agent_firstname,
       "agent_fullname": payload.properties.agent_fullname,
       "agent_id": payload.properties.agent_id,
       "direction": payload.properties.direction,
       "regal_voice_phone": payload.properties.regal_voice_phone,
       "regal_voice_phone_internal_name": payload.properties.regal_voice_phone_internal_name,
       "contact_phone": payload.properties.contact_phone,
       "call_id": payload.properties.call_id,
       "type": payload.properties.type,
       "disposition": payload.properties.disposition,
       "notes": payload.properties.notes,
       "objections": payload.properties.objections,
       "campaign_name": payload.properties.campaign_name,
       "campaign_friendly_id": payload.properties.campaign_friendly_id,
       "started_at": payload.properties.started_at,
       "ended_at": payload.properties.ended_at,
       "completed_at": payload.properties.completed_at,
       "talk_time": payload.properties.talk_time,
       "wrapup_time": payload.properties.wrapup_time,
       "handle_time": payload.properties.handle_time,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_name": payload.properties.journey_name,
       "journey_friendly_id": payload.properties.journey_friendly_id
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Atualizar atribuições do perfil %}

**Atualizar os atributos do perfil na Braze com base nos eventos `contact.attribute.edited` da Regal**

Abaixo está um exemplo de carga útil para um evento `contact.attribute.edited` no Regal. Esse evento é disparado sempre que um de seus agentes aprende algo novo em uma conversa e atualiza uma atribuição no perfil do contato.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
  },
  "name": "contact.attribute.edited",
  "properties": {
    "agent_email": "xxxx@yourbrand.com",
    "contact_phone": "+17625555555",
    "changes": {
      "custom_properties": {
        "annual_income": {
          "old_value": "150,000",
          "new_value": "300,000"
        }
      }
    },
    "created_at": "1657855462"
  },
  "originalTimestamp": "1657855462",
  "eventSource": "Regal Voice"
}
```

Abaixo está um exemplo de transformação de dados para mapear os novos valores de propriedades personalizadas para os atributos relevantes em seus perfis Braze:

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// Capture the key's updated property value within the 'changes' object and store this in an attributes variable that can be used in the /users/track request

const changes = payload.properties.changes.custom_properties;

const attributes = {};
for (const key in changes) {
 attributes[key] = changes[key].new_value;
}

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

const brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     ...attributes
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Mantenha seus experimentos em sincronia %}

**Mantenha seus experimentos no Braze e no Regal em sincronia usando os eventos do `contact.experiment.assigned` **

Abaixo está um exemplo de carga útil para um evento `contact.experiment.assigned` no Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
  },
  "name": "contact.experiment.assigned",
  "properties": {
    "experiment_name": "Post Call Offer Test",
    "experiment_id": "xxxx-xxxx-xxxx-xxxx",
    "experiment_variant": "Aggressive Offer - 50%",
    "journey_uuid": "xxxx-xxxx-xxxx-xxxx",
    "journey_friendly_id": 220,
    "journey_name": "Post Call Follow Up"
  },
  "originalTimestamp": "1657855118",
  "eventSource": "Regal Voice"
}
```

Abaixo está um exemplo de transformação de dados para mapear isso para um evento personalizado no Braze.

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze, it must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z
let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     "name": "Contact Experiment Assigned",
     "time": isoString,
     "properties": {
       "experiment_name": payload.properties.experiment_name,
       "experiment_id": payload.properties.experiment_id,
       "experiment_variant": payload.properties.experiment_variant,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_friendly_id": payload.properties.journey_friendly_id,
       "journey_name": payload.properties.journey_name
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;

```
{% endtab %}
{% tab Cancelar inscrição de um contato %}

**Cancelar inscrição de um contato no Braze com base em um `contact.unsubscribed` da Regal**

Abaixo está um exemplo de carga útil para um evento `contact.unsubscribed` no Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
    "ip": "78.97.213.166"
  },
  "name": "contact.unsubscribed",
  "properties": {
    "new_subscription": true,
    "channel": "voice",
    "text": null,
    "ip": "207.38.149.143",
    "source": "regalvoice.agent_desktop",
    "timestamp": "1657855229"
  },
  "originalTimestamp": "1657855230",
  "eventSource": "Regal Voice"
}
```

Abaixo está um exemplo de transformação de dados para cancelar a inscrição do contato na Braze.

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": true,
     "subscription_groups" : [{
       "subscription_group_id": "YOUR SUBSCRIPTION GROUP ID",
       "subscription_state": "unsubscribed"
     }]
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% endtabs %}

