---
nav_title: "イベントオブジェクト"
article_title: APIイベントオブジェクト
page_order: 6
page_type: reference
description: "この参考記事では、イベントオブジェクトとは何か、イベントベースのキャンペーン戦略においてどのように重要な役割を果たすのかについて解説します。"

---

# イベントオブジェクト

> この記事では、イベント・オブジェクトのさまざまな構成要素、このオブジェクトの使用方法、および使用例について説明します。

## イベントオブジェクトとは何ですか？

イベント・オブジェクトは、特定のイベントが発生したときにAPIを通じて渡されるオブジェクトである。イベント・オブジェクトはイベント配列に格納される。events配列の各eventオブジェクトは、指定された時間値における、特定のユーザーによるカスタムイベントの単一の発生を表す。イベント・オブジェクトには、メッセージ、データ収集、パーソナライゼーションでイベント・プロパティを設定・使用することでカスタマイズできる様々なフィールドがあります。

特定のプラットフォーム用のカスタムイベントの設定方法は、[デベロッパーガイド][1]内のプラットフォーム統合ガイドをお読みください。この情報は、各プラットフォームの**アナリティクスタブに**ある**カスタムイベントのトラッキング**ページで確認できます。いくつかリンクを貼っておく。

カスタムイベントのトラッキングの記事

- [Android][2]
- [iOS][3]
- [Web][4]

### オブジェクト本体

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" is required
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "app_id" : (optional, string) see App Identifier,
  "name" : (required, string) the name of the event,
  "time" : (required, datetime as string in ISO 8601 or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format),
  "properties" : (optional, Properties Object) properties of the event
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
  // See following notes regarding anonymous push token imports
}
```

- [外部ユーザー ID]({{site.baseurl}}/api/basics/#user-ids)
- [アプリ識別子]({{site.baseurl}}/api/identifier_types/)
- [ISO 8601 タイムコード ウィキ][22]

#### 既存のプロファイルの更新のみ

Brazeの既存のユーザープロファイルのみを更新したい場合は、リクエスト本文の中で、`_update_existing_only` キーに`true` という値を付けて渡してください。この値を省略すると、`external_id` がまだ存在しない場合、Brazeは新しいユーザープロファイルを作成します。

{% alert note %}
`/users/track` エンドポイント経由でエイリアスのみのユーザー・プロファイルを作成する場合は、`_update_existing_only` を`false` に設定する必要があります。この値を省略すると、エイリアスのみのプロファイルは作成されません。
{% endalert %}

## イベント・プロパティ・オブジェクト
カスタム・イベントと購入は、イベント・プロパティを持つことができます。プロパティ」の値は、キーがプロパティ名、値がプロパティ値であるオブジェクトでなければなりません。プロパティ名は、255文字以下の空でない文字列でなければならず、先頭のドル記号（$）は使用できません。

プロパティ値は、以下のデータ型のいずれかになります：

| データ型
| --- | --- |
| 数値｜[整数](https://en.wikipedia.org/wiki/Integer)または[浮動小数点数](https://en.wikipedia.org/wiki/Floating-point_arithmetic)として
| ブーリアン
| 日付｜[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)または`yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式の文字列としてフォーマットされる。配列内ではサポートされない。|
| 文字列｜255文字以下。|
| 配列 | 配列に日時を含めることはできない。|
| オブジェクト｜オブジェクトは文字列として取り込まれる。|
{: .reset-td-br-1 .reset-td-br-2}

配列またはオブジェクト値を含むイベント・プロパティ・オブジェクトは、最大 50 KB のイベント・プロパティ・ペイロードを持つことができる。

### イベント・プロパティの永続性
イベント・プロパティは、親イベントによってトリガーされたメッセージのフィルタリングとリキッドパーソナライゼーションのために設計されています。デフォルトでは、Brazeユーザープロファイルに永続化されません。イベント・プロパティ値をセグメンテーションで使用するには、イベント・プロパティ値を長期的に保存するための様々なアプローチについて詳述している[カスタム・][5]イベントを参照のこと。

#### イベント依頼例

```json
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "events" : [
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:30+01:00"
    },
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "rented_movie",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "movie": "The Sad Egg",
        "director": "Dan Alexander"
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:50+01:00"
    }
  ]
}
```
-[ISO 8601 タイムコード ウィキ][19]

## イベントオブジェクト

提供された例を使えば、誰かが最近予告編を見て、映画をレンタルしたことがわかる。キャンペーンに入り、これらのプロパティに基づいてユーザーをセグメントすることはできませんが、Liquidを使用してチャネルを通してカスタムメッセージを送信するために、レシートの形でこれらのプロパティを使用することで、戦略的に使用することができます。例えば、**"ハロー・ベス**、**ダン・アレクサンダーの** **『悲しい卵**』をレンタルしてくれてありがとう。


[1]: {{site.baseurl}}/developer_guide/home/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[19]: http://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 タイムコード ウィキ"
[21]: {{site.baseurl}}/api/api_key/#the-app-identifier-api-key
[22]: https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 タイムコード"
[23]: {{site.baseurl}}/api/basics/#external-user-id-explanation
