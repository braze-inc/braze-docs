---
nav_title: Frente
article_title: Frente
description: "Saiba como integrar o Front ao Braze"
alias: /partners/front/
page_type: partner
search_tag: Partner

---

# Frente

> A integração da Front o capacita a aproveitar a transformação de dados do Braze e os webhooks de cada plataforma para configurar um pipeline de SMS de conversação bidirecional.

O webhook de entrada do Front conterá uma carga útil que inclui a mensagem enviada pelo agente em tempo real. A solicitação precisará ser reformatada antes de ser aceita pelos endpoints do Braze. O modelo Front Data Transformation reformatará a carga útil de **SMS** e gravará um evento personalizado no perfil do usuário intitulado **Outbound SMS Sent,** com o corpo da mensagem sendo passado como uma propriedade do evento.

Antes de configurar uma nova transformação no Braze, recomendamos revisar a matriz de suporte para cada camada em nossa documentação de [transformação de dados]({{site.baseurl}}/user_guide/data/data_transformation/overview/). Nossos níveis Free e Pro oferecem um número diferente de transformações ativas e solicitações de entrada por mês. Confirme se o plano atual em que você está pode suportar seu caso de uso.

## Pré-requisitos

Antes de começar, você precisará do seguinte:

| Pré-requisito             | Descrição                                                               |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Um relato da Front            | É necessário ter uma conta Front para usar a parceria.|
| URL do webhook de transformação de dados do Braze | [A transformação de dados do Braze]({{site.baseurl}}/user_guide/data/data_transformation/overview/) será usada para reformatar o webhook de entrada do Front para que ele possa ser aceito pelo endpoint Braze /users/track.|
| Uma chave da API REST do Front         | Uma chave da API REST da Front será usada para fazer uma solicitação de webhook de saída da Braze para a Front. |

## Casos de uso

- Simplifique seu processo de geração de leads usando o envio automatizado de mensagens SMS da Braze para identificar as preferências do usuário e ativar os agentes de vendas para acompanhar e fechar as vendas.
- Reengaje os clientes que abandonaram seus carrinhos de compras, impulsionando as conversões de vendas por meio de respostas automatizadas por SMS e suporte por bate-papo ao vivo.

## Integração da Front

### Etapa 1: Criar uma transformação de dados

Primeiro você criará uma nova transformação de dados na Braze. As etapas a seguir são simplificadas; para obter um passo a passo completo, consulte [Criação de uma transformação]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation/).

1. No Braze, acesse **Configurações de dados** > **Transformações de dados** e selecione **Criar transformação**.
2. Em **Editing Experience**, selecione **Start from scratch (Começar do zero**).
3. Em **Select Destination (Selecionar destino**), selecione **POST: Rastreamento de usuários**.
4. Copie e cole o seguinte modelo de transformação e depois salve e ative o endpoint.
    {% raw %}
    ```liquid

    // This is a default template that you can use as a starting point. Feel free to delete this entirely to start from
    // scratch, or to delete specific components as you see fit

    // First, this code defines a variable, "brazecall", to build up a /users/track request
    // Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in
    // desired values in your /users/track request with JS dot notation, such as payload.x.y.z

    let brazecall = {
    "events": [
      {
      "phone": payload.recipients[1].handle,
      "_update_existing_only": true,
      "name": "Outbound SMS Sent",
      "time": new Date().toISOString(),
      "properties": {
        "message_id": payload.id,
        "message_body": payload.body,
        "front_author_username": payload.author.username
      }
      }
    ]
    };

    // After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
    return brazecall;
    ```
    {% endraw %}

    Sua transformação deve ser semelhante à seguinte:

    ![Um exemplo de transformação de dados.]({% image_buster /assets/img/front/data_transformation.png %})

{% alert tip %}
Você pode modificar esse modelo para atender às suas necessidades específicas. Por exemplo, você pode personalizar o nome do evento personalizado predefinido. Para saber mais, consulte [Visão geral da transformação de dados]({{site.baseurl}}/user_guide/data/data_transformation/overview/).
{% endalert %}

### Etapa 2: Criar uma campanha de SMS de saída

Em seguida, você criará uma campanha de SMS que ouvirá webhooks do Front e uma resposta de SMS personalizada para seus clientes.

#### Etapa 2.1: Crie sua mensagem

Na caixa de texto **Mensagem**, adicione o seguinte código Liquid, juntamente com qualquer linguagem de aceitação ou outro conteúdo estático.

