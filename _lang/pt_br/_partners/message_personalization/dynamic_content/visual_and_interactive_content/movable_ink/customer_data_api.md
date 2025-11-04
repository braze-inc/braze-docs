---
nav_title: Conexão com a API de dados de cliente
article_title: Conexão com a API de dados de cliente da Movable Ink
description: "Este artigo de referência descreve como se conectar para ativar os dados de eventos de clientes armazenados no Braze para gerar conteúdo personalizado no Movable Ink usando a API de dados de clientes."
page_type: partner
search_tag: Partner
---

# Conexão com a API de dados de cliente da Movable Ink

> A integração da API de dados do cliente do Braze e da Movable Ink permite que os profissionais de marketing ativem os dados de eventos de clientes armazenados no Braze para gerar conteúdo personalizado na Movable Ink.

A Movable Ink é capaz de ingerir eventos comportamentais da Braze por meio de sua API de dados de cliente. Os eventos serão armazenados nos perfis de usuário com base no ID de usuário exclusivo (UUID) que é passado para a Movable Ink.

Para saber mais sobre o Stories, a API de dados de clientes da Movable Ink e como a Movable Ink aproveita os dados comportamentais, visite os seguintes artigos da central de suporte:

- [Potencialize o conteúdo com dados comportamentais](https://support.movableink.com/hc/en-us/sections/360001239453-Power-content-with-behavioral-data)
- [Introdução e guia da API de dados de cliente](https://support.movableink.com/hc/en-us/articles/13815957200663-Customer-Data-API-introduction-and-guide)
- [PERGUNTAS FREQUENTES: API de dados de cliente](https://support.movableink.com/hc/en-us/articles/12423178752279-FAQ-Customer-Data-API)

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta da Movable Ink | É necessário ter uma conta da Movable Ink para usar a parceria. |
| Credenciais da API do Movable Ink | A equipe de soluções da Movable Ink gerará credenciais de API para você. As credenciais da API consistem em:{::nomarkdown}<ul><li>Um URL de endpoint (para onde os dados serão enviados)</li><li>Nome de usuário e senha (usados para autenticar a API)</li></ul>{:/} Se desejar, a Movable Ink poderá fornecer o nome de usuário e a senha como um valor codificado em base64 a ser usado como um valor de cabeçalho de autorização básica. |
| Cargas úteis de eventos comportamentais | Será necessário compartilhar as cargas úteis do evento com a equipe de experiência do cliente da Movable Ink. Consulte [Compartilhamento de cargas úteis de eventos](#event-payloads) com o Movable Ink para obter detalhes. |
| Ativos criativos e lógica comercial | Será necessário compartilhar ativos criativos com a Movable Ink, incluindo arquivos do Adobe Photoshop (PSD) que orientem a Movable Ink sobre como criar o bloco e uma imagem fallback. Você também precisará fornecer a lógica de negócios para saber como e quando exibir o bloco de conteúdo ativado pelo parceiro. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Criar uma campanha de webhook no Braze

#### Etapa 1a: Criar uma nova campanha

1. No Braze, [crie uma campanha de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
2. Dê um nome e uma descrição opcional à sua campanha.
3. Selecione **Modelo em branco** como seu modelo.

#### Etapa 1b: Adicione suas credenciais da API de dados de clientes

1. No campo **URL do webhook**, digite o URL do endpoint da Movable Ink.

![Guia Compose do criador do webhook no Braze com o URL do endpoint do Movable Ink e o Request Body definido como JSON Key/Value Pairs.]({% image_buster /assets/img/movable_ink/cd_api_webhook_url.png %}){: style="max-width:75%" }

{:start="2"}
2\. Selecione a guia **Configurações**.
3\. Adicione os seguintes cabeçalhos de solicitação como pares de valores-chave:

| Chave | Valor |
| --- | --- |
| Tipo de conteúdo | aplicativo/json |
| Autorização | Digite a autenticação básica que você recebeu da Movable Ink. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Guia Configurações do criador do webhook no Braze com pares de valores-chave para Content-Type e Authorization.]({% image_buster /assets/img/movable_ink/cd_api_webhook_settings.png %}){: style="max-width:75%" }

#### Etapa 1c: configure sua carga útil

1. Retorne à guia **Compor**.
2. Para o **corpo da solicitação**, crie seu próprio corpo de solicitação com pares de valores-chave JSON ou insira a carga útil do evento como texto bruto. Consulte as [cargas úteis de amostra](#sample-payloads) para obter exemplos de eventos padrão de comércio eletrônico.

![Guia Compose do criador do webhook no Braze com pares de valores-chave JSON para ID, registro de data e hora, ID do usuário e tipo de evento.]({% image_buster /assets/img/movable_ink/cd_api_webhook_kvp.png %}){: style="max-width:75%" }

#### Etapa 1d: Teste seu webhook {#step-1d}

Será necessário compartilhar uma carga útil de amostra com a equipe de experiência do cliente da Movable Ink. É possível gerar essa carga útil na guia **Teste** com base na carga útil que você construiu.

{% alert important %}
A Movable Ink recomenda esperar para testar seu webhook na Braze até que a equipe de experiência do cliente da Movable Ink tenha confirmado que concluiu o mapeamento e está pronta para receber um teste. Se esse mapeamento não estiver completo, você provavelmente receberá um erro ao testar.
{% endalert %}

Para testar seu webhook, faça o seguinte:

1. Selecione a guia **Teste**.
2. Pré-visualize a mensagem como um usuário para ver uma amostra da carga útil do evento para esse usuário. É possível escolher entre a prévia como usuário aleatório, usuário específico ou usuário personalizado.
3. Se tudo estiver correto, clique em **Send test (Enviar teste)** para enviar uma solicitação de teste.

![Mensagem de resposta do webhook no Braze mostrando uma resposta 200 OK.]({% image_buster /assets/img/movable_ink/cd_api_webhook_response.png %}){: style="max-width:75%" }

### Etapa 2: Finalize a configuração de sua campanha

#### Etapa 2a: Programe sua campanha

Quando terminar de criar e testar o webhook, [agende sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types). 

O Braze oferece suporte a entregas programadas, baseadas em ação e disparadas por API. [A entrega baseada em ação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) é geralmente a melhor opção para a maioria dos casos de uso de eventos comportamentais. Em caso de dúvidas sobre o que faz sentido para o seu caso de uso, entre em contato com os gerentes de sucesso do cliente da Braze e da Movable Ink.

Para entrega baseada em ação:

1. Especifique a ação-gatilho. Esse é o evento que disparará o webhook para a Movable Ink.
2. Certifique-se de que a **postergação do agendamento** esteja definida como **Immediately (Imediatamente**). Os dados do evento devem ser enviados à Movable Ink imediatamente após a ocorrência do evento, sem postergação.
3. Defina a duração da campanha especificando uma hora de início. É provável que um horário de término não seja aplicável, mas ele pode ser definido se necessário para o caso de uso.

{% alert note %}
Para garantir que os dados sejam enviados para a Movable Ink em tempo real, não selecione **Send campaign to users in their local time zone** (Enviar campanha para os usuários em seu fuso local).
{% endalert %}

#### Etapa 2b: Especifique seu público

Em seguida, determine quais usuários deseja direcionar para essa campanha. Para obter detalhes, consulte [Direcionamento de usuários]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/).

Certifique-se de não usar Testes A/B em sua campanha, desmarcando a caixa de seleção **Grupo de controle**. Se um grupo de controle for incluído, uma porcentagem dos usuários não terá dados enviados para o Movable Ink. Todo o seu público deve acessar a variante em vez do grupo de controle.

![Painel de Testes A/B em uma campanha do Braze com 100% de distribuição de variante atribuída à Variante 1 e nenhum grupo de controle.]({% image_buster /assets/img/movable_ink/cd_api_webhook_ab.png %})

#### Etapa 2c: Selecionar eventos de conversão (opcional)

Se desejar, você pode atribuir eventos de conversão a essa campanha no Braze.

No entanto, como o webhook destina-se apenas ao envio de dados, a atribuição nesse nível é provavelmente menos útil do que a atribuição no nível da campanha depois que os dados comportamentais da Braze são usados para personalizar o conteúdo.

### Etapa 3: Lançar a campanha

Revise a configuração do webhook e inicie sua campanha.

## Considerações

### Alinhamento em um identificador de usuário exclusivo

Certifique-se de que o valor do identificador exclusivo de usuário (UUID) que você está usando como `mi_u` esteja disponível no Braze e possa ser incluído nas cargas úteis do evento enviadas ao Movable Ink.

Isso garante que os eventos comportamentais que o Movable Ink referencia ao gerar uma imagem sejam associados ao mesmo cliente para o qual eles receberam os eventos comportamentais. Se o valor do UUID não for o mesmo do `external_id` da Braze, o UUID deverá ser capturado e passado para a Braze como atributo ou nas propriedades de um evento da Braze para usar esse identificador.

O Braze rastreia o comportamento do usuário em várias plataformas (como a Web e o app para dispositivos móveis), portanto, um único usuário pode ter várias IDs anônimas distintas. Esses IDs podem ser mesclados no perfil de usuário único conhecido do Stories quando um evento `identify` é enviado ao Movable Ink, desde que o evento `identify` inclua um identificador anônimo e o identificador único conhecido.

Quando a Movable Ink receber um `user_id` para um único usuário, todos os eventos futuros desse usuário deverão incluir o mesmo `user_id`.

### Compartilhamento de cargas úteis de eventos com o Movable Ink {#event-payloads}

Antes de configurar o conector para a API de dados de cliente da Movable Ink, compartilhe as cargas úteis do evento com a equipe de experiência do cliente da Movable Ink. Isso permite que o Movable Ink mapeie seus eventos para o esquema de eventos deles e evitará qualquer chamada de API rejeitada ou com falha.

Você pode gerar uma carga útil de evento no Braze usando qualquer propriedade de evento. Gere uma carga útil de amostra para um usuário aleatório ou pesquisando um ID de usuário específico. Consulte a [Etapa 1d](#step-1d) acima para obter detalhes.

Compartilhe essa carga útil de amostra com a equipe de experiência do cliente da Movable Ink. Verifique se não há informações confidenciais de identificação pessoal na carga útil da amostra (como endereço de e-mail, número de telefone ou datas de nascimento completas). 

Para saber mais sobre as propriedades de eventos personalizados e o formato esperado dos dados contidos nas propriedades, consulte [Propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

### Usuários conhecidos versus anônimos

Na Braze, os eventos podem ser registrados em um perfil de usuário anônimo. Os identificadores que são vinculados ao perfil do usuário durante o registro de usuários de eventos dependem de como o usuário foi criado (por meio do Braze SDK ou das APIs) e do estágio atual do ciclo de vida do usuário.

#### Encaminhar eventos do Braze apenas para usuários conhecidos

Na sua campanha de webhook, use o filtro `External User ID` para direcionar apenas os usuários que tenham um `external_id` com o filtro `External User ID` `is not blank`.

#### Encaminhamento de eventos do Braze para usuários anônimos e conhecidos

Se quiser encaminhar eventos do Braze de usuários anônimos (usuários antes que um `external_id` seja atribuído ao perfil deles), será necessário decidir qual identificador usar como `anonymous_id` para o Movable Ink até que um `external_id` fique disponível. Escolha um `anonymous_id` que permanecerá constante em seu perfil de usuário Braze. Você pode usar a lógica Liquid no corpo do webhook para decidir se deve passar um `anonymous_id` ou um `user_id`.

Para obter mais informações, consulte os exemplos de webhooks em [exemplos de cargas úteis](#sample-payloads).

## Exemplos de cargas úteis

### Evento de visualização do produto

{% tabs local %}
{% tab Exemplo de evento-gatilho da Braze %}

{% raw %}

```json
{
  "events": [
    {
      "email": "test@braze.com",
      "name": "Product Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "categories": [
          {
            "id": "Bathroom",
            "url": "https://example.com/cat/bathroom"
          }
        ],
        "meta": {
          "color": "green"
        },
        "title": "All-Purpose Cleaning Wipes",
        "price": 1.99,
        "id": "56544",
        "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Carga útil esperada da solicitação da Movable Ink %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "Bathroom",
        "url": "https://example.com/cat/bathroom"
      }
    ],
    "meta": {
      "color": "green"
    },
    "title": "All-Purpose Cleaning Wipes",
    "price": 1.99,
    "id": "56544",
    "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'

```

{% endraw %}
{% endtab %}
{% tab Exemplo de webhook %}

Neste exemplo, um endereço de e-mail com hash é usado como `anonymous_id` para usuários sem `external_id`.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

// Condition logic to determine which identifier to use. If an external_id is available use that, otherwise use the anonymous_id
{% if {{${user_id}}} %}
{% capture user_identifier %}"user_id": "{{${user_id}}}"{% endcapture %}
{% else %}
{% capture user_identifier %}"anonymous_id": "{{anon_id}}"{% endcapture %}
{% endif %}

{
  {{user_identifier}}
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "{{event_properties.${categories}[0].id}}",
        "url": "{{event_properties.${categories}[0].url}}"
      }
    ],
    "meta": {
      "color": "{{event_properties.${meta}.color}}"
    },
    "title": "{{event_properties.${title}}}",
    "price": "{{event_properties.${price}}}",
    "id": "{{event_properties.${id}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
}

```

{% endraw %}
{% endtab %}
{% endtabs %}

### Evento de visualização de categoria

{% tabs local %}
{% tab Exemplo de evento-gatilho da Braze %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Category Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "id": "bathroom-1",
        "title": "Bathroom Stuff",
        "url": "https://www.example.com/categories/bathroom"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Carga útil esperada da solicitação da Movable Ink %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "category_viewed",
  "properties": {
    "id": "bathroom-1",
    "title": "Bathroom Stuff",
    "url": "https://www.example.com/categories/bathroom"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'
```

{% endraw %}

{% endtab %}
{% tab Exemplo de webhook %}

Este exemplo mostra um webhook que rastreia eventos apenas para usuários conhecidos (usuários com `external_id`).

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

{
  "event": "category_viewed",
  "properties": {
    "id": "{{event_properties.${id}}}",
    "title": "{{event_properties.${title}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}

### Identificar o evento

{% tabs local %}
{% tab Exemplo de evento-gatilho da Braze %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Account Created",
      "time": "2023-12-06T19:20:45+01:00"
    }
  ]
}
```

{% endraw %}
{% endtab %}
{% tab Carga útil esperada da solicitação da Movable Ink %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "jg0iq5gd30dqpwn8zmx05p06mzjmjir4r8",
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "identify",
  "user_id": "mycustomerid123"
}'
```

{% endraw %}
{% endtab %}
{% tab Exemplo de webhook %}

Neste exemplo, um endereço de e-mail com hash é usado como `anonymous_id` para usuários sem `external_id`.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

{
  "anonymous_id": "{{anon_id}}",
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "identify",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}



