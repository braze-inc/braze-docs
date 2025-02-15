---
nav_title: Lob
article_title: Lob 
alias: /partners/lob/
description: "Este artigo de referência descreve a parceria entre a Braze e o Lob.com, que permite o envio de mala direta, como cartas, cartões postais e cheques pelo correio."
page_type: partner
search_tag: Partner

---

# Lob

> [Lob.com][38] é um serviço on-line que permite o envio de mala direta aos seus usuários.

A integração entre a Braze e a Lob utiliza os webhooks da Braze e a API da Lob para enviar correspondências, como cartas, cartões postais e cheques pelo correio.  

## Pré-requisitos

|Requisito| Descrição|
| ---| ---|
|Conta da Lob | É necessário ter uma conta Lob para aproveitar essa parceria. |
| Chave de API do Lob | A sua chave de API da Lob pode ser encontrada na seção de configurações, abaixo do seu nome, no dashboard da Lob. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: selecione o endpoint da Lob

O URL HTTP a ser solicitado no webhook é diferente para cada ação que você pode realizar no Lob. No exemplo a seguir, usamos o endpoint da API de cartões postais `https://api.lob.com/v1/postcards`. Visite a [lista completa de endpoints][39] para selecionar o endpoint apropriado para seu caso de uso. 

| Endpoint de API | Pontos de extremidade disponíveis |
| ------------ | ------------------- |
| https://api.lob.com/ | /v1/addresses<br>/v1/addresses/{id}<br>/v1/verify<br>/v1/postcards<br>/v1/postcards/{id}<br>/v1/letter<br>/v1/letter/{id}<br>/v1/checks<br>/v1/checks/{id}<br>/v1/bank_accounts<br>/v1/bank_accounts/{id}<br>/v1/bank_accounts/{id}/verify<br>/v1/areas<br>/v1/areas/{id}<br>/v1/routes/{zip_code}<br>/v1/routes<br>/v1/countries<br>/v1/states|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapa 2: Crie seu modelo de webhook do Braze

Para criar um modelo de webhook Lob para ser usado em futuras campanhas ou Canvas, navegue até **Modelos** > **Modelos de webhook** na plataforma Braze. 

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), acesse **Engajamento** > **Modelos e mídias** > **Modelos de webhook**.
{% endalert %}

Se quiser criar uma campanha única de webhook no Lob ou usar um modelo existente, selecione **Webhook** no Braze ao criar uma nova campanha.

Em seu novo modelo de webhook, preencha os seguintes campos:
- **URL do webhook**: `<LOB_API_ENDPOINT>`
- **Corpo da solicitação**: Texto bruto

#### Cabeçalhos de solicitação e método

A Lob requer um cabeçalho HTTP para autorização e um método HTTP. O seguinte já estará incluído no modelo como um par de valores chave, mas na guia **Settings (Configurações)**, você deve substituir o `<LOB_API_KEY>` pela sua chave de API do Lob. Essa chave deve incluir um ":" logo após a chave e ser codificada em base 64. 

- **Método HTTP**: POST
- **Cabeçalhos de solicitação**:
  - **Autorização**: Básico `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Content-Type**: application/json

![O código do corpo da solicitação e o URL do webhook são exibidos na guia de composição do criador de webhooks do Braze.][35]

#### Corpo da solicitação

A seguir, um exemplo de corpo de solicitação para o endpoint de cartões postais da Lob. Esse corpo de solicitação seja fornecido no modelo básico da Lob na Braze, mas você deverá ajustar seus campos Liquid se desejar usar outros endpoints.

```json
{% raw %}"description": "Demo Postcard",
"to": {
    "name": "{{${first_name}}} {{${last_name}}}",
    "address_line1": "{{custom_attribute.${address_line1}}}",
    "address_city": "{{custom_attribute.${address_city}}}",
    "address_zip": "{{custom_attribute.${address_zip}}}",
    "address_country": "{{custom_attribute.${address_country}}}"
},
"front": "https://lob.com/postcardfront.pdf",
"back": "https://lob.com/postcardback.pdf"{% endraw %}
```

### Etapa 3: veja uma prévia da sua solicitação

Nesse ponto, sua campanha deve estar pronta para ser testada e enviada. Verifique o dashboard do Lob e os registros de mensagens de erro do console de desenvolvedor do Braze se encontrar erros. Por exemplo, o erro a seguir foi causado por um cabeçalho de autenticação formatado incorretamente. 

![Um registro de erros de mensagens que mostra a hora, o nome do app, o canal e a mensagem de erro. A mensagem de erro inclui o alerta de mensagem e o código de status.][36]

{% alert important %}
Lembre-se de salvar seu modelo antes de sair da página! <br>Os modelos de webhook atualizados podem ser encontrados na lista **Modelos de webhook salvos** ao criar uma nova [campanha de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}

[33]: {% image_buster /assets/img_archive/lob_api_key.png %}
[34]: {% image_buster /assets/img_archive/lob_success_response.png %}
[35]: {% image_buster /assets/img_archive/lob_full_request.png %}
[36]: {% image_buster /assets/img_archive/error_log.png %}
[37]: {% image_buster /assets/img_archive/lob_api_endpoint.png %}
Daqui a [38]: https://lob.com
Daqui a [39]: https://lob.com/docs#intro
Daqui a [40]: https://lob.com/docs#auth