{% raw %}
```liquid
{{event_properties.${message_body}}}
```
{% endraw %}

Sua mensagem deve ser semelhante à seguinte:

![Um exemplo de mensagem usando o código Liquid.]({% image_buster /assets/img/front/sms_to_braze.png %}){: style="max-width:80%;"}

#### 2.2 Programar a entrega

Para o tipo de entrega, selecione **Entrega baseada em ação**; em seguida, para o disparo de evento personalizado, selecione **SMS de saída enviado**.

![A página "Schedule Delivery".]({% image_buster /assets/img/front/custom_event_trigger.png %})

{% alert note %}
Esse evento personalizado é a transformação de dados que grava no perfil do usuário. As mensagens do agente serão salvas como uma propriedade de evento nesse evento.
{% endalert %}

Por fim, em **Controles de entrega**, ative a reelegibilidade.

![Reelegibilidade ativada em "Controles de entrega".]({% image_buster /assets/img/front/braze_reeligibility.png %})

### Etapa 3: Criar um canal personalizado

No painel frontal, acesse **Settings** > **Channels** > **Add Channels** (Configurações > Canais > Adicionar canais), selecione **Custom Channel** (Canal personalizado ) e digite um nome para seu novo canal do Braze.

![Um canal personalizado para Braze no painel frontal.]({% image_buster /assets/img/front/front_custom_channel.png %})

### Etapa 4: configurar as definições

