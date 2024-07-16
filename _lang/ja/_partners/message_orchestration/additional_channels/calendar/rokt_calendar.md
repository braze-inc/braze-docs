---
nav_title: Rokt Calendar
article_title:Rokt Calendar
alias: /partners/rokt_calendar/
description:「この参考記事では、BrazeとRokt Calendarのパートナーシップについて概説しています。Rokt Calendarは、ブランドがカレンダーイベントや通知という形で1対1のイベントやプロモーションコミュニケーションをプッシュできるようにするダイナミックなカレンダーマーケティングテクノロジーです。「
page_type: partner
search_tag:Partner

---

# Rokt Calendar

> [Rokt Calendarは](https://www.rokt.com/rokt-calendar/)、ブランドがカレンダーイベントや通知という形で1対1のイベントやプロモーションコミュニケーションをプッシュできるようにするダイナミックなカレンダーマーケティングテクノロジーです。

BrazeとRokt Calendar 統合により、Rokt Calendar 購読者とそのデータを、BrazeWebhook 経由でBrazeにプッシュできます。[その後、このデータをBraze Canvasesで使用して、以下のカスタムRokt Calendar 属性のいずれかを使用してジャーニーターゲティングとオーディエンスセグメンテーションを行うことができます。](#audience-segmentation) 

## 前提条件

| 必要条件  | 説明 |
| ------------ | ----------- |
| Rokt Calendar アカウント | このパートナーシップを利用するには、クライアント固有のRokt Calendarアカウントが必要です。[sales-calendar@rokt.com](mailto:sales-calendar@rokt.com) に連絡して、アカウントマネージャーにご相談ください  |
| Rokt Calendar 設定 | Rokt Calendarのアカウントマネージャーがお客様と協力して、次のような設定を含め、お客様のニーズに最適なカレンダーを設定します。<br>-マージフラグ<br>-サブスクライバー ID フォールバックフラグ<br>-メールキャプチャ (必要な場合) |
| Rokt Calendar の OAuth 認証情報 | Rokt Calendar アカウントマネージャーから提供されたこのキーにより、BrazeとRokt Calendar アカウントを接続できます。<br><br>これは Braze ダッシュボードの **\[設定] > \[****接続コンテンツ**] で作成できます。 |
| Braze REST API キー | `users.track`権限のあるBraze REST APIキー。このキーをRokt Calendar アカウントマネージャーに提供する必要があります。<br><br> これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
| [Braze REST エンドポイント]({{site.baseurl}}/api/basics/#endpoints) | あなたの REST エンドポイント URL。エンドポイントは、インスタンスの Braze URL によって異なります。 |
| 外部サブスクライバー ID | これは、Rokt CalendarサブスクリプションプロセスでカレンダーのサブスクライバーとBrazeユーザーマッチングに使用される識別子です。これはRokt Calendar に渡すものです。|
{: .reset-td-br-1 .reset-td-br-2}

## オーディエンスセグメンテーション {#audience-segmentation}

Rokt Calendarが新しいユーザーを作成したり、既存のサブスクライバー Brazeユーザー照合したりすると、Rokt Calendarは次のカスタムサブスクリプション属性を送信し、Braze内でフィルターできます。

| カスタム属性  | 定義       | 例          |
| ----------------  | ---------------- | ---------------- |
| `rokt:account_code` | Rokt Calendar アカウントのコード | `brazetest/f5733866ade2` そして `brazetest/ff10919f1078` |
| `rokt:account_id` |Rokt Calendar アカウントの ID | `d0ce4299-7d6c-4888-bfd8-c7e867a0fa6c/f5733866ade2` |
| `rokt:account_name` | Rokt Calendar アカウントの名前 | `Braze Test/f5733866ade2` |
| `rokt:calendar_code` | Rokt Calendar カレンダーのコード | `test-calendar-1/f5733866ade2` |
| `rokt:calendar_id` | Rokt Calendar の ID | `9a9007c7-f5a4-e811-b13c-06424c4f2724/f5733866ade2` |
| `rokt:calendar_title` | Rokt Calendar カレンダーのタイトル | `Test Calendar 1/f5733866ade2` |
| `rokt:country_code` | 作成されたサブスクリプションに関連する国コード | `AU/f5733866ade2` |
| `rokt:device_name` | 作成されたサブスクリプションに関連するデバイスタイプ | `Desktop/f5733866ade2` |
| `rokt:geo_country` | 作成されたサブスクリプションに関連する原産国 | `Australia/f5733866ade2` |
| `rokt:optIn1` | ユーザー作成されたサブスクリプションに関連する2つのオプトインのうち最初のオプトインにオプトインした場合 | `True/f5733866ade2` |
| `rokt:optIn2` | ユーザー作成されたサブスクリプションに関連する2つのオプトインのうち2つ目のオプトインにオプトインした場合 | `True/f5733866ade2` |
| `rokt:source` | 作成されたサブスクリプションのソース | `brazetest.Rokt Calendarapp.com/f5733866ade2` |
| `rokt:subscriber_email` | サブスクリプションプロセス中にユーザー入力したメールアドレス | `test@email.com/f5733866ade2` |
| `rokt:subscription_id` | 作成されたサブスクリプションに関連する一意の識別子となるサブスクリプション ID | `06423672-b6ba-4536-aa36-70788a7a0a36` |
| `rokt:subscription_method` | 作成されたサブスクリプションに関連するサブスクリプションメソッド (WebCal/Google)。 | `WebCal/f5733866ade2` |
| `rokt:tags` | 作成されたサブスクリプションに関連して使用されるカレンダータグ。 | `Test Calendar 1/All Teams/f5733866ade2 and Test Calendar 1/TeamI//f5733866ade2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

また、Rokt Calendar は、ユーザー `subscribe` Roktカレンダーに登録するとすぐにカスタムイベントをトリガーします。このイベントは、Brazeセグメンテーションで使用することも、キャンペーンやキャンバスコンポーネントのトリガーとして使用することもできます。

## 統合

### ステップ1:カレンダー購読者のオーディエンス構築

Canvasからカレンダーイベントを送信するには、まず、すでに購読しているユーザーでRoktカレンダーを設定する必要があります。そのためには、カレンダーを購読する場所と方法をユーザーに知らせる必要があります。Rokt Calendar では以下のことを推奨しています。

#### サブスクリプション統合ポイントを提供する
カレンダー購読者のオーディエンススを増やすには、ユーザーナビゲートして購読できる送信先を提供する必要があります。サブスクリプション統合ポイントの例には次のものがあります。
  - Web サイトカレンダーボタンを追加する
  - メールまたは SMS へのカレンダーリンクの追加 
  - アプリカレンダーボタンを追加する
  - ソーシャルメディアにカレンダーリンクを追加する

#### カレンダーを宣伝する
購読者をオーディエンスには、カレンダーをオーディエンス者に宣伝して、購読方法を理解してもらう必要があります。カレンダープロモーションの例としては、次のようなものがあります。
  - ソーシャルメディアへの投稿
  - メールニュースレターと最新情報
  - ブログ投稿
  - アプリ内通知

### ステップ2:Braze でRokt Calendar Webhook を作成する

Brazeでは、以下のいずれかの方法でWebhook キャンペーンまたはキャンバス内のWebhook を設定できます。

- 新しいパーソナライズされたイベントを送信:購読者のカレンダーのSegment に新しいイベントを追加できるようにします。
- パーソナライズされたイベントの更新:購読者のカレンダーの既存のイベント更新できるようにします。

今後のキャンペーンやキャンバスで使用するRokt Calendar Webhook テンプレートを作成するには、Braze プラットフォームで \[テンプレート] > \[****ウェブフックテンプレート****] に移動します。 

{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、\[**エンゲージメント**] > \[**テンプレートとメディア**] > \[**Webhookテンプレート**] に移動します。
{% endalert %}

一回限りのRokt Calendar ウェブフックキャンペーンを作成したい場合、または既存のテンプレートを使用する場合は、新しいキャンペーンを作成するときに Braze で **Webhook** を選択してください。

{% tabs %}
{% tab Send a new event %}
Rokt Calendar Webhook テンプレートを選択すると、以下が表示されるはずです。
- **ウェブフック URL:** {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}`{% endraw %}
- **リクエストボディ**:Raw Text
{% endtab %}
{% tab Update an existing event %}
Rokt Calendar Webhook テンプレートを選択すると、以下が表示されるはずです。
- **ウェブフック URL:** {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}/update`{% endraw %}
- **リクエストボディ**:Raw Text
{% endtab %}
{% endtabs %}

#### リクエストヘッダーとメソッド

Rokt `HTTP Header` Calendar には、Rokt Calendar カレンダーの接続コンテンツ認証情報名を含むフォーム認証が必要です。以下はすでにキーと値のペアとしてテンプレートに含まれていますが、\[**設定**] タブでは、`<Rokt-Calendar-API>`にある認証情報名に置き換える必要があります。`Manage Settings > Connected Content > Credential`

{% raw %}
- **HTTP メソッド**:ポスト
- **リクエストヘッダー**:
  - **認可**:ベアラー `{% connected_content https://api.roktcalendar.com/oauth2/token :method post :basic_auth <Rokt-Calendar-API> :body grant_type=client_credentials :save token :retry %}{{token.access_token}}`
  - **Content-Type**: application/json
{% endraw %}

#### Request body

{% tabs local %}
{% tab Send a new event %}
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
{% tab Update an existing event %}
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
{% tab Event details %}
次のフィールドには、イベントレベルでカスタマイズできる情報が含まれています。

| フィールド             | 定義       | 例          |
| ----------------  | ---------------- | ---------------- |
| `eventId`<br>* **必須** | 追加または更新するイベントの一意の識別子 | `Event_00001`
| `eventTitle`<br>* **必須** | カレンダーに表示される予定のタイトル | 2019年サマーセール
| `eventDescr` | カレンダーに表示される予定の説明 | セールは3日間続きます。`www.mybusiness.com/sale`このリンクをクリックしてオファーをご覧ください。 |
| `eventLocation` | カレンダーに表示されるイベントの場所。これは、EventTitleを補完する2つ目のアクション・コールとしてよく使用されることに注意してください。 | イベントを開くと 50% オフになります |
| `eventStart`<br>* **必須**  | カレンダーに表示されるイベントの開始日時 | `2019-02-21T15:00:00` |
| `eventEnd`<br>* **必須**  | カレンダーに表示されるイベントの開始日時 | `2019-02-21T16:00:00` |
| `eventTz`<br>* **必須**  | カレンダーに表示されるイベントのタイムゾーン。[適用可能なタイムゾーンのリストはこちらにあります](https://roktcalendar-api.readme.io/docs/timezones)。 | `Eastern Standard Time` |
| `notifyBefore`<br>* **必須**  | カレンダーに表示されるイベントのリマインダー時間。分単位で表されることに注意してください | `15` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% endtab %}
{% endtabs %}

{% alert tip %}
有効なタイムゾーンのリストについては、を参照してください[https://roktcalendar-api.readme.io/reference/timezones](https://roktcalendar-api.readme.io/reference/timezones)。
{% endalert %}

### ステップ3:リクエストをプレビューする

**プレビューパネルでリクエストをプレビューするか**、「**テスト**」タブに移動すると、ランダムなユーザーや既存のユーザーを選択したり、独自のユーザーをカスタマイズしてWebhookをテストしたりできます。

{% alert important %}
ページを離れる前に、テンプレートを保存することを忘れないでください！<br>[新しいWebhook キャンペーンを作成すると、更新されたWebhook テンプレートが「**保存済みのウェブフックテンプレート**」リストに表示されます。]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)
{% endalert %}
