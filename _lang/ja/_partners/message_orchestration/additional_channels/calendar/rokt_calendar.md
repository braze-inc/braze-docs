---
nav_title: ロクト・カレンダー
article_title: ロクト・カレンダー
alias: /partners/rokt_calendar/
description: "この参考記事では、BrazeとRokt Calendarの提携について概説している。Rokt Calendarは、ダイナミックなカレンダー・マーケティング・テクノロジーで、ブランドはカレンダー・イベントや通知の形で、1:1のイベントやプロモーション・コミュニケーションをプッシュすることができる。"
page_type: partner
search_tag: Partner

---

# ロクト・カレンダー

> [Rokt Calendarは](https://www.rokt.com/rokt-calendar/)、1:1イベントやプロモーション・コミュニケーションをカレンダーイベントや通知の形でプッシュすることを可能にするダイナミック・カレンダー・マーケティング・テクノロジーである。

BrazeとRokt Calendarの統合により、Rokt Calendarの購読者とそのデータは、Brazeのウェブフックを介してBrazeにプッシュされる。そして、このデータをBraze Canvasesのジャーニーターゲティングとオーディエンスセグメンテーションに使用することができる。 

## 前提条件

| 必要条件  | 説明 |
| ------------ | ----------- |
| 六連カレンダーのアカウント | このパートナーシップを利用するには、クライアント専用のRokt Calendarアカウントが必要である。[sales-calendar@rokt.com](mailto:sales-calendar@rokt.com)に連絡して、アカウント・マネージャーと話す。  |
| ロクト・カレンダーの設定 | Roktカレンダーのアカウントマネージャーが、あなたのニーズに合わせて、以下のような設定を含む、最適なカレンダーを設定する：<br>\- マージフラグ<br>\- 加入者IDフォールバックフラグ<br>\- 必要であれば、電子メールのキャプチャ |
| Rokt Calendar OAuth認証情報 | Roktカレンダーのアカウントマネージャーから提供されるこのキーで、BrazeとRoktカレンダーのアカウントを接続することができる。<br><br>これは、Brazeダッシュボードの**「設定**」>「**接続コンテンツ**」で作成できる。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。このキーをRokt Calendarのアカウントマネージャーに提供する必要がある。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| [Braze RESTエンドポイント]({{site.baseurl}}/api/basics/#endpoints) | RESTエンドポイントのURL。エンドポイントは、インスタンスのBraze URLに依存する。 |
| 外部加入者ID | これは、Roktカレンダーの購読プロセスで、カレンダーの購読者とBrazeユーザーを照合するために使用される識別子である。これは六連カレンダーに渡すものだ。|
{: .reset-td-br-1 .reset-td-br-2}

## オーディエンス・セグメンテーション {#audience-segmentation}

Rokt Calendarが新規ユーザーを作成するとき、または既存の購読者とBrazeユーザーをマッチさせるとき、Rokt Calendarは、Braze内でフィルタリングできる以下のカスタム購読属性を送信する：

| カスタム属性  | 定義       | 例          |
| ----------------  | ---------------- | ---------------- |
| `rokt:account_code` | 六連カレンダーのアカウントコード | `brazetest/f5733866ade2` そして `brazetest/ff10919f1078` |
| `rokt:account_id` |六連カレンダーのアカウントID | `d0ce4299-7d6c-4888-bfd8-c7e867a0fa6c/f5733866ade2` |
| `rokt:account_name` | ロクト・カレンダーのアカウント名 | `Braze Test/f5733866ade2` |
| `rokt:calendar_code` | ロクト・カレンダー・カレンダーのコード | `test-calendar-1/f5733866ade2` |
| `rokt:calendar_id` | 六連カレンダーのカレンダーID | `9a9007c7-f5a4-e811-b13c-06424c4f2724/f5733866ade2` |
| `rokt:calendar_title` | 六連カレンダーのカレンダータイトル | `Test Calendar 1/f5733866ade2` |
| `rokt:country_code` | 作成されたサブスクリプションに関連する国コード | `AU/f5733866ade2` |
| `rokt:device_name` | 作成されたサブスクリプションに関連するデバイスタイプ | `Desktop/f5733866ade2` |
| `rokt:geo_country` | 作成されたサブスクリプションに関連する原産国 | `Australia/f5733866ade2` |
| `rokt:optIn1` | ユーザーが、作成されたサブスクリプションに関連する2つのオプトインのうち、最初のオプトインにオプトインした場合 | `True/f5733866ade2` |
| `rokt:optIn2` | ユーザーが、作成された購読に関連する2つのオプトインのうち2つ目にオプトインした場合 | `True/f5733866ade2` |
| `rokt:source` | 作成されたサブスクリプションのソース | `brazetest.Rokt Calendarapp.com/f5733866ade2` |
| `rokt:subscriber_email` | 購読手続き中にユーザーが入力したEメールアドレス | `test@email.com/f5733866ade2` |
| `rokt:subscription_id` | 作成されたサブスクリプションに関連する、一意な識別子としてのサブスクリプションID。 | `06423672-b6ba-4536-aa36-70788a7a0a36` |
| `rokt:subscription_method` | 作成されたサブスクリプションに関連するサブスクリプションメソッド（webcal/Google）。 | `WebCal/f5733866ade2` |
| `rokt:tags` | 作成された購読に関連して使用されたカレンダータグ。 | `Test Calendar 1/All Teams/f5733866ade2 and Test Calendar 1/TeamI//f5733866ade2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Roktカレンダーはまた、ユーザーがRoktカレンダーに登録するとすぐに、`subscribe` カスタムイベントをトリガーする。

## 統合

### ステップ1:カレンダー購読者のオーディエンスを構築する

Canvasからカレンダー・イベントを送信するには、まずRoktカレンダーを設定し、ユーザーを登録する必要がある。そのためには、カレンダーを購読する場所と方法をユーザーに知らせる必要がある。ロクト・カレンダーでは、以下のことを推奨している：

#### サブスクリプションの統合ポイントを提供する
カレンダー購読者のオーディエンスを作るには、ユーザーが移動して購読できる先を提供する必要がある。サブスクリプション統合ポイントの例としては、以下のようなものがある：
  - ウェブサイトにカレンダーボタンを追加する
  - メールやSMSにカレンダーリンクを追加する 
  - カレンダーボタンをアプリに追加する
  - ソーシャルメディアにカレンダーのリンクを追加する

#### カレンダーを宣伝する
購読者のオーディエンスを作るには、購読方法を知ってもらうために、オーディエンスにカレンダーを宣伝する必要がある。カレンダープロモーションの例としては、以下のようなものがある：
  - ソーシャルメディアへの投稿
  - Eメールニュースレターと最新情報
  - ブログ記事
  - アプリ内通知

### ステップ2:BrazeでRokt CalendarのWebhookを作成する

Brazeでは、WebhookキャンペーンやCanvas内のWebhookを設定することができる：

- 新しいパーソナライズされたイベントを送信する：購読者のカレンダーのセグメントに新しいイベントを追加できるようにする。
- パーソナライズされたイベントを更新する：購読者のカレンダーにある既存のイベントを更新できるようにする。

今後のキャンペーンやCanvasで使用するRokt Calendarウェブフックテンプレートを作成するには、Brazeプラットフォームの**「テンプレート**」>「**ウェブフックテンプレート**」に移動する。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**Engagement（エンゲージメント）**」＞「**Templates & Media（テンプレート＆メディア**）」＞「**Webhook Templates（ウェブフック・テンプレート**）」と進む。
{% endalert %}

単発のRokt Calendar Webhookキャンペーンを作成したい場合、または既存のテンプレートを使用したい場合は、新しいキャンペーンを作成する際にBrazeの**Webhookを**選択する。

{% tabs %}
{% tab 新しいイベントを送信する %}
Rokt Calendarウェブフック・テンプレートを選択すると、以下のように表示される：
- **ウェブフックのURL**： {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}`{% endraw %}
- **リクエスト・ボディ**Raw Text
{% endtab %}
{% tab 既存のイベントを更新する %}
Rokt Calendarウェブフック・テンプレートを選択すると、以下のように表示される：
- **ウェブフックのURL**： {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}/update`{% endraw %}
- **リクエスト・ボディ**Raw Text
{% endtab %}
{% endtabs %}

#### リクエストヘッダと方法

Rokt Calendarは、認証のために、Rokt Calendar Connected Contentクレデンシャル名を含む`HTTP Header` 。以下はすでにキーと値のペアとしてテンプレート内に含まれているが、**「設定」**タブでは、`<Rokt-Calendar-API>` を`Manage Settings > Connected Content > Credential` にあるクレデンシャル名に置き換える必要がある。

{% raw %}
- **HTTPメソッド**：POST
- **ヘッダーをリクエストする**：
  - **認可する**：ベアラー `{% connected_content https://api.roktcalendar.com/oauth2/token :method post :basic_auth <Rokt-Calendar-API> :body grant_type=client_credentials :save token :retry %}{{token.access_token}}`
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
{% tab イベント詳細 %}
以下のフィールドには、イベント・レベルでカスタマイズできる情報が含まれている。

| フィールド             | 定義       | 例          |
| ----------------  | ---------------- | ---------------- |
| `eventId`<br>**\*必須** | 追加または更新されるイベントの一意な識別子。 | `Event_00001`
| `eventTitle`<br>**\*必須** | カレンダーに表示されるイベントのタイトル | サマーセール2019
| `eventDescr` | カレンダーに表示されるイベントの説明文 | セール期間は3日間で、このリンク（`www.mybusiness.com/sale` ）をクリックするとオファーが表示される。 |
| `eventLocation` | カレンダーに表示されるイベントの場所。これはしばしば、eventTitleを補完する2番目の行動喚起として使用されることに注意。 | 50％オフのイベントを開く |
| `eventStart`<br>**\*必須**  | カレンダーに表示されるイベントの開始日時 | `2019-02-21T15:00:00` |
| `eventEnd`<br>**\*必須**  | カレンダーに表示されるイベントの開始日時 | `2019-02-21T16:00:00` |
| `eventTz`<br>**\*必須**  | カレンダーに表示されるイベントのタイムゾーンを指定する。 | `Eastern Standard Time` |
| `notifyBefore`<br>**\*必須**  | カレンダーに表示されるイベントのリマインダー時間。 | `15` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
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