No campo endpoint da API de saída, digite o URL do webhook de transformação de dados [que você criou antes](#step-1-set-up-a-data-transformation-in-braze). Todas as mensagens enviadas por agentes ao vivo em seu novo canal do Braze serão enviadas para cá. Esse canal também fornece um URL de endpoint para o Braze encaminhar mensagens SMS no campo **URL de entrada**.

Não se esqueça de anotar esse URL - você precisará dele mais tarde.

![As configurações de canal para o canal Braze recém-criado em Front.]({% image_buster /assets/img/front/front_custom_channel2.png %}){: style="max-width:65%;"}

### Etapa 5: Configurar o encaminhamento de SMS de entrada

Em seguida, você criará duas novas campanhas de webhook no Braze para que possa encaminhar SMS recebidos de clientes para a caixa de entrada do Front.

|Número|Finalidade|
|---|---|
|Campanha de webhook 1|Sinaliza à Front que uma conversa de bate-papo ao vivo está sendo solicitada.|
|Campanha de webhook 2|Encaminha todas as respostas de SMS de conversação enviadas pelo cliente para a caixa de entrada do Front.|
{: .reset-td-br-1 .reset-td-br-2 }

#### Etapa 5.1: Criar uma categoria de palavra-chave SMS

No dashboard do Braze, acesse **Público**, escolha seu **grupo de inscrições de SMS** e selecione **Adicionar palavra-chave personalizada**. Para criar uma categoria de palavra-chave de SMS exclusiva para o Front, preencha os campos a seguir.

|Campo|Descrição|
|---|---|
|Categoria da palavra-chave|O nome da categoria da palavra-chave, como `FrontSMS1`.|
|Palavras-chave|Suas palavras-chave personalizadas, como `TIMETOMOW`. Evite palavras comuns para evitar disparos acidentais. Lembre-se de que as palavras-chave não diferenciam maiúsculas de minúsculas, portanto, `lawn` corresponderia a `LAWN`.|
|Mensagem de resposta|A mensagem que será enviada quando uma palavra-chave for detectada, como "Um paisagista entrará em contato com você em breve".|
{: .reset-td-br-1 .reset-td-br-2 }

![Um exemplo de categoria de palavra-chave SMS no Braze.]({% image_buster /assets/img/front/front_keyword.png %}){: style="max-width:65%;"}

#### Etapa 5.2: Crie sua primeira campanha de webhook

No dashboard do Braze, crie sua primeira campanha de webhook usando o URL [que você criou anteriormente](#step-3-configure-the-settings-for-your-new-custom-braze-channel).

![Um exemplo da primeira campanha de webhook que deve ser criada no Braze.]({% image_buster /assets/img/front/sms_to_front.png %}){: style="max-width:65%;"}

Adicione o seguinte ao corpo da solicitação:

{% raw %}
```liquid
{ 
 "sender": {
  "handle": "{{${phone_number}}}",
  "name": "{{${user_id}}}"
 },
 "body_format": "markdown",
 "metadata": {
  "headers": {
   "first_name": "{{${first_name}}}",
   "last_name": "{{${last_name}}}"
  }
 },
 "body": "{{sms.${inbound_message_body} | default : "no body available" }}"
}
```
{% endraw %}

Na guia “Settings” (Configurações), configure os cabeçalhos de solicitação `Authorization`, `content-type` e `accept`.

![Um exemplo de solicitação com os três cabeçalhos necessários.]({% image_buster /assets/img/front/webhook_settings.png %}){: style="max-width:65%;"}

#### Etapa 5.3: Agendar a primeira entrega

Em **Entrega programada**, selecione **Entrega baseada em ação** e, em seguida, escolha **Enviar uma mensagem de entrada SMS** para o tipo de disparo. Adicione também o grupo de inscrições de SMS e a categoria de palavras-chave que você [configurou anteriormente](#step-51-create-an-sms-keyword-category).

![A página "Schedule Delivery" da primeira campanha de webhook.]({% image_buster /assets/img/front/front_actionbased_keyword.png %})

Em **Controles de entrega**, ative a reelegibilidade.

![Reelegível selecionado em "Delivery Controls" (Controles de entrega) para a primeira campanha de webhook.]({% image_buster /assets/img/front/braze_reeligibility.png %})

#### Etapa 5.4: Crie sua segunda campanha de webhook

Como sua segunda campanha de webhook corresponderá à primeira, você pode [duplicar a primeira e renomeá-la]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/#duplicating-segments-or-campaigns). Você pode fazer isso agora.

#### Etapa 5.5: Agendar a segunda entrega

Para **Programar entrega**, defina o **disparo baseado em ação** e o **grupo de inscrições de SMS** como os mesmos da [primeira entrega](#step-53-schedule-the-first-delivery). Entretanto, para a **categoria de palavra-chave**, escolha **Other** (Outra).

![A página "Scheduled Delivery" (Entrega programada) da segunda campanha de webhook, com "Other" (Outro) escolhido como a categoria de palavra-chave.]({% image_buster /assets/img/front/front_actionbased_other_keyword.png %})

#### Etapa 5.6: Adicionar um filtro de público

Sua campanha de webhook agora pode encaminhar respostas de SMS recebidas de seus clientes. Para filtrar as respostas de SMS de modo que somente as mensagens de chats ativos sejam encaminhadas, adicione o filtro de segmentação **Last Received Message From Specific Campaign** à **etapa de públicos-alvo**.

![Um filtro de público com a opção "Última mensagem recebida de uma campanha específica" selecionada.]({% image_buster /assets/img/front/front_segment_last_received_message.png %}){: style="max-width:65%;"}

Em seguida, configure seu filtro:

1. Em **Campaign (Campanha**), selecione a campanha de SMS [que você criou anteriormente](#step-2-create-an-outbound-sms-campaign).
2. Em **Operador**, selecione **Menor que**.
3. Em **Janela de tempo**, escolha o período de tempo em que o bate-papo deve permanecer aberto sem uma resposta do cliente.

![As definições de configuração do filtro de público selecionado.]({% image_buster /assets/img/front/front_target_audience.png %})

## Considerações

### Segmentos faturáveis

- As mensagens SMS no Braze são cobradas por segmento de mensagem. Entender o que define um segmento de mensagens e como essas mensagens serão divididas é fundamental para entender como você será cobrado pelas mensagens. Para saber mais, consulte nossa [documentação]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/).
- Respostas longas dos agentes consumirão mais segmentos faturáveis.

### Consumo de pontos de dados

No momento, a integração exige que um evento personalizado seja gravado em um perfil de usuário toda vez que um agente envia um SMS pela Front. Isso pode ser adequado para trocas rápidas que duram apenas algumas mensagens, mas à medida que as conversas se tornam mais longas, o mesmo acontece com as implicações dos pontos de dados. Um ponto de dados é consumido para cada evento personalizado registrado no Braze.

### Inclusão de links em mensagens SMS

O envio de um link do bate-papo ao vivo da Front será renderizado com tags HTML extras.

### Anexar arquivo de imagem pela Front

Os arquivos de imagem no Front não serão renderizados em mensagens SMS enviadas pelo Braze.

### Aceitação 

As mensagens de conversação têm um risco maior de conter a palavra "pare" ou outra semelhante que possa ser reconhecida como uma cancelamento de inscrição impreciso.
