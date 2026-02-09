---
nav_title: Stripe
article_title: Stripe
description: "Este artigo descreve a parceria entre Braze e Stripe."
alias: /partners/stripe/
page_type: partner
search_tag: Partner
---

# Stripe

> [Stripe](https://www.stripe.com/) é uma plataforma abrangente de infraestrutura financeira que permite que empresas aceitem pagamentos, gerenciem operações de receita e facilitem o comércio global por meio de um conjunto de APIs e serviços integrados.

Ao integrar Braze e Stripe, você pode:

- Atualizar perfis de usuários no Braze com dados de pagamento e faturamento em tempo real do Stripe.
- Disparar mensagens no Braze com base em eventos do Stripe, como início de teste, inscrição ativada, cancelamento de inscrição e mais.
- Personalizar mensagens do Braze com base no histórico de pagamentos ou status de faturamento de um usuário recebido usando webhooks do Stripe.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Stripe | Uma conta do Stripe com acesso a webhooks é necessária para aproveitar esta parceria. |
| Transformação de Dados Braze | Uma [URL de Transformação de Dados]({{site.baseurl}}/data_transformation/) é necessária para receber dados do Stripe. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Configure a Transformação de Dados do Braze para aceitar os webhooks do Stripe {#step-1}

{% multi_lang_include create_transformation.md %}

### Etapa 2: Configurar webhooks do Stripe

Siga os passos na [documentação de webhooks do Stripe](https://docs.stripe.com/development/dashboard/webhooks) para configurar um webhook.

Adicione sua URL de webhook de Transformação de Dados como **URL de Destino** e selecione os tipos de eventos que você gostaria de enviar para o Braze. Consulte [a documentação do Stripe](https://docs.stripe.com/api/events/types) para uma lista completa de tipos de eventos.

![Um exemplo de configuração de webhook do Stripe.]({% image_buster /assets/img/stripe/stripe_webhook_configuration.png %}){: style="max-width:80%;"}

Em seguida, envie um evento de teste para sua Transformação de Dados. 

### Etapa 3: Escreva o código de transformação para aceitar os eventos do Stripe escolhidos

Em seguida, você transformará a carga útil do webhook que será enviada do Stripe para um valor de retorno de objeto JavaScript.

1. Atualize sua Transformação de Dados e certifique-se de que você pode ver a carga útil de teste do Stripe na seção **Detalhes do Webhook**.
2. Atualize seu código de Transformação de Dados para suportar os eventos do Stripe escolhidos.
3. Selecione **Validar** para retornar uma prévia da saída do seu código e verificar se é uma solicitação `/users/track` aceitável.
4. Salve e ative sua Transformação de Dados.

![Um exemplo de detalhes do webhook e código de transformação.]({% image_buster /assets/img/stripe/stripe_data_transformation.png %})

#### Formato do corpo da solicitação

Este valor de retorno deve aderir ao formato do corpo da solicitação do endpoint `/users/track`:

- O código de transformação é aceito na linguagem de programação JavaScript. Qualquer fluxo de controle JavaScript padrão, como a lógica if/else, é aceito.
- O código de transformação acessa o corpo da solicitação do webhook usando a variável payload. Esta variável é um objeto populado pela análise do corpo da solicitação JSON.
- Qualquer recurso aceito em nosso `/users/track` endpoint é aceito, incluindo:
    - Objetos de atributos de usuário, objetos de evento e objetos de compra
    - Atributos aninhados e propriedades de evento personalizado aninhadas
    - Atualizações do grupo de inscrições
    - Endereço de e-mail como um identificador

### Etapa 4: Publique seu webhook do Stripe

Após escrever sua Transformação de Dados, selecione **Validar** para garantir que seu código de Transformação de Dados esteja formatado corretamente e funcionará como esperado. Em seguida, salve e ative sua transformação de dados. Após a ativação, os dados do evento personalizado serão registrados no perfil de um usuário quando ele completar o evento.

![Um evento personalizado do Stripe "Cobrança Bem-Sucedida" em um perfil de usuário do Braze.]({% image_buster /assets/img/stripe/stripe_braze_profile_event.png %}){: style="max-width:80%;"}

## Exemplo de payload do webhook do Stripe {#example}

```json
{
 "headers": {
   "Version": "HTTP/1.1",
   "X-Datadog-Trace-Id": "9124157397962821303",
   "X-Datadog-Parent-Id": "9124157397962821303",
   "X-Datadog-Sampling-Priority": "2",
   "Host": "xxx",
   "X-Request-Id": "xxx",
   "X-Real-Ip": "165.159.72.690",
   "X-Forwarded-For": "161.123.56.890",
   "X-Forwarded-Host": "xxx",
   "X-Forwarded-Port": "443",
   "X-Forwarded-Proto": "https",
   "X-Forwarded-Scheme": "https",
   "X-Scheme": "https",
   "X-Original-Forwarded-For": "12.345.678.123",
   "Cf-Ray": "9470a06172f8816e-IAD",
   "Cache-Control": "no-cache",
   "User-Agent": "Stripe/1.0 (+https://stripe.com/docs/webhooks)",
   "Accept-Encoding": "gzip",
   "Cf-Connecting-Ip": "12.123.456.789",
   "Cf-Visitor": "{\"scheme\":\"https\"}",
   "X-Worker-Executions": "1",
   "Cf-Worker": "xxx",
   "X-Fastly-Geoloc-Countrycode": "US",
   "Stripe-Signature": "t=xxx,v1=xxxx,v0=xxxx",
   "Cf-Ew-Via": "15",
   "Cdn-Loop": "cloudflare; loops=1; subreqs=1",
   "Accept": "*/*; q=0.5, application/xml"
 },
 "payload": {
   "id": "evt_3RTqw0RMEOaIvYpU1k2TFajH",
   "object": "event",
   "api_version": "2025-04-30.basil",
   "created": 1748465448,
   "data": {
     "object": {
       "id": "ch_3RTqw0RMEOaIvYpU1M9ZYtjP",
       "object": "charge",
       "amount": 100,
       "amount_captured": 100,
       "amount_refunded": 0,
       "application": null,
       "application_fee": null,
       "application_fee_amount": null,
       "balance_transaction": null,
       "billing_details": {
         "address": {
           "city": null,
           "country": null,
           "line1": null,
           "line2": null,
           "postal_code": null,
           "state": null
         },
         "email": null,
         "name": null,
         "phone": null,
         "tax_id": null
       },
       "calculated_statement_descriptor": "Stripe",
       "captured": true,
       "created": 1748465448,
       "currency": "usd",
       "customer": "cus_SOeDf39aosGb97",
       "description": "(created by Stripe CLI)",
       "destination": null,
       "dispute": null,
       "disputed": false,
       "failure_balance_transaction": null,
       "failure_code": null,
       "failure_message": null,
       "fraud_details": {},
       "livemode": false,
       "metadata": {},
       "on_behalf_of": null,
       "order": null,
       "outcome": {
         "advice_code": null,
         "network_advice_code": null,
         "network_decline_code": null,
         "network_status": "approved_by_network",
         "reason": null,
         "risk_level": "normal",
         "risk_score": 9,
         "seller_message": "Payment complete.",
         "type": "authorized"
       },
       "paid": true,
       "payment_intent": "pi_3RTqw0RMEOaIvYpU1pQl3Lmp",
       "payment_method": "pm_1RTqw0RMEOaIvYpU5VE8HFlp",
       "payment_method_details": {
         "card": {
           "amount_authorized": 100,
           "authorization_code": null,
           "brand": "visa",
           "checks": {
             "address_line1_check": null,
             "address_postal_code_check": null,
             "cvc_check": "pass"
           },
           "country": "US",
           "exp_month": 5,
           "exp_year": 2026,
           "extended_authorization": {
             "status": "disabled"
           },
           "fingerprint": "HAKdyqJ9xh2YhbzT",
           "funding": "credit",
           "incremental_authorization": {
             "status": "unavailable"
           },
           "installments": null,
           "last4": "4242",
           "mandate": null,
           "multicapture": {
             "status": "unavailable"
           },
           "network": "visa",
           "network_token": {
             "used": false
           },
           "network_transaction_id": "726575100121113",
           "overcapture": {
             "maximum_amount_capturable": 100,
             "status": "unavailable"
           },
           "regulated_status": "unregulated",
           "three_d_secure": null,
           "wallet": null
         },
         "type": "card"
       },
       "radar_options": {},
       "receipt_email": null,
       "receipt_number": null,
       "receipt_url": "https://pay.stripe.com/receipts/payment/xxx",
       "refunded": false,
       "review": null,
       "shipping": null,
       "source": null,
       "source_transfer": null,
       "statement_descriptor": null,
       "statement_descriptor_suffix": null,
       "status": "succeeded",
       "transfer_data": null,
       "transfer_group": null
     }
   },
   "livemode": false,
   "pending_webhooks": 3,
   "request": {
     "id": "req_jqtL1Q6CPaNx8x",
     "idempotency_key": "f0f9aee4-a889-4fcc-bc2e-fa41fa426f05"
   },
   "type": "charge.succeeded"
 }
}
```

## Casos de uso de transformação de dados

Os seguintes são exemplos de modelos construídos usando nosso [exemplo de payload do webhook do Stripe](#example). Esses modelos podem ser usados como ponto de partida. Você pode começar do zero ou excluir componentes específicos conforme achar necessário.

Neste modelo de exemplo, estamos registrando um evento personalizado no perfil do Braze. O tipo de evento será enviado como o nome do evento personalizado, e o objeto de dados será passado como propriedades do evento. 

### Caso de uso: cliente como um identificador

Neste modelo de exemplo, estamos usando o campo cliente como o identificador.

{% tabs local %}
{% tab Input %}

```javascript

/* This template is based on the source platform's documentation here: https://stripe.com/docs/webhooks


/* Braze's /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Stripe's charge succeeded event payload as the event timestamp in Braze must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.data.object.created;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();


/* defines a variable 'brazecall' that will hold the request payload for the /users/track request
let brazecall;


/* if the type is charge.succeeded and customer field is not null, build the /users/track request to log an event to the user profile
if (payload.type == "charge.succeeded" && payload.data.object.customer) {
 brazecall = {
   "events": [
     {
       "external_id": payload.data.object.customer,
       "name": "Charge Succeeded",
       "time": isoString,
       "properties": {
         "amount": payload.data.object.amount,
         "paid": payload.data.object.paid,
         "status": payload.data.object.status
       }
     }
   ]
 };
}
/* After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Output %}

```json
{
  "events": [
    {
      "external_id": "an_account@example.com",
      "name": "Charge Succeeded",
      "time": "2025-05-28T18:21:39.527Z",
      "properties": {
        "amount": 100,
    "paid":true,
    "Status":"succeeded"
    }
   }
  ]
}
```

{% endtab %}
{% endtabs %}

## Monitoramento e solução de problemas

Consulte [Monitorando sua transformação]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation/#step-5-monitor-your-transformation) para mais informações sobre monitoramento e solução de problemas da sua transformação.
