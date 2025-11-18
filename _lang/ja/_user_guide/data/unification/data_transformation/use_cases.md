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
- Brazeで新規ユーザーを作成する。
- BrazeのEメールリストに追加する。
- 回答のいくつかを Braze のカスタム属性として同期します。回答は、将来に向けてパーソナライズされたメッセージングエクスペリエンスを強化できる貴重なファーストパーティデータであるためです。

## サービスチケットを開く

顧客が Zendesk などのプラットフォームでカスタマーサービスチケットを開く場合には、次のことができます。
- Zendeskチケットが作成されたときに、Brazeにカスタムイベントを書き込む。
- Zendeskに否定的なCSATレーティングが提供されたときに、Brazeのイベントプロパティでカスタムイベントを記述する。

## Brazeとの連携

Braze は、顧客インサイトおよび調査のプラットフォームである [Iterate]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/surveys/iterate/) と連携しています。Data Transformation では、複数のカスタム属性を保存する既存の統合ではなく、1 つの階層化カスタム属性の下に調査の回答を複数保存できます。

## 変換コードの例

調査プラットフォームである Typeform から調査の回答を受信するたびに、次のサンプルペイロードが送信されるとします。

![]({% image_buster /assets/img/data_transformation/data_transformation2.png %})

{% tabs local %}
{% tab Basic transformation %}

この例では、調査の回答を属性として取り、調査が完了したことを示すイベントを書き込みます。

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

基本的なトランスフォーメーションの例をさらに踏まえ、`if` ステートメントを導入して、いずれかの回答でユーザーを分類します。

```
let nps_category;
let nps_number = payload.form_response.answers[1].number;
if (nps_number < 7) {
  nps_category = "Detractor";
} else if (nps_number == 7 || nps_number == 8) {
  nps_category = "Passive";
} else if (nps_number > 8) {
  nps_category = "Promoter";
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
```
{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/data_transformation/data_transformation2.png %}