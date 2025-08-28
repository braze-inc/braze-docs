---
nav_title: Rokt Calendar
article_title: Rokt Calendar
alias: /partners/rokt_calendar/
description: "この参考記事では、BrazeとRokt Calendarの提携について概説している。Rokt Calendarは、ダイナミックなカレンダー・マーケティング・テクノロジーで、ブランドはカレンダー・イベントや通知の形で、1:1のイベントやプロモーション・コミュニケーションをプッシュすることができる。"
page_type: partner
search_tag: Partner
---

# Rokt Calendar

> [Rokt Calendar](https://www.rokt.com/rokt-calendar/) は、ブランドがカレンダーイベントや通知の形式で1:1イベントやプロモーションコミュニケーションをプッシュできるようにするダイナミックなカレンダーマーケティングテクノロジーです。

_この統合は、Rokt Calendar によって管理されます。_

## 統合について

Braze と Rokt Calendar の統合により、Rokt Calendar のサブスクライバーとそのデータを Braze Webhook 経由で Braze にプッシュできます。その後、Braze キャンバスでこのデータを使用して、以下のカスタム [Rokt Calendar 属性](#audience-segmentation)を使用したジャーニーターゲティングとオーディエンスセグメンテーションを行うことができます。 

## 前提条件

| 必要条件  | 説明 |
| ------------ | ----------- |
| Rokt Calendar アカウント | このパートナーシップを利用するには、クライアント専用のRokt Calendarアカウントが必要である。[sales-calendar@rokt.com](mailto:sales-calendar@rokt.com)に連絡して、アカウント・マネージャーと話す。  |
| Rokt Calendar の設定 | Roktカレンダーのアカウントマネージャーが、あなたのニーズに合わせて、以下のような設定を含む、最適なカレンダーを設定する：<br>\- マージフラグ<br>\- 加入者IDフォールバックフラグ<br>\- 必要であれば、電子メールのキャプチャ |
| Rokt Calendar OAuth認証情報 | Roktカレンダーのアカウントマネージャーから提供されるこのキーで、BrazeとRoktカレンダーのアカウントを接続することができる。<br><br>これは、Brazeダッシュボードの**「設定**」>「**接続コンテンツ**」で作成できる。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。このキーを Rokt Calendar アカウントマネージャーに提供する必要があります。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| [Braze REST エンドポイント]({{site.baseurl}}/api/basics/#endpoints) | RESTエンドポイントのURL。エンドポイントは、インスタンスのBraze URLに依存する。 |
| 外部サブスクライバー ID | これは、Rokt Calendar サブスクリプションプロセスがカレンダーサブスクライバーと Braze ユーザーを照合するために使用する ID です。これを Rokt Calendar に渡します。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## オーディエンスセグメンテーション {#audience-segmentation}

Rokt Calendar での新規ユーザーの作成時、またはサブスクライバーと Braze ユーザーの照合時に、Rokt Calendar から、Braze 内でフィルタリングできる次のカスタムサブスクリプション属性が送信されます。

| カスタム属性  | 定義       | 例          |
| ----------------  | ---------------- | ---------------- |
| `rokt:account_code` | Rokt Calendar アカウントのコード | `brazetest/f5733866ade2` と `brazetest/ff10919f1078` |
| `rokt:account_id` |Rokt Calendar アカウントの ID | `d0ce4299-7d6c-4888-bfd8-c7e867a0fa6c/f5733866ade2` |
| `rokt:account_name` | Rokt Calendar アカウントの名前 | `Braze Test/f5733866ade2` |
| `rokt:calendar_code` | Rokt Calendar カレンダーのコード | `test-calendar-1/f5733866ade2` |
| `rokt:calendar_id` | Rokt Calendar カレンダーの ID | `9a9007c7-f5a4-e811-b13c-06424c4f2724/f5733866ade2` |
| `rokt:calendar_title` | Rokt Calendar カレンダーのタイトル | `Test Calendar 1/f5733866ade2` |
| `rokt:country_code` | 作成されたサブスクリプションに関連する国コード | `AU/f5733866ade2` |
| `rokt:device_name` | 作成されたサブスクリプションに関連するデバイスタイプ | `Desktop/f5733866ade2` |
| `rokt:geo_country` | 作成されたサブスクリプションに関連する原産国 | `Australia/f5733866ade2` |
| `rokt:optIn1` | ユーザーが、作成されたサブスクリプションに関連する2つのオプトインのうち、最初のオプトインにオプトインした場合 | `True/f5733866ade2` |
| `rokt:optIn2` | ユーザーが、作成されたサブスクリプションに関連する2つのオプトインのうち2番目にオプトインした場合 | `True/f5733866ade2` |
| `rokt:source` | 作成されたサブスクリプションのソース | `brazetest.Rokt Calendarapp.com/f5733866ade2` |
| `rokt:subscriber_email` | サブスクリプションプロセス中にユーザーが入力したメールアドレス | `test@email.com/f5733866ade2` |
| `rokt:subscription_id` | 作成されたサブスクリプションに関連する、一意な識別子としてのサブスクリプションID。 | `06423672-b6ba-4536-aa36-70788a7a0a36` |
| `rokt:subscription_method` | 作成されたサブスクリプションに関連するサブスクリプションメソッド（webcal/Google）。 | `WebCal/f5733866ade2` |
| `rokt:tags` | 作成された購読に関連して使用されたカレンダータグ。 | `Test Calendar 1/All Teams/f5733866ade2 and Test Calendar 1/TeamI//f5733866ade2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

また、Rokt Calendar は、ユーザーが Rokt Calendar をサブスクライブするとすぐに `subscribe` カスタムイベントをトリガーします。このカレンダーは、Braze セグメンテーションで使用することも、キャンペーンまたはキャンバスコンポーネントのトリガーとして使用することもできます。

## 統合

### ステップ1:カレンダーサブスクライバーのオーディエンスを作成する

キャンバスからカレンダーイベントを送信するには、まずすでにサブスクライブしているユーザーを使用して Rokt Calendar を設定する必要があります。そのためには、カレンダーをサブスクライブする場所と方法をユーザーに通知します。Rokt Calendar では以下のことが推奨されています。

#### サブスクリプションの統合ポイントを提供する
カレンダーサブスクライバーのオーディエンスを作成するには、ユーザーが移動してサブスクライブできる場所を提供する必要があります。サブスクリプション統合ポイントの例としては、以下のようなものがある：
  - ウェブサイトにカレンダーボタンを追加する
  - メールやSMSにカレンダーリンクを追加する 
  - カレンダーボタンをアプリに追加する
  - ソーシャルメディアにカレンダーのリンクを追加する

#### カレンダーを宣伝する
サブスクライバーからなるオーディエンスを作成するには、サブスクライブ方法がわかるように、オーディエンスにカレンダーをプロモーションする必要があります。カレンダープロモーションの例としては、以下のようなものがある：
  - ソーシャルメディアへの投稿
  - Eメールニュースレターと最新情報
  - ブログ記事
  - アプリ内通知

### ステップ2:BrazeでRokt CalendarのWebhookを作成する

Braze では、次のいずれかを行うために Webhook キャンペーンまたはキャンバス内の Webhook を設定できます。

- 新しいパーソナライズされたイベントを送信する：サブスクライバーのカレンダーのセグメントに新しいイベントを追加できるようにします。
- パーソナライズされたイベントを更新する：サブスクライバーのカレンダーにある既存のイベントを更新できるようにします。

今後のキャンペーンやCanvasで使用するRokt Calendarウェブフックテンプレートを作成するには、Brazeプラットフォームの**「テンプレート**」>「**ウェブフックテンプレート**」に移動する。 

単発のRokt Calendar Webhookキャンペーンを作成したい場合、または既存のテンプレートを使用したい場合は、新しいキャンペーンを作成する際にBrazeの**Webhookを**選択する。

{% tabs %}
{% tab 新しいイベントを送信する %}
Rokt Calendarウェブフック・テンプレートを選択すると、以下のように表示される：
- **Webhook URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}`{% endraw %}
- **リクエスト本文**:Raw Text
{% endtab %}
{% tab 既存のイベントを更新する %}
Rokt Calendarウェブフック・テンプレートを選択すると、以下のように表示される：
- **Webhook URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}/update`{% endraw %}
- **リクエスト本文**:Raw Text
{% endtab %}
{% endtabs %}

#### リクエストヘッダと方法

Rokt Calendar では、認証のために Rokt Calendar コネクテッドコンテンツの認証情報名を含む `HTTP Header` が必要です。以下はすでにキーと値のペアとしてテンプレート内に含まれているが、**「設定」**タブでは、`<Rokt-Calendar-API>` を`Manage Settings > Connected Content > Credential` にあるクレデンシャル名に置き換える必要がある。

{% raw %}
- **HTTPメソッド**：POST
- **リクエストヘッダー**:
  - **Authorization**:ベアラー `{% connected_content https://api.roktcalendar.com/oauth2/token :method post :basic_auth <Rokt-Calendar-API> :body grant_type=client_credentials :save token :retry %}{{token.access_token}}`
  - **Content-Type**: application/json
{% endraw %}

#### Request body

{% tabs ローカル %}
{% tab 新しいイベントを送信する %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  },
  "subscriptionIds": ["{{custom_attribute.${rokt:subscription_id}| join: '","'  }}"]
}
```
{% endraw %}
{% endtab %}
{% tab 既存のイベントを更新する %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  }
}
```
{% endraw %}
{% endtab %}
{% tab イベントの詳細 %}
以下のフィールドには、イベント・レベルでカスタマイズできる情報が含まれている。

| フィールド             | 定義       | 例          |
| ----------------  | ---------------- | ---------------- |
| `eventId`<br>**\*必須** | 追加または更新されるイベントの一意な識別子。 | `Event_00001`
| `eventTitle`<br>**\*必須** | カレンダーに表示されるイベントのタイトル | Summer Sale 2019
| `eventDescr` | カレンダーに表示されるイベントの説明文 | セール期間は3日間で、このリンク（`www.mybusiness.com/sale` ）をクリックするとオファーが表示される。 |
| `eventLocation` | カレンダーに表示されるイベントの場所。これはしばしば、eventTitleを補完する2番目の行動喚起として使用されることに注意。 | 50％オフのイベントを開く |
| `eventStart`<br>**\*必須**  | カレンダーに表示されるイベントの開始日時 | `2019-02-21T15:00:00` |
| `eventEnd`<br>**\*必須**  | カレンダーに表示されるイベントの開始日時 | `2019-02-21T16:00:00` |
| `eventTz`<br>**\*必須**  | カレンダーに表示されるイベントのタイムゾーン。適用可能なタイムゾーンのリストは[こちら](https://roktcalendar-api.readme.io/docs/timezones)で確認できます。 | `Eastern Standard Time` |
| `notifyBefore`<br>**\*必須**  | カレンダーに表示されるイベントのリマインダー時刻。これは分単位で表されます。 | `15` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

{% alert tip %}
有効なタイムゾーンのリストは、[https://roktcalendar-api.readme.io](https://roktcalendar-api.readme.io/reference/timezones)/reference/timezonesを参照のこと。
{% endalert %}

### ステップ3:リクエストをプレビューする

**Preview**パネルでリクエストをプレビューするか、**Test**タブに移動して、ランダムなユーザー、既存のユーザーを選択するか、ウェブフックをテストするために自分でカスタマイズする。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないこと！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成するときに、**保存されたWebhookテンプレート**リストで見つけることができる。
{% endalert %}

