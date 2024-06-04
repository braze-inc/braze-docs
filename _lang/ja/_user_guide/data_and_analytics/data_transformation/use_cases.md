---
nav_title: ユースケース
article_title: Braze Data Transformation のユースケース
page_order: 2
page_type: reference
description: "このリファレンス記事では、Braze Data Transformation のユースケースをいくつか紹介します。"
---

# データ変換のユースケース

> Braze Data Transformation と外部プラットフォーム例の Webhook の組み合わせを持つ、次のようなユースケースを考えてみましょう。

## リード創出

自社の Web サイトで、リードを創出する Typeform フォームをホストしています。新規ユーザーがこのフォームに入力すると、次のことができます。
\- Brazeで新規ユーザーを作成します。
\- そのユーザーを Braze のメールリストに追加します。
\- 回答のいくつかを Braze のカスタム属性として同期します。回答は、将来に向けてパーソナライズされたメッセージングエクスペリエンスを強化できる貴重なファーストパーティデータであるためです。

## サービスチケットを開く

顧客が Zendesk などのプラットフォームでカスタマーサービスチケットを開く場合には、次のことができます。
\- Zendesk チケットの作成時に Braze でカスタムイベントを作成します。
\- Braze のイベントプロパティを使用して、否定的な CSAT 評価 (顧客満足度) が Zendesk に入力されたときのカスタムイベントを作成します。

## Brazeとの連携

Braze の[連携]({{site.baseurl}}/partners/message_orchestration/channel_extensions/surveys/iterate/)を、顧客のインサイトおよび調査のプラットフォームである Iterate と使用できます。Data Transformation では、複数のカスタム属性を保存する既存の統合ではなく、1 つの階層化カスタム属性の下に調査の回答を複数保存できます。

## 変換コードの例

調査プラットフォームである Typeform から調査の回答を受信するたびに、次のサンプルペイロードが送信されるとします。

![][1]

{% tabs local %}
{% tab Basic transformation %}

このユースケースでは、調査の回答を属性として受け取り、調査が完了したことを示すイベントを書き込みます。

```
return {
  "attributes": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_rating": payload.form_response.answers[1].number
    }
  ],
  "events": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
}
```

{% endtab %}
{% tab Advanced transformation %}

次の高度なユースケースは基本的なユースケースに基づき、回答の 1 つを使用してユーザーを分類する `if` ステートメントを導入して作成されています。

\`\`\`
let nps\_category;
let nps\_number = payload.form\_response.answers[1].number;
if (nps\_number < 7) {
  nps\_category = "Detractor";
} else if (nps\_number == 7 || nps\_number == 8) {
  nps\_category = "Passive";
} else if (nps\_number > 8) {
  nps\_category = "Promoter";
}

return {
"attributes": [
{
"email": payload.form_response.hidden.email_address,
"_update_existing_only": true,
"home_city": payload.form_response.answers[0].text,
"home_weather_NPS_category": nps_category
}
  ],
    "events": [
          {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
          }
        ]
      };
    \`\`\`
  {% endtab %}
  {% endtabs %}

[1]: {% image_buster /assets/img/data_transformation/data_transformation2.png %}