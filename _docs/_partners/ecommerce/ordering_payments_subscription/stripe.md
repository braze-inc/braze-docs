---
nav_title: Stripe
article_title: Stripe
description: "This article outlines the partnership between Braze and Stripe."
alias: /partners/stripe/
page_type: partner
search_tag: Partner
---

# Stripe

> [Stripe](https://www.stripe.com/) a comprehensive financial infrastructure platform that enables businesses to accept payments, manage revenue operations, and facilitate global commerce through a suite of integrated APIs and services.

By integrating Braze and Stripe, you can:

- Update user profiles in Braze with real-time payment and billing data from Stripe
- Trigger messaging in Braze based on Stripe events such as trial started, subscription activated, subscription cancellation, and more
- Personalize Braze messaging based on a user’s payment history or billing status received via Stripe webhooks


## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Stripe account | A Stripe account with access to webhooks is required to take advantage of this partnership. |
| Braze Data Transformation | A [Data Transformation URL]({{site.baseurl}}/data_transformation/) is necessary to receive data from Stripe. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Set up the Braze Data Transformation to accept Stripe’s webhooks {#step-1}

{% multi_lang_include create_transformation.md location="typeform" %}

### Step 2: Set up Stripe webhooks

Follow the steps in [Stripe's webhooks documentation](https://docs.stripe.com/development/dashboard/webhooks) to set up a webhook.

Add your Data Transformation webhook URL as the **Destination URL** and select the event types you’d like to send to Braze. A full list of event types can be found [here] (https://docs.stripe.com/api/events/types)





Send a test event to your Data Transformation. 


### Step 3: Write transformation code to accept your chosen Stripe events

In this step, you will transform the webhook payload that will be sent from Stripe to a JavaScript object return value.

1. Refresh your Data Transformation and make sure you can see the Stripe test payload in the **Webhook Details**.
2. Update your Data Transformation code to support your chosen Stripe events.
3. Click **Validate** to return a preview of your code’s output and to check if it’s an acceptable `/users/track` request.
4. Save and activate your Data Transformation.




#### Request body format

This return value must adhere to Braze’s `/users/track` request body format:

- Transformation code is accepted in the JavaScript programming language. Any standard JavaScript control flow, such as if/else logic, is supported.
- Transformation code accesses the webhook request body via the payload variable. This variable is an object populated by parsing the request body JSON.
- Any feature supported in our `/users/track` endpoint is supported, including:
    - User attributes objects, event objects, and purchase objects
    - Nested attributes and nested custom event properties
    - Subscription group updates
    - Email address as an identifier

## Example Stripe webhook payload

```json

{
 "headers": {
   "Version": "HTTP/1.1",
   "X-Datadog-Trace-Id": "9124157397962821303",
   "X-Datadog-Parent-Id": "9124157397962821303",
   "X-Datadog-Sampling-Priority": "2",
   "Host": "rest-01-secondary.k8s.cluster-001.s-use-1.braze.com",
   "X-Request-Id": "d1fd62a0-3172-497a-b602-ea2121047be7",
   "X-Real-Ip": "162.158.78.190",
   "X-Forwarded-For": "162.158.78.190",
   "X-Forwarded-Host": "rest-01-secondary.k8s.cluster-001.s-use-1.braze.com",
   "X-Forwarded-Port": "443",
   "X-Forwarded-Proto": "https",
   "X-Forwarded-Scheme": "https",
   "X-Scheme": "https",
   "X-Original-Forwarded-For": "54.187.205.235",
   "Cf-Ray": "9470a06172f8816e-IAD",
   "Cache-Control": "no-cache",
   "User-Agent": "Stripe/1.0 (+https://stripe.com/docs/webhooks)",
   "Accept-Encoding": "gzip",
   "Cf-Connecting-Ip": "54.187.205.235",
   "Cf-Visitor": "{\"scheme\":\"https\"}",
   "X-Worker-Executions": "1",
   "Cf-Worker": "todd.braze.com",
   "X-Fastly-Geoloc-Countrycode": "US",
   "Stripe-Signature": "t=1748465449,v1=36046c788460b5a9967888c29ac628fc9239bf7fed65eeb69012578333f9f966,v0=a117958094cdf432c1ad15cd9b868ae0135b024b8f4e473cadaee895a294bb68",
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
       "receipt_url": "https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xUlRuZnRSTUVPYUl2WXBVKKju3cEGMgZtsd96xMI6LBZjOf9bzeeWUJAnq1IOrLXIPbJebk-x8ACoyEpexcnVyEMg2a-6venjRuU6",
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

## Data Transformation use cases

The following are example templates built using our [example Stripe webhook payload](#example-stripe-webhook-payload). These templates can be used as a starting point. You can start from scratch or delete specific components as you see fit.

In this example template, we are logging a custom event to the Braze profile. The event type will be sent as the custom event name, and the data object will be passed as event properties. 

### Use case: customer as identifier

In this example template, we are using the customer field as the identifier.

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


### Step 4: Publish your Stripe webhook

After you have written your data transformation, click **Validate** to make your Data Transformation code is formatted correctly and will work as expected. Then, save and activate your Data Transformation.

Once activated, custom event data will be logged to a user's profile when they complete the event.



## Monitoring and troubleshooting

See the section [Monitoring your transformation]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation/#step-5-monitor-your-transformation) for more information on monitoring and troubleshooting your transformation.

