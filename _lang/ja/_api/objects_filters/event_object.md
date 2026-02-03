---
nav_title: "イベント・オブジェクト"
article_title: APIイベントオブジェクト
page_order: 6
page_type: reference
description: "この参考記事では、イベント・オブジェクトとは何か、イベント・オブジェクトがイベント・ベースのキャンペーン戦略においていかに重要な役割を果たすかについて解説する。"

---

# イベント・オブジェクト

> この記事では、イベント・オブジェクトのさまざまな構成要素、このオブジェクトの使用方法、そして使用例について説明する。

## イベントオブジェクトとは。

イベント・オブジェクトは、特定のイベントが発生したときにAPIを通じて渡されるオブジェクトである。イベント・オブジェクトはイベント配列に格納される。events配列の各イベントオブジェクトは、指定された時間値における、特定のユーザーによるカスタムイベントの単一の発生を表す。イベント・オブジェクトにはさまざまなフィールドがあり、それらを使用して、メッセージ、データ収集、パーソナライゼーションにおいてイベントプロパティを設定し、使用することでカスタマイズすることができます。

特定のプラットフォームにカスタムイベントを設定する手順については、[開発者ガイド]({{site.baseurl}}/developer_guide/home/)の「プラットフォーム総合ガイド」を参照してください。ご使用のプラットフォームに基づいて、関連記事を参照してください。

- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)

### オブジェクト本体

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
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

- [外部ユーザ ID]({{site.baseurl}}/api/basics/#user-ids)
- [アプリ識別子]({{site.baseurl}}/api/identifier_types/)
- [ISO 8601タイムコード](https://en.wikipedia.org/wiki/ISO_8601)

#### 既存のプロファイルのみを更新する

Braze で既存のユーザープロファイルのみを更新するには、`_update_existing_only` キーをリクエストの本文内に `true` の値で渡す必要があります。この値を省略すると、`external_id` がまだ存在しない場合、Brazeは新しいユーザープロファイルを作成する。

{% alert note %}
`/users/track` エンドポイントを使用してエイリアスのみのユーザープロファイルを作成する場合は、`_update_existing_only` を`false` に設定する必要があります。この値が省略された場合、エイリアスのみのプロファイルは作成されない。
{% endalert %}

## イベント・プロパティ・オブジェクト

カスタムイベントと購入にはイベントプロパティが含まれる場合があります。「プロパティ」値は、キーがプロパティ名で値がプロパティ値であるオブジェクトである必要があります。プロパティ名は、255文字以下の空でない文字列でなければならず、先頭にドル記号（$）は付けない。

プロパティ値は、次のデータ型のいずれでもかまいません。

| データ型 | 説明 |
| --- | --- |
| 数値 | [整数](https://en.wikipedia.org/wiki/Integer)または[浮動小数点数として](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| ブール値 | `true` または `false` |
| 日時 | 文字列として [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 形式または以下のいずれかの形式でフォーマットする必要があります。<br>- `yyyy-MM-ddTHH:mm:ss:SSSZ`<br>- `yyyy-MM-ddTHH:mm:ss`<br>- `yyyy-MM-dd HH:mm:ss`<br>- `yyyy-MM-dd`<br>- `MM/dd/yyyy`<br>- `ddd MM dd HH:mm:ss.TZD YYYY`<br><br>アレイ内ではサポートされていない。<br><br>「T」は時間指定子であり、プレースホルダーではないことに注意してください。変更または削除しないでください。<br><br>タイムゾーンのない時間属性はデフォルトで UTC の真夜中になります（ダッシュボード上では会社のタイムゾーンの UTC の真夜中に相当する形式で表示されます）。<br><br> タイムスタンプが未来のイベントはデフォルトで現在の時刻になります。  |
| 文字列 | 255 文字以下。 |
| 配列 | 配列に日時を含めることはできない。 |
| オブジェクト | オブジェクトは文字列として取り込まれます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

配列またはオブジェクト値を含むイベントプロパティオブジェクトには、最大 100 KB のイベントプロパティペイロードを設定できます。

### 予約済みのキー

以下のキーは予約されているため、カスタムイベントプロパティとして使用できません。

- `time`
- `event_name`

{% alert important %}
カスタムイベントプロパティ名として予約キーを使用すると、`/users/track` エンドポイントにリクエストを送信する際に API エラーが発生する。
{% endalert %}

### イベント・プロパティの永続性

イベント・プロパティは、親イベントによってトリガーされるメッセージのフィルタリングと、リキッド・パーソナライゼーションのために設計されている。デフォルトでは、Braze ユーザープロファイルでは永続化されません。セグメンテーションでイベントプロパティ値を使用するには、イベントプロパティ値を長期的に保存するための様々なアプローチについて詳述している[カスタム]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)イベントを参照のこと。

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
- [ISO 8601 時間コード Wiki](http://en.wikipedia.org/wiki/ISO_8601)

## イベント・オブジェクト

提供された例を使えば、誰かが最近予告編を見て、映画をレンタルしたことがわかる。キャンペーンに入り、これらのプロパティに基づいてユーザーをセグメントすることはできませんが、Liquid を使用してチャネルを介し、カスタムメッセージを送信するために、受け取りの形でこれらのプロパティを使用することで、戦略的に使用することができます。例えば、『こんにちは、**Beth**。**Dan Alexander** の **The Sad Egg** をレンタルしていただき、ありがとうございます。お客様のレンタル状況に基づいて、お勧めの映画をご紹介いたします...』のように使用できます。


