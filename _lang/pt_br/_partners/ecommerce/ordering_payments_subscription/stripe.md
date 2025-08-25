---
nav_title: Listrado
article_title: Listrado
description: "Este artigo descreve a parceria entre a Braze e a Stripe."
alias: /partners/stripe/
page_type: partner
search_tag: Partner
---

# Listrado

> [A Stripe](https://www.stripe.com/) é uma plataforma abrangente de infraestrutura financeira que ativa as empresas para aceitar pagamentos, gerenciar operações de receita e facilitar o comércio global por meio de um conjunto de APIs e serviços integrados.

Ao integrar o Braze e o Stripe, você pode:

- Atualize os perfis de usuários no Braze com dados de pagamento e faturamento em tempo real do Stripe.
- Dispare envios de mensagens no Braze com base em eventos do Stripe, como início de avaliação, ativação de inscrição, cancelamento de inscrição e muito mais.
- Personalize o envio de mensagens do Braze com base no histórico de pagamentos de um usuário ou no status de faturamento recebido usando os webhooks do Stripe.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Stripe | É necessário ter uma conta Stripe com acesso a webhooks para aproveitar essa parceria. |
| Transformação de Dados Braze | É necessário um [URL de transformação de dados]({{site.baseurl}}/data_transformation/) para receber dados do Stripe. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Configure a transformação de dados do Braze para aceitar os webhooks do Stripe {#step-1}

{% multi_lang_include create_transformation.md %}

### Etapa 2: Configurar webhooks do Stripe

Siga as etapas da [documentação dos webhooks do Stripe](https://docs.stripe.com/development/dashboard/webhooks) para configurar um webhook.

Adicione o URL do webhook de transformação de dados como o **URL de destino** e selecione os tipos de eventos que deseja enviar ao Braze. Consulte [a documentação do Stripe](https://docs.stripe.com/api/events/types) para obter uma lista completa dos tipos de eventos.

![Um exemplo de configuração de webhook do Stripe.]({% image_buster /assets/img/stripe/stripe_webhook_configuration.png %}){: style="max-width:80%;"}

Em seguida, envie um evento de teste para sua transformação de dados. 

### Etapa 3: Escreva o código de transformação para aceitar seus eventos Stripe escolhidos

Em seguida, você transformará a carga útil do webhook que será enviada pelo Stripe em um valor de retorno de objeto JavaScript.

1. Atualize a Transformação de dados e verifique se é possível ver a carga útil do teste do Stripe na seção **de detalhes do Webhook**.
2. Atualize seu código de transformação de dados para dar suporte aos eventos Stripe escolhidos.
3. Selecione **Validar** para retornar uma prévia da saída do seu código e verificar se é uma solicitação `/users/track` aceitável.
4. Salve e ative sua Transformação de Dados.

![Um exemplo de detalhes de webhook e código de transformação.]({% image_buster /assets/img/stripe/stripe_data_transformation.png %})

#### Formato do corpo da solicitação

Esse valor de retorno deve estar de acordo com o formato do corpo da solicitação do ponto de extremidade `/users/track`:

- O código de transformação é aceito na linguagem de programação JavaScript. Qualquer fluxo de controle JavaScript padrão, como a lógica if/else, é aceito.
- O código de transformação acessa o corpo da solicitação do webhook usando a variável de carga útil. Esta variável é um objeto populado pela análise do corpo da solicitação JSON.
- Qualquer recurso aceito em nosso `/users/track` endpoint é aceito, incluindo:
    - Objetos de atribuição do usuário, objetos de evento e objetos de compra
    - Atributos aninhados e propriedades de evento personalizado aninhadas
    - Atualizações do grupo de inscrições
    - Endereço de e-mail como um identificador

### Etapa 4: Publique seu webhook do Stripe

Depois de escrever sua transformação de dados, selecione **Validar** para garantir que o código da transformação de dados esteja formatado corretamente e funcione conforme o esperado. Em seguida, salve e ative sua transformação de dados. Após a ativação, os dados de eventos personalizados serão registrados no perfil do usuário quando ele concluir o evento.

![Um evento personalizado do Stripe "Charge Succeeded" (Cobrança bem-sucedida) em um perfil de usuário do Braze.]({% image_buster /assets/img/stripe/stripe_braze_profile_event.png %}){: style="max-width:80%;"}

## Exemplo de carga útil do webhook do Stripe {#example}

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

Os modelos a seguir foram criados com base em nossa [carga útil de webhook do Stripe](#example). Esses modelos podem ser usados como ponto de partida. Você pode começar do zero ou excluir componentes específicos conforme achar necessário.

Neste modelo de exemplo, estamos registrando um evento personalizado no perfil do Braze. O tipo de evento será enviado como o nome do evento personalizado, e o objeto de dados será passado como propriedades do evento. 

### Caso de uso: cliente como um identificador

Neste modelo de exemplo, estamos usando o campo cliente como identificador.

{% tabs local %}
{% tab Entrada %}

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
{% tab Saída %}

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

Consulte [Monitoramento de sua transformação]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation/#step-5-monitor-your-transformation) para obter mais informações sobre monitoramento e solução de problemas de sua transformação.
