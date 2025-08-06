--- 
nav_title: SessãoM
article_title: SessãoM
description: "Este artigo de referência descreve a parceria entre o Braze e a SessionM, uma plataforma de engajamento com clientes e fidelidade."
alias: /partners/sessionm/
page_type: partner
search_tag: Partner
--- 

# Plataforma de fidelidade SessionM

> A [SessionM](https://www.mastercardservices.com/en/capabilities/sessionm) é uma plataforma de engajamento com clientes e fidelidade que oferece recursos de gerenciamento de campanhas e soluções de gerenciamento de fidelidade para ajudar os profissionais de marketing a impulsionar o direcionamento para aumentar o engajamento e a lucratividade.

## Pré-requisitos

| Origem | Requisito | Descrição |
| --- | --- | --- |
| Braze | Uma chave da API REST da Braze | Uma chave da API REST da Braze com `trigger_send` permissões. Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Braze | Um endpoint Braze REST | Sua URL de endpoint REST. Seu endpoint dependerá do [URL da Braze para [sua instância]({{site.baseurl}}/api/basics/#endpoints). |
| Braze e SessionM | Identificador de correspondência | Para usar a integração, certifique-se de que tanto a SessionM quanto o Braze tenham um registro dos identificadores usados por cada plataforma. As referências a `user_id` correspondem ao identificador de usuário da SessionM gerado no momento da criação do perfil na SessionM. |
| SessãoM | Uma conta SessionM | É necessário ter uma conta SessionM para aproveitar essa parceria. |
| SessãoM | Um endpoint REST do SessionM Core | Seu endpoint dependerá do URL SessionM da sua instância. Isso pode ser criado no dashboard do SessionM em **Digital Properties**. |
| SessãoM | Uma chave da API REST do SessionM Core | A chave da API SessionM associada à sua instância e à integração do Braze. Essa chave pode ser usada para todas as chamadas baseadas em núcleo, inclusive tags. Isso pode ser criado no dashboard do SessionM em **Digital Properties**. |
| SessãoM | Um segredo da API REST do SessionM Core | O segredo da API SessionM associado à sua instância e à integração do Braze. Essa chave pode ser usada para todas as chamadas baseadas em núcleo, inclusive tags. Isso pode ser criado no dashboard do SessionM em **Digital Properties**. |
| SessãoM | Um ponto de extremidade REST do SessionM Connect | Seu endpoint dependerá do URL SessionM da sua instância. Entre em contato com o gerente técnico de contas da SessionM ou com a equipe de entrega para fornecer informações. |
| SessãoM | Uma string de autorização REST do SessionM Connect | A string de autorização básica do SessionM Connect associada à sua instância. Essa string de autenticação pode ser usada para todas as chamadas baseadas em conexão, incluindo get_user_offers. Entre em contato com o gerente técnico de contas da SessionM ou com a equipe de entrega para fornecer informações. |
| SessãoM | Um ID de varejista do SessionM Connect REST | Uma identificação de guid exclusiva para o cliente específico associado à sua instância. Entre em contato com o gerente técnico de contas da SessionM ou com a equipe de entrega. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), poderá criar uma chave de API em **Console do desenvolvedor** > **Configurações de API**.
{% endalert %} 

## Casos de uso

Os casos de uso a seguir mostram algumas maneiras de aproveitar a integração da SessionM e do Braze.

- Crie uma segmentação que incorpore dados em todas as plataformas de fidelidade, gestão de clientes e envio de mensagens.
- Use a segmentação robusta para direcionar conjuntos específicos de usuários com ofertas e promoções.
- Aproveite as informações mais atualizadas sobre usuários, ofertas e fidelidade ao enviar mensagens.
- Fornecer notificações detalhadas aos clientes sobre o progresso e a conclusão das atividades promocionais e de fidelidade.
- Notifique os clientes quando uma nova oferta for concedida e forneça os detalhes da oferta.

## Integração da SessionM com o Braze

### Etapa 1: Criar um segmento no Braze

No Braze, crie um segmento de usuários para direcionamento com promoções e ofertas da SessionM. 

![Criador de segmentos com o filtro "Atributos personalizados" selecionado.]({% image_buster /assets/img/sessionm/CreateSegment.png %})

### Etapa 2: Importar segmentos do Braze para a SessionM

#### Opção 1: Exportar para o endpoint SessionM Tag (recomendado)

Primeiro, crie uma campanha de webhook no Braze e defina o URL do webhook como {% raw %}`{{endpoint_core}}/priv/v1/apps/{{appkey_core}}/users/{{${user_id}}}/tags`{% endraw %}. Use Liquid para definir o endereço `user_id` no URL. 

Usando um **corpo de solicitação** de texto bruto, crie o corpo do webhook para incluir as tags desejadas a serem adicionadas ao perfil do usuário na SessionM e o TTL desejado. Um exemplo é:

 ```
 {
   "tags":[
    "braze_test"
   ],
   "ttl":2592000
}
 ```

![]({% image_buster /assets/img/sessionm/SessionMWebhookComposer.png %}){: style="max-width:85%;"}

Na guia **Configurações**, adicione os pares de valores-chave para cada campo de cabeçalho de solicitação:
    \- Criar uma chave `Content-Type` com um valor correspondente `application/json`
    \- Crie uma chave `Authorization` com um valor correspondente `Basic YOUR-ENCODED-STRING-KEY`. Entre em contato com a equipe da SessionM para obter a chave de string codificada para o seu endpoint. 

![Configurações de webhook.]({% image_buster /assets/img/sessionm/SessionMWebhookSettings.png %}){: style="max-width:85%;"}

Programe sua entrega, defina seu **público-alvo** para direcionamento ao segmento [que você criou anteriormente](#step-1-create-a-segment-in-braze) e, em seguida, lance sua campanha.

{% alert important %}
Esse processo também pode ser feito por meio de um cliente API, como o Postman, fazendo uma solicitação diretamente ao [endpoint SessionM Tag](https://docs.sessionm.com/developer/APIs/Core/Customers/customers_tags.htm#create-or-increment-a-customer-tag), especificando o cliente, o nome da tag e um TTL para cada usuário na chamada (um único usuário por chamada).
<br><br>
O exemplo de solicitação a seguir usa cURL. 

{% raw %}
```bash
curl --location -g --request POST '{{endpoint_core}}/priv/v1/apps/{{apikey_core}}/users/{{user_id}}/tags' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic {{base64_encoded_string}}' \
--data-raw '{
"tags":[
"tagname1",
"tagname2"
],
"ttl":20000
}'
```
{% endraw %}
{% endalert %}

#### Opção 2: importação de CSV

Exporte seu segmento do Braze usando o segmentador do Braze e forneça um arquivo CSV ao SessionM que contenha os clientes a serem marcados, o nome da tag e um TTL para cada usuário no arquivo.

## Recuperação da carteira de ofertas em tempo real com o Braze

A integração do SessionM com o Braze permite a extração em tempo real dos dados de usuários do SessionM no momento do envio da mensagem, usando o Connected Content, para eliminar o risco de comunicar aos clientes ofertas de fidelidade desatualizadas, expiradas ou já resgatadas. 

O exemplo a seguir mostra o Connected Content sendo usado para modelar dados da carteira de ofertas em uma mensagem. No entanto, o Connected Content pode ser usado com qualquer um dos pontos de extremidade Connect da SessionM. 

### Etapa 1: Emitir oferta na SessionM

A SessionM emite ofertas para os clientes a partir de várias alavancas internas diferentes que podem ser configuradas. Após serem emitidas, as ofertas são movidas para um estado que a SessionM chama de "carteira de ofertas".

O cliente deve concluir a ação necessária ou atender ao direcionamento e a oferta é emitida na SessionM.

Em seguida, a SessionM adiciona a oferta à carteira do cliente no estado emitido.

### Etapa 2: Chamar a API SessionM Offer Wallet

Na etapa da campanha ou do Canva com as ofertas da SessionM, use o [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) para fazer uma chamada de API para o [endpoint da SessionM `get_user_offers` ](https://domains-connecteast1.ent-sessionm.com/offers/swagger/ui/index#!/InfoV232583210323232323232323232323232This32API32allows32for32the32querying32of32information32about32offers32in32a32read45only32fashion4610323232323232323232323232May32be32initiated32by32the32dashboard32or32the32mobile32app4610323232323232323232323232/InfoV2_GetUserOffers/).

Na solicitação Connected Content, especifique a SessionM `user_id` do usuário e sua `retailer_id` para recuperar a lista completa de ofertas ativas que o cliente tem em sua carteira. Cada solicitação a esse endpoint pode incluir um único usuário. Entre em contato com a equipe do SessionM para obter a chave de string codificada para o cabeçalho de autorização básica na sua chamada de Connected Content.

No corpo da solicitação, `culture` tem como padrão `en-US`, mas é possível usar o Liquid para modelar o idioma de um usuário para ofertas multilíngues da SessionM (por exemplo, usando {% raw %}`"culture":"{{${language}}}"`{% endraw %}).

{% raw %}
```
{% capture postbody %}
{"retailer_id":"YOUR-RETAIL-ID","user_id":"{{${user_id}}}","skip":0,"take":1000,"include_pending_extended_data":false,"culture":"en-US"}
{% endcapture %}

{% connected_content
     {{endpoint_connect}}/offers/api/2.0/offers/get_user_offers
:method post     
:headers {
       "Content-Type": "application/json",
       "Authorization": "Basic YOUR-BASE64-ENCODED-KEY"
  }
     :body {{postbody}}
     :save wallet
%}
```
{% endraw %}

### Etapa 3: Preencher a carteira de ofertas para envio de mensagens do Braze

Depois que uma solicitação é feita ao ponto de extremidade, o SessionM retorna a lista completa de ofertas no estado emitido, juntamente com os detalhes completos de cada oferta. Este é um exemplo de resposta retornada:

{% raw %}
```
{
    "status": "ok",
    "payload": {
      "user": {
        "opted_in": false,
        "activated": false,
        ...
      },
      "user_id": "00000000-0000-0000-0000-000000000000",
      "user_offers": [
        {
          "offer_id": "1a2b3324-1da6-4e49-b921-afc386dabb60",
          "offer_group_id": "00000000-0000-0000-0000-000000000000",
          "offer_type": "manual_fulfillment",
          ...
        }
      ],
      "total_records": 1,
      "offer_groups": [
        {
          "id": "00000000-0000-0000-0000-000000000000",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "offer_categories": [
        {
          "id": "9a82f973-aae6-4e10-839b-7117a852cf9e",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "total_points": 1000,
      "available_points": 100
    }
}
```
{% endraw %}

Usando a notação de ponto Liquid, isso pode ser preenchido na mensagem. Por exemplo, para personalizar a mensagem com o resultado `offer_id`, você pode aproveitar a carga útil de retorno usando {% raw %}`{{wallet.payload.available_points}`{% endraw %}, que retorna `100`.

{% alert note %}
Essa é uma API individual. Se pretender enviar um lote de mais de 500 usuários, entre em contato com a equipe da conta SessionM para saber como incorporar dados em massa na integração.
{% endalert %}

## Configuração do envio de mensagens disparadas

A integração entre a SessionM e o Braze permite que os dados do perfil do usuário, os detalhes da oferta e os saldos de pontos sejam preenchidos dinamicamente no envio de mensagens e enviados em tempo real para o cliente no ponto de ação.

### Etapa 1: A equipe de entrega da SessionM configura os modelos

Colabore com a equipe de entrega da SessionM para desenvolver modelos a serem usados no envio de mensagens disparadas. A SessionM inserirá dados do perfil do usuário, detalhes da oferta e saldos de pontos nas mensagens e as disparará no Braze para envio de mensagens em tempo real para o cliente.

Os campos padrão presentes em todos os modelos da SessionM incluem:
- `canvas_id`
- `campaign_id`
- `broadcast flag`
- `customer identifier`
- `email address`

{% alert note %}
Ao definir o endereço `broadcast flag` como `true`, a mensagem será enviada para todo o segmento que a campanha ou o Canva direciona no Braze.
{% endalert %}

Campos adicionais podem ser configurados com base em necessidades específicas:

- **Dados da oferta:** `offer_id`, `offer title`, `user offer id`, `description`, `terms and conditions`, `logo`, `pos discount id`, `expiration date`
- **Dados do prêmio por pontos:** `point award amount`, `point account name`
- **Dados do evento de gatilho:** Qualquer dado no evento de gatilho que utilize o resultado do webhook de disparo/envio
- **Dados específicos da campanha:** `campaign runtime`, `campaign_id`, `campaign name`, `campaign custom data`

Campos adicionais são enviados ao Braze como `trigger_properties` para personalizar a mensagem. 

### Etapa 2: Criar uma campanha ou uma tela do Braze

Crie uma campanha acionada pela API ou uma tela no Braze para ser disparada pela SessionM. Se campos adicionais tiverem sido configurados, como `offer_id` ou `offer title`, use Liquid (como {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %}) para adicionar os campos personalizados em seu envio de mensagens.

![Propriedades do disparador da API.]({% image_buster /assets/img/sessionm/apiTriggerProperties.png %})

Na guia **Schedule Delivery (Entrega de agendamento)**, anote o ID da campanha ou do Canva, pois ele será adicionado às **Advanced Settings (Configurações avançadas)** da campanha SessionM.

![Campanha disparada pela API.]({% image_buster /assets/img/sessionm/apiTriggerCampaign.png %})

Finalize os detalhes de sua campanha ou do Canva e selecione **Launch (Iniciar)**. 

### Etapa 3: Criar uma campanha promocional ou de envio de mensagens da SessionM

Em seguida, crie sua campanha na SessionM.

![Criação da campanha SessionM.]({% image_buster /assets/img/sessionm/SessionMCampaignCreation.png %})

Atualize as configurações avançadas na campanha SessionM para incluir a seguinte carga útil JSON contendo `braze_campaign_id` ou `braze_canvas_id`.

{% raw %}
```
{
"braze_campaign_id": "{{CAMPAIGN ID}}",
"braze_canvas_id": "{{CANVAS ID}}",
}
```
{% endraw %}

![Configurações avançadas da SessionM.]({% image_buster /assets/img/sessionm/SessionMAdvancedSettings.png %}){: style="max-width:85%;"}

Crie um disparo de mensagens sobre a programação ou o comportamento desejado. Em seguida, selecione **Braze Messaging Variant** como a **variante de envio de mensagens** no menu **External Message** para usar o modelo.

![Envio de mensagens externas da SessionM.]({% image_buster /assets/img/sessionm/SessionMExternalMessage.png %})

Esse modelo extrai as atribuições estáticas e dinâmicas relevantes e chama o ponto de extremidade do Braze.

![Modelo SessionM Braze.]({% image_buster /assets/img/sessionm/SessionMBrazeTemplate.png %}){: style="max-width:85%;"}
