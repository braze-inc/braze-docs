---
nav_title: Rokt Calendar
article_title: Rokt Calendar
alias: /partners/rokt_calendar/
description: "Este artigo de referência descreve a parceria entre a Braze e a Rokt Calendar, uma tecnologia dinâmica de marketing de calendário que permite às marcas enviar eventos e comunicações promocionais 1:1 na forma de eventos e notificações por push."
page_type: partner
search_tag: Partner
---

# Rokt Calendar

> [O Rokt Calendar](https://www.rokt.com/rokt-calendar/) é uma tecnologia dinâmica de marketing de calendário que ativa as marcas para empurrar eventos 1:1 e comunicações promocionais na forma de eventos e notificações de calendário.

_Esta integração é mantida pelo Rokt Calendar._

## Sobre a integração

A integração entre a Braze e a Rokt Calendar permite que seus assinantes da Rokt Calendar e seus dados sejam enviados para a Braze por webhooks da Braze. Em seguida, você pode usar esses dados no Braze Canvases para direcionamento de jornada e segmentação de público usando qualquer um dos seguintes [atributos personalizados do Rokt Calendar](#audience-segmentation). 

## Pré-requisitos

| Requisito  | Descrição |
| ------------ | ----------- |
| Conta Rokt Calendar | É necessário ter uma conta Rokt Calendar específica do cliente para usar a parceria. Entre em contato com [sales-calendar@rokt.com](mailto:sales-calendar@rokt.com) para falar com um gerente de contas  |
| Configuração do Rokt Calendar | Seu gerente de conta do Rokt Calendar trabalhará com você para configurar o calendário da forma mais adequada às suas necessidades, incluindo configurações como:<br>\- Bandeira de mesclagem<br>\- Sinalizador de fallback de SubscriberID<br>\- Captura de e-mail, se necessário |
| Credenciais OAuth do Rokt Calendar | Essa chave, fornecida pelo gerente de sua conta Rokt Calendar, permitirá conectar suas contas Braze e Rokt Calendar.<br><br>Isso pode ser criado no dashboard do Braze em **Settings** > **Connected Content** (Configurações > Conteúdo conectado). |
| Chave da API REST do Braze | Uma chave da API REST da Braze com `users.track` permissões. Você precisará fornecê-la ao seu gerente de conta da Rokt Calendar.<br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| [Ponto de extremidade REST do Braze]({{site.baseurl}}/api/basics/#endpoints) | Seu URL do ponto de extremidade REST. Seu endpoint dependerá do URL do Braze para sua instância. |
| ID do assinante externo | Esse é o identificador usado pelo processo de inscrição do Rokt Calendar para fazer a correspondência entre o assinante do calendário e o usuário do Braze. Isso é algo que você passa para a Rokt Calendar.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Segmentação do público {#audience-segmentation}

Quando o Rokt Calendar cria um novo usuário ou combina um assinante existente com um usuário do Braze, o Rokt Calendar enviará os seguintes atributos personalizados de inscrição que você pode filtrar no Braze:

| Atributo personalizado  | Definição       | Exemplo          |
| ----------------  | ---------------- | ---------------- |
| `rokt:account_code` | Código da conta do Rokt Calendar | `brazetest/f5733866ade2` e `brazetest/ff10919f1078` |
| `rokt:account_id` |ID da conta do Rokt Calendar | `d0ce4299-7d6c-4888-bfd8-c7e867a0fa6c/f5733866ade2` |
| `rokt:account_name` | Nome da conta do Rokt Calendar | `Braze Test/f5733866ade2` |
| `rokt:calendar_code` | Código do calendário Rokt Calendar | `test-calendar-1/f5733866ade2` |
| `rokt:calendar_id` | ID do calendário Rokt Calendar | `9a9007c7-f5a4-e811-b13c-06424c4f2724/f5733866ade2` |
| `rokt:calendar_title` | Título do calendário Rokt Calendar | `Test Calendar 1/f5733866ade2` |
| `rokt:country_code` | Código do país relacionado à inscrição criada | `AU/f5733866ade2` |
| `rokt:device_name` | Tipo de dispositivo relacionado à inscrição criada | `Desktop/f5733866ade2` |
| `rokt:geo_country` | País de origem relacionado à inscrição criada | `Australia/f5733866ade2` |
| `rokt:optIn1` | Se o usuário tiver feito a aceitação da primeira de duas aceitações relacionadas à inscrição criada | `True/f5733866ade2` |
| `rokt:optIn2` | Se o usuário tiver aceitado a segunda de duas aceitações relacionadas à inscrição criada | `True/f5733866ade2` |
| `rokt:source` | A fonte da inscrição criada | `brazetest.Rokt Calendarapp.com/f5733866ade2` |
| `rokt:subscriber_email` | O endereço de e-mail inserido pelo usuário durante o processo de inscrição | `test@email.com/f5733866ade2` |
| `rokt:subscription_id` | O ID da inscrição, que serve como um identificador exclusivo, relacionado à inscrição criada | `06423672-b6ba-4536-aa36-70788a7a0a36` |
| `rokt:subscription_method` | Método de inscrição (webcal/Google) relacionado à inscrição criada. | `WebCal/f5733866ade2` |
| `rokt:tags` | Tags de calendário usadas relacionadas à inscrição criada. | `Test Calendar 1/All Teams/f5733866ade2 and Test Calendar 1/TeamI//f5733866ade2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

O Rokt Calendar também acionará um evento personalizado do `subscribe` assim que o usuário se inscrever no calendário Rokt, que poderá ser usado na segmentação do Braze ou como disparador de uma campanha ou componente do Canvas.

## Integração

### Etapa 1: crie um público de inscritos no calendário

Para enviar eventos de calendário do Canva, é necessário ter uma configuração de calendário da Rokt Calendar com usuários já inscritos. Para fazer isso, será necessário informar aos usuários onde e como assinar o calendário. A Rokt Calendar recomenda estas sugestões:

#### Fornecer pontos de integração de inscrição
Para criar um público de calendários dos assinantes, será necessário oferecer um destino para o qual o usuário possa navegar e se inscrever. Alguns exemplos de pontos de integração de inscrição incluem:
  - Adicione um botão de calendário ao seu site
  - Adição de um link de calendário em um e-mail ou SMS 
  - Adicione um botão de calendário ao seu app
  - Adicione um link de calendário nas redes sociais

#### Promover o calendário
Para criar um público de assinantes, você precisará promover o calendário para o seu público, para que ele saiba como se inscrever. Alguns exemplos de promoção de calendário incluem:
  - Publicações em redes sociais
  - Envio de e-mail com boletins informativos e atualizações
  - Publicações no blog
  - Notificações no app

### Etapa 2: Criar um webhook do Rokt Calendar no Braze

No Braze, você pode configurar uma campanha de webhook ou um webhook em um Canva:

- Enviar um novo evento personalizado: Permitir que novos eventos sejam adicionados a um segmento dos calendários dos assinantes.
- Atualizar um evento personalizado: Permitir que uma atualização seja feita em um evento existente nos calendários dos assinantes.

Para criar um modelo de webhook da Rokt Calendar para ser usado em futuras campanhas ou Canvas, navegue até **Modelos** > **Modelos de webhook** na plataforma Braze. 

Se quiser criar uma campanha única de webhook do Rokt Calendar ou usar um modelo existente, selecione **Webhook** no Braze ao criar uma nova campanha.

{% tabs %}
{% tab Enviar um novo evento %}
Depois de selecionar o modelo de webhook da Rokt Calendar, você verá o seguinte:
- **URL do webhook**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}`{% endraw %}
- **Corpo da solicitação**: Texto bruto
{% endtab %}
{% tab Atualizar um evento existente %}
Depois de selecionar o modelo de webhook da Rokt Calendar, você verá o seguinte:
- **URL do webhook**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}/update`{% endraw %}
- **Corpo da solicitação**: Texto bruto
{% endtab %}
{% endtabs %}

#### Cabeçalhos de solicitação e método

A Rokt Calendar requer um `HTTP Header` para autorização que inclua seu nome de credencial de conteúdo conectado da Rokt Calendar. Os itens a seguir já estarão incluídos no modelo como pares de valores-chave, mas na guia **Settings (Configurações)**, você deve substituir `<Rokt-Calendar-API>` pelo nome da credencial encontrado em `Manage Settings > Connected Content > Credential`.

{% raw %}
- **Método HTTP**: POST
- **Cabeçalho da solicitação**:
  - **Autorização**: portador `{% connected_content https://api.roktcalendar.com/oauth2/token :method post :basic_auth <Rokt-Calendar-API> :body grant_type=client_credentials :save token :retry %}{{token.access_token}}`
  - **Tipo de Conteúdo**: application/json
{% endraw %}

#### Corpo da solicitação

{% tabs local %}
{% tab Enviar um novo evento %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  },
  "subscriptionIds": ["{{custom_attribute.${rokt:subscription_id}| join: '","'  }}"]
}
```
{% endraw %}
{% endtab %}
{% tab Atualizar um evento existente %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  }
}
```
{% endraw %}
{% endtab %}
{% tab Detalhes do evento %}
Os campos a seguir incluem informações que podem ser personalizadas no nível do evento.

| Campo             | Definição       | Exemplo          |
| ----------------  | ---------------- | ---------------- |
| `eventId` <br>***Necessário** | Um identificador exclusivo para o evento a ser adicionado ou atualizado | `Event_00001`
| `eventTitle` <br>***Necessário** | O título do evento, como apareceria no calendário | Promoção de verão 2019
| `eventDescr` | A descrição do evento como apareceria no calendário | A promoção é válida por três dias; clique no link `www.mybusiness.com/sale` para ver as ofertas. |
| `eventLocation` | O local do evento como apareceria no calendário. Observe que isso é frequentemente usado como uma segunda chamada para ação, que é complementar ao eventTitle. | Abra o evento para obter 50% de desconto |
| `eventStart` <br>***Necessário**  | A data e a hora de início do evento, como apareceria no calendário | `2019-02-21T15:00:00` |
| `eventEnd` <br>***Necessário**  | A data e a hora de início do evento, como apareceria no calendário | `2019-02-21T16:00:00` |
| `eventTz` <br>***Necessário**  | O fuso horário do evento, como apareceria no calendário. Observe que a lista de fusos horários aplicáveis pode ser encontrada [aqui](https://roktcalendar-api.readme.io/docs/timezones). | `Eastern Standard Time` |
| `notifyBefore` <br>***Necessário**  | A hora do lembrete do evento, como apareceria no calendário; note que isso é expresso em minutos | `15` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

{% alert tip %}
Para obter uma lista de fusos horários válidos, consulte [https://roktcalendar-api.readme.io](https://roktcalendar-api.readme.io/reference/timezones)/reference/timezones.
{% endalert %}

### Etapa 3: veja uma prévia da sua solicitação

Pré-visualize a solicitação no painel **Preview (Pré-visualização** ) ou navegue até a guia **Test (Teste** ), onde é possível selecionar um usuário aleatório, um usuário existente ou personalizar o seu próprio usuário para testar o webhook.

{% alert important %}
Lembre-se de salvar seu modelo antes de sair da página! <br>Os modelos de webhook atualizados podem ser encontrados na lista **Modelos de webhook salvos** ao criar uma nova [campanha de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}

