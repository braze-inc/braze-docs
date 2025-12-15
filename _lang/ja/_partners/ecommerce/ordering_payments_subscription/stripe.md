---
nav_title: Stripe
article_title: Stripe
description: "この記事では、Braze と Stripe のパートナーシップについて概説します。"
alias: /partners/stripe/
page_type: partner
search_tag: Partner
---

# Stripe

> [Stripe](https://www.stripe.com/)は、企業が一連の統合されたAPIやサービスを通じて、決済を受け入れ、収益オペレーションを管理し、グローバルな商取引を容易にすることを可能にする総合的な金融インフラ・プラットフォームです。

Braze と Stripe を統合することで、以下のことが可能になります。

- Stripe からのリアルタイムの支払いと請求データを使用して、Braze でユーザプロファイルを更新します。
- トライアルの開始、サブスクリプションの有効化、サブスクリプションのキャンセルなどのストライプイベントに基づいて、Braze でメッセージをトリガーします。
- Stripe ウェブフックを使用して受信したユーザの支払履歴または請求ステータスに基づいて、Braze メッセージをカスタマイズします。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Stripe アカウント | このパートナーシップを利用するには、webhook にアクセスできる Stripe アカウントが必要です。 |
| Braze Data Transformation | Stripe からデータを受信するには、[Data Transformation URL]({{site.baseurl}}/data_transformation/) が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ 1: Stripe の Webhook を受け入れるように Braze Data Transformation を設定する {#step-1}

{% multi_lang_include create_transformation.md %}

### ステップ 2:Stripe webhook を設定する

[Stripe のwebhooks documentation](https://docs.stripe.com/development/dashboard/webhooks) の手順に従って、Webhook を設定します。

Data Transformation Webhook URL を**Destination URL** として追加し、Braze に送信するイベントタイプを選択します。イベントタイプの完全なリストについては、[Stripe のドキュメント](https://docs.stripe.com/api/events/types)を参照してください。

![StripeのWebhook設定例。]({% image_buster /assets/img/stripe/stripe_webhook_configuration.png %}){: style="max-width:80%;"}

次に、テストイベントを Data Transformation に送信します。 

### ステップ 3: 選択したStripe イベントを受け入れるトランスフォーメーションコードを記述します

次に、Stripe から送信されるWebhook ペイロードをJavaScript オブジェクトの戻り値に変換します。

1. Data Transformation を更新し、[**Webhook の詳細**] セクションに Stripe テストペイロードが表示されることを確認します。
2. 選択したStripe イベントをサポートするようにData Transformation コードを更新します。
3. [**検証**] を選択すると、コードの出力のプレビューが返され、`/users/track` リクエストとして受け入れられるかどうかがチェックされます。
4. Data Transformation を保存して有効化します。

![Webhookの詳細と変換コードの例。]({% image_buster /assets/img/stripe/stripe_data_transformation.png %})

#### リクエスト本文の形式

この戻り値は、`/users/track` エンドポイントリクエストボディ形式に従う必要があります。

- 変換コードは JavaScript プログラミング言語で受け入れられます。if/else ロジックなど、標準的な JavaScript 制御フローがすべてサポートされています。
- トランスフォーメーションコードは、ペイロード変数を使用してWebhook リクエストボディにアクセスします。この変数は、リクエスト本文の JSON を解析して読み込まれたオブジェクトです。
- `/users/track` エンドポイントでサポートされるすべてのフィーチャーがサポートされています。例を示します。
    - ユーザー属性オブジェクト、イベントオブジェクト、および購入オブジェクト
    - 階層化属性と階層化カスタムイベントプロパティ
    - サブスクリプショングループの更新
    - 識別子としてのメールアドレス

### ステップ 4: Stripe Webhook を公開する

Data Transformation を作成したら、[**検証**] を選択して、Data Transformation コードが正しくフォーマットされており、期待通りに動作することを確認します。その後、Data Transformation を保存してアクティブ化します。アクティブ化後、カスタムイベントデータは、イベントが完了するとユーザーのプロファイルに記録されます。

![BrazeユーザープロファイルのStripeカスタムイベント "Charge Succeeded"。]({% image_buster /assets/img/stripe/stripe_braze_profile_event.png %}){: style="max-width:80%;"}

## Stripe Webhook ペイロードのサンプル {#example}

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

## データ変換のユースケース

以下に、[Stripe の Webhook ペイロードのサンプル](#example)を使用して作成したテンプレートの例を示します。これらのテンプレートは出発点として使用できる。ゼロから作成するか、必要に応じて特定のコンポーネントを削除することができます。

このテンプレート例では、Braze プロファイルにカスタムイベントをロギングしています。イベントタイプはカスタムイベント名として送信され、データオブジェクトはイベントプロパティとして渡されます。 

### ユースケース: 識別子としての顧客

このテンプレートの例では、識別子として顧客フィールドを使用しています。

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

## モニタリングとトラブルシューティング

トランスフォーメーションのモニタリングとトラブルシューティングの詳細については、[トランスフォーメーションのモニタリング]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation/#step-5-monitor-your-transformation)を参照してください。
